#!/bin/bash
mkdir -p certs
openssl req -x509 -newkey rsa:4096 -nodes -out certs/certificate.pem -keyout certs/key.pem -days 500