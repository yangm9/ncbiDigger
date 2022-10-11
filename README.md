# ncbiDigger 

## 1 Description


## 2 Software Architecture


## 3 Installation

It is necessary to download and install the [Google Chrome](https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm) and the [Chrome Driver](https://chromedriver.chromium.org/downloads), and the bash scripts are as follows:
```
#下载谷歌浏览器并安装
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
cd ~/software # 进入安装目录
rpm2cpio google-chrome-stable_current_x86_64.rpm | cpio -div #解压安装rpm
cd usr/bin # 进入程序所在目录
unlink google-chrome* # 删除原有废弃链接
ln -s ../../opt/google/chrome/google-chrome # 创建新的链接文件
./google-chrome --version # 查看浏览器版本，显示为Google Chrome 97.0.4692.99

#在当前目录下载对应版本的chromedriver
wget https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

1.  xxxx
2.  xxxx
3.  xxxx


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

