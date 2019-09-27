#!/bin/bash
# Program name: ping ip range 0-255

#read -p 'What IPv4 adress do you want to ping?: ' ip

ip2=$(echo "$1" | cut -d '.' -f1-3) 

> iplist.txt

for count in {0..255}
	do
		ping -c 1 -w 1 $ip2.$count | grep 'Reply from' | awk '{print $3}' | sort | uniq >> iplist.txt
		done 
