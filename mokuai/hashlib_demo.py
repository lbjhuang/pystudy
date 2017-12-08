# -*- coding: UTF-8 -*-
import hashlib


# ######## md5 ########
hash = hashlib.md5(bytes('huang',encoding="utf-8"))  #创建一个md5对象(并加盐huang字符串混合提高保密性)
# help(hash.update)
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
#print(hash.digest())

######## sha1 ########

hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())