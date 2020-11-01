from pymd5 import md5, padding
from urllib import parse, request
# 
# m = "Use HMAC, not hashes"
# h = md5()
# h.update(m.encode())
# print(str(h.hexdigest()))

h1 = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=512)

h = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=512)
m = "Use HMAC, not hashes"

x = "Good advice"
h.update(x.encode())
print(str(h.hexdigest()))

# http://cis551.cis.upenn.edu/project2/api?token=0c6edcc81c7714b37a87cee7bb1f3d89&user=aturing&command1=ListSquirrels&command2=NoOp
orig = "http://cis551.cis.upenn.edu/project2/api?token="
part2 = "&user=aturing&command1=ListSquirrels&command2=NoOp"
part3 = "&command3=UnlockAllSafes"

padString = parse.quote(padding(len(part2)*8))

# print(padding(len(part2)*8))
token = "0c6edcc81c7714b37a87cee7bb1f3d89"
token_h = md5(state=bytes.fromhex(token) + padding(len(part2)*8), count=512)
token_h.update("&command3=UnlockAllSafes".encode())
print(str(token_h.hexdigest()))

print(parse.quote(padding(len(part2)*8)))


# padString = str(padding(len(part2)*8)).replace("\\", "")
# padString = padString.replace("x", "%")

# padString = padString[2: len(padString) - 1]
# print(padString)
# print(padding(len(part2)*8).encode())

# newString = orig + str(token_h.hexdigest()) +  part2 + padString + part3
newString = orig + "0c6edcc81c7714b37a87cee7bb1f3d89" +  part2 + padString + part3

print(newString)


# extendedHash = m + padding(len(m)*8) + x
