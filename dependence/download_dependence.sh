#下载谷歌浏览器并安装
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
rpm2cpio google-chrome-stable_current_x86_64.rpm | cpio -div
cd usr/bin
unlink google-chrome*
ln -s ../../opt/google/chrome/google-chrome
./google-chrome --version

