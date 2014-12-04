#!/usr/bin/python
print "Content-Type: text/html"
print

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"

import cgitb
cgitb.enable()


bill=[]

print("Please input the product numbers you wish to purchase")

def add_to_list(item):
  bill.append(item)
  print("Added! List has {} items.".format(len(bill)))
  
def show_list():
  print("Here's your list")
  for item in bill:
    print(item)
    
while True:
  new_item = input("> ")
  if new_item == 'DONE':
    break
  elif new_item == 'SHOW':
    show_list()
    continue
  
  add_to_list(new_item)
  continue 
  
show_list()
