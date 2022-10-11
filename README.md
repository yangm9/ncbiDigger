# ncbiDigger 

## 1 Description

ncbiDigger is designed to get the information for some accession id. 

## 2 Software Architecture


## 3 Installation

#### 3.1 Google Chrome and Chrome Driver 

It is necessary to download and install the [Google Chrome](https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm) and the [Chrome Driver](https://chromedriver.chromium.org/downloads), and the bash scripts are as follows:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
cd ~/software
rpm2cpio google-chrome-stable_current_x86_64.rpm | cpio -div
cd usr/bin
unlink google-chrome* # delete the original link 
ln -s ../../opt/google/chrome/google-chrome # create a new link for google-chrome
./google-chrome --version # print the version of Google Chrome，such as Google Chrome 97.0.4692.99

#Download the corresponding version of chromedriver in the current directory.
wget https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
#### 3.2 Dependency Installation

## 4 Instructions

1.  xxxx
2.  xxxx
3.  xxxx


## 5 Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request

## 6 Version updates

