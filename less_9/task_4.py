import hashlib

print(hashlib.sha1(b'Hello World!').hexdigest())

# 2ef7bde608ce5404e97d5f042f95f89f1c232871

print(hashlib.sha1(b'Hello World.').hexdigest())

# b701146cf2c1262a6385c8b1fb1db98f05820499

s = hashlib.sha1(b'Hello World.').hexdigest()

print(s.encode('utf-8'))

# b'b701146cf2c1262a6385c8b1fb1db98f05820499'

print(hashlib.sha1(b'hsdhsdefuieia' + bytes(s.encode('utf-8'))).hexdigest())

# 2afb7a7a5787c903ced86ffcbd410442eb153292