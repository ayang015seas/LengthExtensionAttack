from pymd5 import md5, padding
from urllib import parse, request

m = "Use HMAC, not hashes"
h = md5()
h.update(m.encode())
print(str(h.hexdigest()))

h = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=512)

pad = parse.quote(padding(len(m)*8))
padHex = padding(len(m)*8).hex()

h1 = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d") + padding(len(m)*8), count=512)

x = "Good advice"
h.update(x.encode())
h1.update(x.encode())

print(str(h.hexdigest()))
print(str(h1.hexdigest()))