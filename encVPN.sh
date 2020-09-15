#!/bin/bash
BASEDIR=$(dirname "$0")

# pass 2 args, encrypt+transfer
if [ $# -eq 2 ];then
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

    #===encryption======#
    #obtain password
    echo "begin encryption"
    read -s -p "enter password(press Enter to use default passwd 'abc'): " passwd
    if [ -z "$passwd" ];then
        passwd="abc"
    fi
    echo
    #echo "$passwd"
    #python3 ./aes256.py -e -input $1 -key $passwd
    python3 ${BASEDIR}/aes256.py -e -input $1 -key $passwd
    #====transfer===#
    echo "start transmission encrypted file to $2"
    scp $1.enc $2
    # remove encrypted file
    rm $1.enc

# pass 1 arg, decrypt
elif [ $# -eq 1 ];then
    echo "begin decryption"
    read -s -p "enter password(press Enter to use default passwd 'abc'): " passwd
    if [ -z "$passwd" ];then
        passwd="abc"
    fi
    echo
    #python3 ./aes256.py -d -input $1 -key $passwd
    python3 ${BASEDIR}/aes256.py -d -input $1 -key $passwd

else
    echo "use commands: ./envVPN.sh decrypted-file or ./encVPN.sh original-file destination"
fi

echo "done"
