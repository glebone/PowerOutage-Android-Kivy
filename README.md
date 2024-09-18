# Kivy Development Environment Setup on macOS and Arch Linux

This guide will walk you through setting up a Kivy development environment on macOS and Arch Linux, including installing necessary tools, setting up environment variables, building APKs, and signing them.

## 1. Install Homebrew (macOS Only)

Homebrew is a package manager for macOS that simplifies the installation of software.

### macOS
1. **Install Homebrew**:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. **Verify Homebrew Installation**:
    ```bash
    brew --version
    ```

## 2. Install Python and Set Up a Virtual Environment

### macOS
1. **Install Python**:
    ```bash
    brew install python
    ```

### Arch Linux
1. **Install Python**:
    ```bash
    sudo pacman -S python
    ```

### Set Up the Virtual Environment
1. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv kivy_venv
    source kivy_venv/bin/activate
    ```
2. **Upgrade `pip` and Install Kivy and Buildozer**:
    ```bash
    pip install --upgrade pip
    pip install cython kivy buildozer
    ```

## 3. Set Environment Variables for Android Development

### Install Android SDK and NDK

#### macOS
1. **Install Android SDK and NDK**:
    ```bash
    brew install --cask android-sdk
    brew install --cask android-ndk
    ```

#### Arch Linux
1. **Install Android SDK and NDK**:
    ```bash
    sudo pacman -S android-sdk android-ndk
    ```

### Set Up Environment Variables

#### macOS & Arch Linux
1. **Set Environment Variables**:
    Add the following lines to your `~/.zshrc` or `~/.bash_profile` (or `~/.bashrc` on Arch Linux):
    ```bash
    export ANDROIDSDK=/usr/local/share/android-sdk
    export ANDROIDNDK=/usr/local/share/android-ndk
    export ANDROID_HOME=$ANDROIDSDK
    export PATH=$ANDROIDSDK/tools:$ANDROIDSDK/platform-tools:$ANDROIDNDK:$PATH
    ```
2. **Apply the Changes**:
    ```bash
    source ~/.zshrc   # or source ~/.bash_profile or ~/.bashrc
    ```

## 4. Install Java

Java is required to build Android apps. The Android Gradle plugin requires Java 17.

### macOS
1. **Install Java 17**:
    ```bash
    brew install openjdk@17
    ```

### Arch Linux
1. **Install Java 17**:
    ```bash
    sudo pacman -S jdk17-openjdk
    ```

### Set Up Java Environment Variables

#### macOS & Arch Linux
1. **Set Java Environment Variables**:
    Add the following to your `~/.zshrc` or `~/.bash_profile` (or `~/.bashrc` on Arch Linux):
    ```bash
    export JAVA_HOME=$(/usr/libexec/java_home -v 17)   # macOS
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk      # Arch Linux
    export PATH=$JAVA_HOME/bin:$PATH
    ```
2. **Apply the Changes**:
    ```bash
    source ~/.zshrc   # or source ~/.bash_profile or ~/.bashrc
    ```
3. **Verify Java Installation**:
    ```bash
    java -version
    ```

## 5. Build the APK

1. **Navigate to Your Project Directory**:
    ```bash
    cd /path/to/your/project
    ```
2. **Ensure Your Virtual Environment is Activated**:
    ```bash
    source kivy_venv/bin/activate
    ```
3. **Build the APK**:
    ```bash
    buildozer -v android debug
    ```
    The APK will be generated in the `bin/` directory.

## 6. Sign the APK

If you are building a release version of the APK, you need to sign it:

1. **Generate a Keystore** (if you don’t have one already):
    ```bash
    keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
    ```
2. **Sign the APK**:
    ```bash
    jarsigner -verbose -keystore my-release-key.keystore ./bin/myapp-release-unsigned.apk my-key-alias
    ```
3. **Align the APK**:
    ```bash
    zipalign -v 4 ./bin/myapp-release-unsigned.apk ./bin/myapp-release.apk
    ```

## 7. Install the APK on an Android Device

1. **Connect Your Android Device**:
   - Enable USB debugging on your Android device and connect it via USB.

2. **Install the APK**:
   ```bash
   adb install ./bin/myapp-release.apk
