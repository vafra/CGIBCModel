#!/usr/bin/python

import cgitb
import cgi
import db
cgitb.enable()

inputs = cgi.FieldStorage()
fill = {}
for key in inputs:
    fill[key] = inputs[key].value

db.addNewRec("Tbl_Attribute", fill)

print "Content-type:text/html\r\n\r\n"
print "<html><head><title>Here you can add a new attribute for flats </title></head><body>"
db.getList("Tbl_Attribute")
print "<Form method='post' action = 'flatattributes.cgi'>"
print "<label> Name: </label></label><input type='text' name='name'></input>"
print "<label> Description: </label></label><input type='text' name='description'></input>"
print "<input type='submit' value='submit'></input></div></FORM>"
print "</body></html>"