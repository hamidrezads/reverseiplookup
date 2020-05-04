import requests
target = raw_input("Enter Domain/IP: ")
u = "https://api.hackertarget.com/reverseiplookup/?q=" + target
r = requests.get(u)
res = r.content
res = res.split("\n")
print str(len(res)) + " domains were found!"
for i in res:
    print i