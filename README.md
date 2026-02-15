## WELCOME INTO THE README 
this program is code by TheNatDev360
Media Installer Py
=================

Media Installer Py is a Python-based tool designed to simplify the installation of media content directly on your device. This project aims to provide a seamless experience for Windows, Linux, and Android (via Termux) users.

Features
--------

- Cross-platform support: Windows, Linux, and Android (Termux)
- Easy dependency management
- Simple execution of your media installation scripts

Prerequisites
-------------

- Python 3.x installed on your system
- Git (optional, if you want to clone the repository)

Installation & Usage
-------------------

Step 1: Clone the repository

    git clone https://github.com/Thenatdev360/MediaInstallerPy.git
    cd MediaInstallerPy

Step 2: Install Dependencies

Before running Media Installer, you need to install the required dependencies. This depends on your operating system:

Windows:

    dependencies.bat

Linux & Termux (Android):

    chmod +x dependencies.sh
    ./dependencies.sh

if not work you use(android):

    bash dependencies.sh

> Note: Termux users: The Linux `.sh` script is fully compatible with Termux on Android.

Step 3: Run Media Installer

After installing dependencies, you can run the main program:

    python media_installer.py

Follow the on-screen instructions to install your media content.

Notes
-----

- Make sure your Python environment has the necessary permissions to execute scripts.
- If you encounter any issues on Android, ensure Termux has storage access enabled.

License
-------

This project is open-source and available under the MIT License.
