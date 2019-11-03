# Looking for Android / iPhone / iPad versions?

We have recently launched our mobile versions in Google Play Store and Apple App Store.

Illustrated User Manual: <a href='https://www.uniquebible.app/mobile'>https://www.uniquebible.app/mobile</a><br>
Links for downloads: <a href='https://www.uniquebible.app/download'>https://www.uniquebible.app/download</a>

# UniqueBible
A cross-platform & offline bible application, integrated with high-quality resources and unique features.

<b>Tested in:</b> Windows, macOS and Linux (Ubuntu & Mint)

(developed with Python [version: 3.7.2])

Visit <a href="https://BibleTools.app" target="_blank">https://BibleTools.app</a> for further information.

# Pre-requisite

The "desktop" version of "UniqueBible.app" is programmed with python library.  Users have to install python library first in order to run "UniqueBible.app" on your desktop OS.

Go to <a href="https://www.python.org">https://www.python.org</a> for instructions on installation of python for FREE.

# Install Dependencies

pip3 install PySide2
<br>(PySide2 is required for graphical user interface, used by UniqueBible.app.)

pip3 install PyPDF2
<br>(PyPDF2 is required for reading text from *.pdf documents.)

pip3 install python-docx
<br>(python-docx is required for reading text from *.docx documents.)

pip3 install gdown
<br>(gdown is required for downloading database files stored in google drive.)

# Download & Run UniqueBible.app

Click on the download button on this page to download a zip copy of this repository, i.e. "UniqueBible-master.zip".

<img src="downloadButton.png">

# Example: Install & Run on macOS / Linux

1. Use the download button on this page to download a zip copy.<br>
2. This example assume that your downloaded file is located in "Downloads" of your home directory, i.e. ~/Downloads/.<br>
3. Open terminal and enter all the following commands:<br>
cd ~<br>
unzip ~/Downloads/UniqueBible-master.zip<br>
cd UniqueBible-master<br>
python3 -m venv venv<br>
source venv/bin/activate<br>
pip3 install PySide2<br>
pip3 install PyPDF2<br>
pip3 install python-docx<br>
pip3 install gdown<br>
4. To run the app that installed with the previous 3 steps, enter the following command in terminal:<br>
python3 main.py<br>

# Example: Install & Run on Windows

1. Use the download button on this page to download a zip copy.<br>
2. Unzip the downloaded file "UniqueBible-master.zip" into a folder, e.g. "c:\UniqueBible-master"<br>
3. Open command prompt and enter all the following commands:<br>
python -m venv c:\UniqueBible-master\venv<br>
cd c:\UniqueBible-master<br>
.\venv\Scripts\activate<br>
pip3 install PySide2<br>
pip3 install PyPDF2<br>
pip3 install python-docx<br>
pip3 install gdown<br>
4. To run the app that installed with the previous 3 steps, enter the following command in terminal:<br>
python3 main.py<br>

# Example: Install & Run on Chrome OS
1. Enable Linux apps: Open your Chrome OS Settings app, find “Linux Apps” and click “Turn On“. Your Chromebook will download the required files to use Linux apps. When complete, a new Terminal app will open.<br>
To get the latest update, in Linux terminal, enter:<br>
sudo apt udpate<br>
sudo apt full-upgrade<br>
2. Make sure you have "wget" installed, by running the following commands in Linux terminal:<br>
sudo apt install wget<br>
3. Make sure you have "python" library & tools are in place:<br>
sudo apt install python3<br>
sudo apt install python3-setuptools<br>
sudo apt install python3-pip<br>
4. Install dependencies for this app, enter the following command:<br>
pip3 install --user PySide2<br>
pip3 install --user PyPDF2<br>
pip3 install --user python-docx<br>
pip3 install --user gdown<br>
[Remarks: In our testings, command "pip3 install PySide2" encounters memory errors on some low-memory chromebooks.  You may install wheel from Qt servers with this command instead:<br>
pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2 --trusted-host download.qt.io<br>
Reference: https://wiki.qt.io/Qt_for_Python/GettingStarted]<br>
5. Export PATH<br>
* temporary solution - enter this command in terminal:<br>
export PATH=$PATH:$HOME/.local/bin<br>
* permanent solution - add the following line at the end of file ".bashrc" in the home directory:<br>
export PATH=$PATH:$HOME/.local/bin<br>
[close and re-open the Linux terminal after saving the changes in file ".bashrc"]<br>
6. Download the app in a zip file, enter in terminal:<br>
cd ~<br>
wget https://github.com/eliranwong/UniqueBible/archive/master.zip<br>
unzip master.zip<br>
cd UniqueBible-master<br>
7. Run the app, enter in Linux terminal:<br>
cd ~/UniqueBible-master/ && python3 main.py<br>
8. Create a shortcut, add the following line at the end of file ".bashrc" in the home directory:<br> 
alias uba="cd ~/UniqueBible-master/ && python3 main.py"<br>
[close and re-open the Linux terminal after saving the changes in file ".bashrc"]<br>
9. Run the app with shortcut in terminal:<br>
uba

# Creating a Shortcut

There are various ways to create a shortcut, below are some examples:<br>
For macOS / Linux: https://github.com/eliranwong/UniqueBible/blob/master/shortcut_uba_macOS_Linux.sh<br>
Linux / Chrome OS: https://github.com/eliranwong/UniqueBible/blob/master/shortcut_uba_Linux.desktop<br>
Windows: https://github.com/eliranwong/UniqueBible/blob/master/shortcut_uba_Windows.bat<br>
<i>Remarks: Change paths in the files above according to where you place the app's folder on your devices.</i>

# Where are the Database Files?

All codes for running the app is shared in this repository.

Github has restrictions on upload size.  For this reason, full set of database files is not able to be uploaded here.

To run UniqueBible.app and its features, several database files are required.  To help you about installing particular datasets, <b>"Download Helper"</b> comes up automatically, when a database file is needed for a particular feature.

You can also manually install <b>"ALL"</b> https://marvel.bible datasets via our menu bar.<br>
Go to "Resources" > "Install Marvel.bible Datasets"

<i><b>Remarks:</b></i> It takes time for large files to be downloaded.  The core datasets for running UniqueBible.app is 49MB in size.  You may need to wait for a while for downloading it after you first launched UniqueBible.app.

In ADDITION to official UniqueBible.app data, we support various <b>3rd party modules</b>.  Please see <a href="https://github.com/eliranwong/UniqueBible#3rd-party-resources">below</a> for details.

# Screenshot:

<img src="screenshot.png">

# 3rd Party Resources

In addition to Marvel.bible modules and datasets, UniqueBible.app has a built-in converter.<br>
The built-in converter supports import of the following third-party modules:<br>

* MySword Bible Modules (<a href="https://mysword.info/download-mysword/bibles">https://mysword.info/download-mysword/bibles</a>)

* MySword Commentary Modules (<a href="https://mysword.info/download-mysword/commentaries">https://mysword.info/download-mysword/commentaries</a>)

* MySword Dictionary Modules (<a href="https://mysword.info/download-mysword/dictionaries">https://mysword.info/download-mysword/dictionaries</a>)

* e-Sword Bible Modules [Apple / macOS / iOS (*.bbli)] (<a href="https://www.e-sword.net">https://www.e-sword.net</a>)

* e-Sword Commentary Modules [Apple / macOS / iOS (*.cmti)] (<a href="https://www.e-sword.net">https://www.e-sword.net</a>)

* e-Sword Dictionary Modules [Apple / macOS / iOS (*.dcti)] (<a href="https://www.e-sword.net">https://www.e-sword.net</a>)

* e-Sword Lexicon Modules [Apple / macOS / iOS (*.lexi)] (<a href="https://www.e-sword.net">https://www.e-sword.net</a>)

* e-Sword Book Modules [Apple / macOS / iOS (*.refi)] (<a href="https://www.e-sword.net">https://www.e-sword.net</a>)

* MyBible Bible Modules (<a href="https://www.ph4.org/b4_my.php?k=bibles&q=mybible">https://www.ph4.org/b4_my.php?k=bibles&q=mybible</a>)

* MyBible Commentary Modules (<a href="https://www.ph4.org/b4_my.php?k=commentaries&q=mybible">https://www.ph4.org/b4_my.php?k=commentaries&q=mybible</a>)

* MyBible Dictionary Modules (<a href="https://www.ph4.org/b4_my.php?k=dictionary&q=mybible">https://www.ph4.org/b4_my.php?k=dictionary&q=mybible</a>)

* More MySword / e-Sword modules are available at: <a href="http://www.biblesupport.com">http://www.biblesupport.com</a>

Users need to download 3rd party modules separately.<br><br>
Built-in converter can be accessed via our menu bar:<br>
Go to menu "Resources" > "Import 3rd Party Modules"<br>
For import of <b>multiple files in one go</b>:<br>
Put 3rd party modules, which you want to import, in a folder.<br>
Go to menu "Resources" > "Import Supported 3rd Party Modules in a Folder"

<b>Disclaimer</b>: All third-party modules are created by third parties. UniqueBible.app does not endorse any particular theological views or individual content of these 3rd-party modules. Please contact individual module creators or parties if you have issues with their content. UniqueBible.app is NOT responsible for any third-party modules in terms of their quality or content. Users should only use these third-party modules with their own judgment and at their own risks.

# Donations:

Please consider a donation via our PayPal account:
<a href="https://www.paypal.me/MarvelBible">https://www.paypal.me/MarvelBible</a>

