#!/bin/bash
[ -z $1 ] && echo "usage $0 <host_name>" && exit -1;

openssl s_client -servername $1 -connect $1:443 2>&1 < /dev/null |
openssl x509 -pubkey -noout |
openssl rsa -pubin -outform der 2>/dev/null |
openssl dgst -sha256 -binary | openssl enc -base64