#!/bin/bash
#Download the Google browser and install it
if [[ ( $@ == "--help") ||  $@ == "-h" ]]
then 
    echo "Usage: $0 <installation_directory>"
    exit 0
fi

cd $1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
rpm2cpio google-chrome-stable_current_x86_64.rpm | cpio -div
cd usr/bin
unlink google-chrome*
ln -s ../../opt/google/chrome/google-chrome
./google-chrome --version

# install miniconda and python
if [ -x "$(command -v python3)" ];
then 
	wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	sh Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b
	/opt/miniconda3/bin/conda init
	source ~/.bashrc
	pip install -r requirements.txt
	echo -e "PATH=\"`pwd`:\$PATH\"" >>~/.bashrc
	source ~/.bashrc
fi
