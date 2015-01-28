import so

num = 10000
print "Realizando  conexiones simultaneas"
ping = "ping -c1 ugraerospaceprogram.appspot.com > /dev/null"

for i in range(num):
        p = os.system(ping)

if p == 0:
    return true
else:
    return false
