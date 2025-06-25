#!/bin/bash
set -x
export CA_PWD="Password123jkh!"

# CONST
COUNTRY="FR"
STATE="Paris"
CITY="Paris"
ORG="ORG-Test"
ORG_UNIT="TEST-UNIT"
EMAIL="medarbiachour@gmail.com"

# Read Common Name (CN)
#read -p "PLEASE ENTER COMMON NAME (CN): " COMMON_NAME


#client_name=$(hostname)
client_name=$(hostname)
dir="client-certs"
echo "Creating Client Key for $client_name"
openssl genrsa -out client.key 2048
echo "Creating certificate request"
#openssl req -new -out client.csr -key client.key
openssl req -new -key client.key -out client.csr -subj "/C=$COUNTRY/ST=$STATE/L=$CITY/O=$ORG/OU=$ORG_UNIT/CN=$client_name/emailAddress=$EMAIL"
echo "Signing client certificate with CA key"
echo "The CA key File must be in the server-certs folder"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 9999 -passin env:CA_PWD
# Exécutez la commande OpenSSL avec les valeurs spécifiées
if [ -d $dir ];then
 echo "directory Exists"
else
 mkdir $dir
fi

echo ""mv client.* $dir