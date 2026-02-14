[app]

# (str) Title of your application
title = TRACKH2O

# (str) Package name
package.name = trackh2o

# (str) Package domain (needed for android packaging)
package.domain = org.sih

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's include kv files explicitly)
source.include_exts = py,kv,png,jpg,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Note: Adding 'sqlite3' or 'openssl' here if your app uses databases/web APIs
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the develop branch of p4a (Only if master fails)
p4a.branch = master

# (str) Android NDK directory (leave empty to download it)
android.ndk_path = 

# (str) Android SDK directory (leave empty to download it)
android.sdk_path = 

# (bool) If True, then skip trying to update the libs
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to exclude from the build
source.exclude_patterns = license, .git, .github

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Androidx, register for modern libraries
android.enable_androidx = True

# (int) Log level (2 = error/warning, 1 = info, 0 = debug)
log_level = 2

# (int) display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build work directory
build_dir = ./.buildozer

# (str) Path to bin directory
bin_dir = ./bin
