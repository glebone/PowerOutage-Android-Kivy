[app]

# (str) Title of your application
title = Power Outage Schedule

# (str) Package name
package.name = poweroutageschedule

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourname

# (str) Source code where the main.py file is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Kivy is required, matplotlib for plotting, re and other built-in modules are included automatically
requirements = kivy, matplotlib

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The entry point of your application
entrypoint = main.py

# (list) Permissions
android.permissions = INTERNET

# (list) Features
# Uncomment and add the features you need
# android.features = android.hardware.usb.host

# (str) Application icon
icon.filename = icon.png

# (str) Supported platforms
# Available options: android, ios, tvos, macosx, win, linux, web
# You can specify a list of supported platforms separated by commas.
# For example, platforms = android,ios
platforms = android

# (str) Presplash of the application
# presplash.filename = presplash.png

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# adaptive_icon.foreground = res/icon_fg.png
# adaptive_icon.background = res/icon_bg.png

# (list) Add custom java compile options
# java.compile.options = -source 1.8 -target 1.8

# (list) Add custom options to the gradle build
# android.gradle_arguments = --no-daemon

# (str) Custom package data (android only)
# android.package_data_dir = /data/data/org.yourname.poweroutageschedule/files

# (str) Android API level to use
android.api = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android's LogCat output for logging
logcat = True

# (list) Android additional libraries
# android.add_libs_armeabi_v7a = libs/android/*.so
# android.add_libs_arm64_v8a = libs/android/*.so

# (list) Java classes to add as activities
# android.add_activities = com.example.ExampleActivity

# (list) Android add Jars libraries
# android.add_jars = path/to/library.jar

# (str) Custom presplash color (for Android and iOS)
# presplash.color = #FFFFFF

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The build type used for packaging (debug or release)
# android.build_type = debug

# (str) Build a bundle instead of an APK. (aab or apk)
# android.arch = armeabi-v7a

# (str) Keystore file
# android.release_keystore = my_keystore.keystore

# (str) Keystore password
# android.release_keystore_password = my_keystore_password

# (str) Key alias
# android.release_keyalias = my_keyalias

# (str) Key password
# android.release_keyalias_password = my_keyalias_password

# (list) Screenshots
# (list) Supported screen densities
# android.supported_screens = small, normal, large, xlarge

# (str) Asset directories to be included (comma separated)
# android.add_asset_dirs = assets

# (str) Gradle options to be passed to the build
# android.gradle_options = "-Dorg.gradle.jvmargs=-Xmx1024m"

# (bool) Copy the Android build directory to the source directory after building
# copy_to_source_dir = False

# (list) Patterns to exclude from the final APK
# exclude_patterns = *.pyc

# (str) Path to Android SDK
# android.sdk_path = /path/to/android/sdk

# (str) Path to Android NDK
# android.ndk_path = /path/to/android/ndk

# (str) Android NDK toolchain
# android.ndk_toolchain = arm-linux-androideabi-4.9

# (str) Path to Java JDK
# java.jvm_path = /path/to/jdk

# (str) Custom build directory
# build_dir = /path/to/build

# (bool) Enable the custom build directory
# custom_build_dir = False

# (str) Path to buildozer cache directory
# cache_dir = /path/to/cache

# (bool) Disable the compilation of C code
# android.disable_cython = False

# (bool) If True, does not try to install the app after building
# no_install = False

# (bool) If True, uses a virtual machine to build
# use_virtualenv = False

# (str) Directory in which the virtual environment should be created
# virtualenv_dir = .buildozer/venv

# (bool) Do not use the virtual environment to run build commands
# no_virtualenv = False

# (bool) Force re-creating the virtual environment
# force_virtualenv = False

# (bool) Use SDL2 instead of Pygame
# use_sdl2 = True

# (bool) If True, will ask for confirmation before running any dangerous commands
# confirm_before_command = True

# (str) Path to the Android manifest template
# android.manifest = AndroidManifest.tmpl.xml

# (str) Path to the build script
# build_script = build.py

# (str) Path to the requirements file
# requirements_file = requirements.txt

# (list) Additional build commands
# build_commands = build_all

# (str) Path to the dist directory
# dist_dir = dist

# (str) Path to the src directory
# src_dir = src

# (str) Path to the bin directory
# bin_dir = bin

# (str) Path to the tmp directory
# tmp_dir = tmp

# (str) Path to the lib directory
# lib_dir = lib

# (str) Path to the data directory
# data_dir = data

# (str) Path to the res directory
# res_dir = res

# (str) Path to the assets directory
# assets_dir = assets

# (str) Path to the templates directory
# templates_dir = templates

# (str) Path to the test directory
# test_dir = test

# (str) Path to the tools directory
# tools_dir = tools

# (str) Path to the config directory
# config_dir = config

# (str) Path to the log directory
# log_dir = log

# (str) Path to the build directory
# build_dir = build

# (str) Path to the .buildozer directory
# buildozer_dir = .buildozer

# (bool) If True, will build in debug mode
# debug = False

# (bool) If True, will build in release mode
# release = False

# (bool) If True, will sign the APK with the debug key
# sign = False

# (bool) If True, will zipalign the APK
# zipalign = False

# (bool) If True, will verify the APK
# verify = False

# (bool) If True, will install the APK
# install = False

# (bool) If True, will run the app after installing
# run = False

# (bool) If True, will clean the build directory before building
# clean = False

# (bool) If True, will clean the cache directory before building
# clean_cache = False

# (bool) If True, will update the project before building
# update = False

# (bool) If True, will build the project even if it is up to date
# force_build = False

# (bool) If True, will use the default configurations
# default = False

# (bool) If True, will print the version of Buildozer
# version = False

# (bool) If True, will show the help message
# help = False

# (bool) If True, will show the usage message
# usage = False

# (bool) If True, will show the commands
# commands = False

# (bool) If True, will show the options
# options = False

# (bool) If True, will show the values
# values = False

# (bool) If True, will show the dependencies
# dependencies = False

# (bool) If True, will show the environment variables
# environment = False

# (bool) If True, will show the configuration
# configuration = False

# (bool) If True, will show the commands in the buildozer.spec file
# show_commands = False

# (bool) If True, will show the options in the buildozer.spec file
# show_options = False

# (bool) If True, will show the values in the buildozer.spec file
# show_values = False

# (bool) If True, will show the dependencies in the buildozer.spec file
# show_dependencies = False

# (bool) If True, will show the environment variables in the buildozer.spec file
# show_environment = False

# (bool) If True, will show the configuration in the buildozer.spec file
# show_configuration = False

# (bool) If True, will show the commands in the buildozer.spec file
# show_commands_in_spec = False

# (bool) If True, will show the options in the buildozer.spec file
# show_options_in_spec = False

# (bool) If True, will show the values in the buildozer.spec file
# show_values_in_spec = False

# (bool) If True, will show the dependencies in the buildozer.spec file
# show_dependencies_in_spec = False

# (bool) If True, will show the environment variables in the buildozer.spec file
# show_environment_in_spec = False

# (bool) If True, will show the configuration in the buildozer.spec file
# show_configuration_in_spec = False

# (bool) If True, will run the tests
# test = False

# (bool) If True, will show the logs
# log = False

# (bool) If True, will show the verbose logs
# verbose = False

# (bool) If True, will show the debug logs
# debug = False

# (bool) If True, will show the error logs
# error = False

# (bool) If True, will show the warning logs
# warning = False

# (bool) If True, will show the critical logs
# critical = False

# (bool) If True, will show the help message for the given command
# help_command = False

# (str) The command to run
# command =

# (str) The arguments to pass to the command
# args =

# (str) The options to pass to the command
# options =

# (str) The values to pass to the command
# values =

# (str) The environment variables to set
# env =

# (str) The configuration file to use
# config =

# (str) The log file to use
# logfile =

# (str) The PID file to use
# pidfile =

# (str) The user to run as
# user =

# (str) The group to run as
# group =

# (str) The umask to use
# umask =

# (str) The working directory to use
# chdir =

# (str) The stdin file to use
# stdin =

# (str) The stdout file to use
# stdout =

# (str) The stderr file to use
# stderr =

# (str) The program to execute
# exec =

# (str) The arguments to pass to the program
# exec_args =

# (str) The options to pass to the program
# exec_options =

# (str) The values to pass to the program
# exec_values =

# (str) The environment variables to set for the program
# exec_env =

# (str) The configuration file to use for the program
# exec_config =

# (str) The log file to use for the program
# exec_logfile =

# (str) The PID file to use for the program
# exec_pidfile =

# (str) The user to run the program as
# exec_user =

# (str) The group to run the program as
# exec_group =

# (str) The umask to use for the program
# exec_umask =

# (str) The working directory to use for the program
# exec_chdir =

# (str) The stdin file to use for the program
# exec_stdin =

# (str) The stdout file to use for the program
# exec_stdout =

# (str) The stderr file to use for the program
# exec_stderr =

# (bool) If True, will show the help message for the program
# exec_help = False

# (str) The command to run for the program
# exec_command =

# (str) The arguments to pass to the program command
# exec_args =

# (str) The options to pass to the program command
# exec_options =

# (str) The values to pass to the program command
# exec_values =

# (str) The environment variables to set for the program command
# exec_env =

# (str) The configuration file to use for the program command
# exec_config =

# (str) The log file to use for the program command
# exec_logfile =

# (str) The PID file to use for the program command
# exec_pidfile =

# (str) The user to run the program command as
# exec_user =

# (str) The group to run the program command as
# exec_group =

# (str) The umask to use for the program command
# exec_umask =

# (str) The working directory to use for the program command
# exec_chdir =

# (str) The stdin file to use for the program command
# exec_stdin =

# (str) The stdout file to use for the program command
# exec_stdout =

# (str) The stderr file to use for the program command
# exec_stderr =
