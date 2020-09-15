#!/bin/bash

# check VPN status
tunStr=$(ifconfig -a | grep tun)
if [ -z "$tunStr" ];then
    echo "VPN Not Activated..."
    read -p "Do you want to continue? y|n: " cntFlag
    while [ "$cntFlag" != "y" ] && [ "$cntFlag" != "n" ]
    do
        read -p "Do you want to continue? please give 'y' or 'n': " cntFlag
    done
    if [ "$cntFlag" = "n" ];then
        echo "exit"
        exit 0
    fi
else
    echo "VPN activated..."
fi
echo "test"
