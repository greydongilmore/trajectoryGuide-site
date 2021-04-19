
# Installation

There are a few ways to install **edf2bids**. For those looking to simply run the software you should install a compiled version.

## Obtain pre-compiled versions

#### Windows

For 64-bit Windows, compiled version can be found in <a href="https://drive.google.com/drive/folders/1op8Gv6sVWosIL7QQyXsUvNNjR5XXXj0j?usp=sharing" target="_blank">this google drive folder</a>. Make sure to download the latest version, the zipped folders contain the date of compiling.

## Compile from source

The source code can be download from the <a href="https://github.com/greydongilmore/edf2bids" target="_blank">GitHub repository</a>.

### Python Setup

First you will need to install Python, depending on what operating system you are using there are different approaches.

#### Windows

1. You will need to download the <a href="https://www.python.org/downloads/windows/" target="_blank">windows python installer</a>.
2. Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x
3. Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit
4. Install by double-clicking on the downloaded file.

#### Mac

1. Install Homebrew by opening a Terminal window and pasting the following line. 

```console
/usr/bin/ruby -e $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)
```

2. Homebrew asks you to enter your password so it can finalize the installation. Enter your user account password and hit enter
3. Once Homebrew has finished installing, return to your terminal and run the following command:

```console
brew install python3
```

#### Linux

1. Open a terminal window and run the following commands:

```console
sudo apt-get install python3.6
sudo apt install python3-pip
```

### Compiling

## Other Useful Software

### EDFBrowser

<a href="https://www.teuniz.net/edfbrowser/" target="_blank">EDFBrowser</a> (developed by Teunis van Beelen) is a free, open-source, viewer/toolbox for EEG/IEEG data. It is a great tool to use when attempting to organize your input directory for **edf2bids**.

#### Windows

For 64-bit windows download <a href="https://www.teuniz.net/edfbrowser/setup_edfbrowser_177_64bit.zip" target="_blank">this file</a>.

For 32-bit Windows download <a href="https://www.teuniz.net/edfbrowser/setup_edfbrowser_177_32bit.zip" target="_blank">this file</a>.

#### Mac

You can download the latests `.dmg` file from <a href="https://gitlab.com/whitone/EDFbrowser/-/releases" target="_blank">this website</a>.

#### Linux

To install on Linux, you must first have the dependencies installed (`g++`, `Qt5`):

```sh
sudo apt-get update
sudo apt-get install g++ make git qtbase5-dev-tools qtbase5-dev qt5-default
```

Then enter the following commands to download and install:

```sh
git clone https://gitlab.com/Teuniz/EDFbrowser.git
cd EDFbrowser
qmake
make -j4
sudo make install
edfbrowser
```

