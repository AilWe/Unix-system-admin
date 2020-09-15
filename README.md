# encryption_inside_vpn-raspberry
Description:
This project is used to provide file encryption service during data
transmission through a VPN pipline on raspberry platform.

Platform:
Currently we will use the ubuntu 18.04 platform on common desktop and
raspbian Buster on Raspberry Pi b 3+ device.

Preinstall:
sudo apt update;
sudo apt install net-tools python3 python3-pip;
pip3 install pycrypto;


Usage:
1)encryption & transmission:
./encVPN filename remote_address
2) decryption:
./encVPN encrypted_filename
3) detectVPN:
./detectVPN
4)encrypt file with AES algorithm:
python3 aes256.py -e -input yourfile -key yourkey
5)decrypt file with AES algorithm:
python3 aes256.py -d -input yourfile -key yourkey

This tool can be used no matter VPN is actived or not. However, it can automatically check VPN status and require user's approval to continue.
