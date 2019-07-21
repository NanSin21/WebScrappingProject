#!C:\Users\PC-2\AppData\Local\Programs\Python\Python36-32\python.exe
import cgi,cgitb

form = cgi.FieldStorage()
f= form.getvalue('fname')
l= form.getvalue('lname')

print('Content-type: text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Your page</title>')
print('</head>')
print('<body style="background-color:yellow">')
print('<h2>Welcome %s %s</h2>' % (f,l))
print('<br><br><form action="webscrap1.py" method="get">')
print("Give link for web scrapping: ")
print('<input type="text" name="httpstr" minlength="15">')
print('<br><input type="submit" name="Send">')
print('</form>')
print('</body>')
print('</html>')

