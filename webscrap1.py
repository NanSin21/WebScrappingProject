#!C:\Users\PC-2\AppData\Local\Programs\Python\Python36-32\python.exe
import cgi,cgitb
import json
from urllib.request import urlopen

form = cgi.FieldStorage()
str = form.getvalue('httpstr')
print('Content-type: text/html\r\n\r\n')
print('<html>')
print('<body style="background-color:pink">')
print('<h2>%s</h2>'%str)

with urlopen("{}/json?format=json".format(str)) as f:
    s1 = f.read()
    print('<h3>%s</h3>' %s1)


print('</body>')
print('<html>')
