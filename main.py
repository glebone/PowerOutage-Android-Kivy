from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import mainthread
import threading
import re
import logging
from datetime import datetime, timedelta

# Import matplotlib and configure it for use with Kivy
import matplotlib
matplotlib.use('Agg')  # Use the Anti-Grain Geometry backend (no UI)
import matplotlib.pyplot as plt
from io import BytesIO
from kivy.core.image import Image as CoreImage

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Default text in Ukrainian for the multiline input, representing a sample power outage schedule.
default_text = """
❗️💡Черкащина. Відповідно до команди НЕК "Укренерго", в неділю, 1 вересня, в області будуть застосовані графіки погодинних відключень електроенергії.

Години без світла:
■ 00:00-01:00 2 черга
■ 01:00-02:00 2 черга
■ 02:00-03:00 3 черга
■ 03:00-04:00 3 черга
■ 04:00-05:00 4 черга
■ 05:00-06:00 4 черга
■ 06:00-07:00 5 черга
■ 07:00-08:00 5 черга
■ 08:00-09:00 6 черга
■ 09:00-10:00 6 черга
■ 10:00-11:00 1 черга
■ 11:00-12:00 1 черга
■ 12:00-13:00 2 черга
■ 13:00-14:00 2 черга
■ 14:00-15:00 3 черга
■ 15:00-16:00 3 черга
■ 16:00-17:00 4 черга
■ 17:00-18:00 5 та 6 черги
■ 18:00-19:00 5 та 6 черги
■ 19:00-20:00 1 та 2 черги
■ 20:00-21:00 1 та 2 черги
■ 21:00-22:00 3 та 4 черги
■ 22:00-23:00 4 черга
■ 23:00-24:00 5 черга
"""

class PowerOutageApp(App):
    def build(self):
        self.title = "Power Outage Schedule"

        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Text Input
        self.text_input = TextInput(text=default_text, multiline=True, size_hint=(1, 0.7))
        layout.add_widget(self.text_input)

        # Queue Selector
        self.queue_spinner = Spinner(
            text='Queue 3',
            values=[f'Queue {i}' for i in range(1, 7)],
            size_hint=(1, None),
            height=44
        )
        layout.add_widget(self.queue_spinner)

        # Buttons Layout
        buttons_layout = BoxLayout(size_hint=(1, None), height=44)

        # Add to Calendar Button
        add_button = Button(text='Add to Calendar')
        add_button.bind(on_press=self.on_add_to_calendar_clicked)
        buttons_layout.add_widget(add_button)

        # Draw Chart Button
        draw_button = Button(text='Draw Chart')
        draw_button.bind(on_press=self.on_draw_chart_clicked)
        buttons_layout.add_widget(draw_button)

        layout.add_widget(buttons_layout)

        # Status Label
        self.status_label = Label(text='', size_hint=(1, 0.1))
        layout.add_widget(self.status_label)

        return layout

    def update_status(self, message):
        self.status_label.text = message
        logging.debug(message)

    def parse_outage_schedule(self, text):
        pattern = re.compile(r'■ (\d{2}:\d{2})-(\d{2}:\d{2}) ((?:\d черга)|(?:\d та \d черги)|(?:\d та \d черга))')
        matches = pattern.findall(text)
        schedule = [(f"{start}-{end}", group) for start, end, group in matches]
        logging.debug(f"Parsed schedule: {schedule}")
        return schedule

    def filter_schedule(self, schedule, queue):
        queue_pattern = re.compile(rf"\b{queue}(?: черга| та {queue} черги)\b")
        filtered_schedule = [item for item in schedule if queue_pattern.search(item[1])]
        logging.debug(f"Filtered schedule for Queue {queue}: {filtered_schedule}")
        return filtered_schedule

    def extract_date_from_text(self, text):
        # Mapping of Ukrainian month names to month numbers
        month_mapping = {
            'січня': 1,
            'лютого': 2,
            'березня': 3,
            'квітня': 4,
            'травня': 5,
            'червня': 6,
            'липня': 7,
            'серпня': 8,
            'вересня': 9,
            'жовтня': 10,
            'листопада': 11,
            'грудня': 12,
        }

        date_pattern = re.compile(r'(\d{1,2})\s([а-яА-Я]+)', re.UNICODE)
        match = date_pattern.search(text)

        if match:
            day = int(match.group(1))
            month_str = match.group(2).lower()
            month = month_mapping.get(month_str)

            if month:
                date = datetime(datetime.now().year, month, day).date()
                logging.debug(f"Extracted date: {date}")
                return date
            else:
                self.update_status(f"Unknown month: {month_str}")
                logging.debug(f"Unknown month: {month_str}")
        else:
            self.update_status("Date not found in text.")
            logging.debug("Date not found in text.")

        # Fallback to current date
        return datetime.now().date()

    def on_add_to_calendar_clicked(self, instance):
        threading.Thread(target=self.add_to_calendar).start()

    def add_to_calendar(self):
        # Retrieve the text and queue
        text = self.text_input.text
        queue = int(self.queue_spinner.text.split()[1])
        event_date = self.extract_date_from_text(text)

        # Parse and filter the schedule
        schedule = self.parse_outage_schedule(text)
        filtered_schedule = self.filter_schedule(schedule, queue)

        # For demonstration, we'll just update the status with the number of events
        events_count = len(filtered_schedule)
        self.update_status(f"Total events for Queue {queue}: {events_count}")

        # TODO: Integrate Google Calendar API securely if needed

    def on_draw_chart_clicked(self, instance):
        threading.Thread(target=self.draw_chart).start()

    def draw_chart(self):
        # Retrieve the text and queue
        text = self.text_input.text
        queue = int(self.queue_spinner.text.split()[1])
        event_date = self.extract_date_from_text(text)

        # Parse and filter the schedule
        schedule = self.parse_outage_schedule(text)
        filtered_schedule = self.filter_schedule(schedule, queue)

        # Prepare data for the chart
        hours = [0] * 24
        for time_range, _ in filtered_schedule:
            start_time_str, end_time_str = time_range.split('-')
            start_hour = int(start_time_str.split(':')[0])
            end_hour = int(end_time_str.split(':')[0])

            if end_time_str == '24:00':
                end_hour = 24

            if start_hour < end_hour:
                for i in range(start_hour, end_hour):
                    hours[i] = 1
            else:
                for i in range(start_hour, 24):
                    hours[i] = 1
                for i in range(0, end_hour):
                    hours[i] = 1

        labels = [f"{i:02d}:00" for i in range(24)]
        colors = ['red' if h == 1 else 'green' for h in hours]

        plt.figure(figsize=(6, 6))
        plt.pie([1]*24, labels=labels, colors=colors, startangle=90, counterclock=False)
        plt.title(f'Power Outage Schedule for Queue {queue} on {event_date}')

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        im = CoreImage(buf, ext='png')
        self.show_image_popup(im)

    @mainthread
    def show_image_popup(self, image):
        popup = Popup(title='Power Outage Schedule', size_hint=(0.9, 0.9))
        img_widget = Image(texture=image.texture)
        popup.content = img_widget
        popup.open()

if __name__ == '__main__':
    PowerOutageApp().run()
