import sys, subprocess

num = 1000
print "Realizando  conexiones simultaneas"
host = "ping -c1 ugraerospaceprogram.appspot.com"

for i in range(num):
    p = subprocess.Popen(host, shell=True, stderr=subprocess.PIPE)
    
    while True:
        out = p.stderr.read(1)
        
        if out == '' and p.poll()!= None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
    
    
print "Test finalizado"
