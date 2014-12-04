#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html"
print

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"

bill=[]
# item = a list that contains the checked items of catalogue.html 
# with inventory.csv and if they match adds them to the bill 


def add_to_list(item):
  bill.append(item)
  
def show_bill():
  print "<h2>Here's the bill.</h2>"
  for item in bill:
    print(item)
  
show_bill()
