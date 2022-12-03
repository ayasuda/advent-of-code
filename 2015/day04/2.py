#!/usr/bin/env python3.9

import hashlib

secret = "ckczppom"


cnt = 0
while True:
    source = f'{secret}{cnt}'.encode("utf-8")

    md5 = hashlib.md5(source).hexdigest()
    if md5[0:6] == "000000":
        print(cnt)
        break

    if cnt % 10000 == 0:
        print(f'{cnt} checked')
    cnt += 1
