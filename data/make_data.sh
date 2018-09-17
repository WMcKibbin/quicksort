#!/bin/bash

seq $1 | xargs -I SEQ bash -c "od -vAn -N2 -tu2 < /dev/urandom" | awk "{\$1=\$1};1"
