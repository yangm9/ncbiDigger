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
#### 3.1 输入文件
输入文件为accession ID的列表，目前仅支持Assembly和BioProject的ID。
输入文件示例：
[assembly.list](example/assembly.list)
或
[project.list](example/project.list)

#### 3.2 用法
    
ncbiDigger.py -i <accession_list> [-t <accession_type>] -o <out_dir>
        <accession_list>: NCBI assembly accession list file, i.e., GCA_013202315.1\\nGCA_013202525.1\\n
        <accession_type>: Accession ID type, i.e., Assembly, Project
        <out_dir>: output directory
用法举例：
```
ncbiDigger.py -i assembly.list -t Assembly -o .
ncbiDigger.py -i project.list -t Project -o .
```
参见example目录中的脚本。

## 4 事项
#### 4.1 注意事项
#### 4.2 待办事项
1) BioProject中某些ID会搜索到多个项目，导致无法爬取，此事需要解决。

## 5 版本更新日志

ncbiDigger-v0.01
```
1. 根据assembly编号(GCA/GCF)获取样本采集相关信息，如环境来源、经纬度等等;2. 根据BioProject编号获取项目类型、名称和摘要信息。
```
2022-10-09

