#!/usr/bin/bash
sed -i -e 's/\*/'\''/g' -e 's/O1P/OP1/g' -e 's/O2P/OP2/g' $1
