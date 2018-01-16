#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '</body>'
print '</html>'





# Collect values from form
inputs = cgi.FieldStorage()
fill = {}
for key in inputs:
   fill[key] = inputs[key].value

# If the form was completed, save what was entered on it
try:
     said = fill["info"]
     form = 1
     db.query('insert into comment (info) values ("' \
               +said.replace('"',r'\"') \
               +'")')
except:
     form = 0
=============================================
#!/usr/bin/python

import sqlite3
import cgitb
import db
cgitb.enable()


i = 20

conn = sqlite3.connect("pragsale.db")
with conn:
    c = conn.cursor()
    c.execute("Select Count(*) From Tbl_Flats")

print "Content-type:text/html\r\n\r\n"
print "<html><head><title>Hello Word - First CGI Program</title></head><body><h2>The number of records is : </h2>"

print "<li>"
print(c.fetchone())
print "</li>"

for row in c.execute("SELECT * FROM Tbl_Flats"):
        print(row)

print "<h2> Thats it. </h2></body></html>"

conn.close()
