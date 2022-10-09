# ncbiDigger
## 1 介绍
## 2 安装教程
#### 1.1 安装谷歌浏览器和驱动
谷歌浏览器下载地址：
https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
谷歌浏览器驱动下载地址：
https://chromedriver.chromium.org/downloads
下载和安装代码如下：
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
完成以上操作，google的环境配置即已完成，只不过后续需要指定chromedriver的全路径。需要注意的是google-chrome和chromedriver的版本一定要配套一致，不然会落入无尽的坑中。

## 3 使用说明
## 4 事项

## 5 版本更新日志

