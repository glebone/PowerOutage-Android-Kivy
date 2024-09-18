[app]

# (str) Title of your application
title = Moon Phase Calculator

# (str) Package name
package.name = moonphase

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# android.permissions = android.permission.INTERNET

# (int) Android API level to target
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Enable backup for the app
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or aar)
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar)
android.debug_artifact = apk

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False
log_level = 2
