import sys
import ctypes
import struct

a = 5
b = 125.54
c = 'Hello World!'

print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))

# 1734408176
# 14
# b'\x1c\x00\x00\x00(\x91_g\x01\x00\x00\x00\x05\x00'

