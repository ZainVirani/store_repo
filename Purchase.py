#!/usr/bin/python
import re
import cgi

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage() # parse query
	#if form.has_key("firstname") and form["firstname"].value != "":
	#		print "<h1>Hello", form["firstname"].value, "</h1>"
	#else:
	#	print "<h1>Error! Please enter first name.</h1>"
	
	inventory = []
	one_order = form.getvalue("one")
	five_order = form.getvalue("five")
	ten_order = form.getvalue("ten")
	twenty_order = form.getvalue("twenty")
	content = ""

	if form.has_key("loggedin"):
		print asdfasdf


	with open ('../database/Inventory.scv', 'r') as f:	
		for line in f:
			line = (line.split(","))
			inventory.append(int(line[1]))

		if ((inventory[0]-int(one_order))>=0)and((inventory[1]-int(five_order))>=0)and((inventory[2]-int(ten_order))>=0)and((inventory[3]-int(twenty_order))>=0):
			line1 ='one,'+str(inventory[0]-int(one_order))+',1\n'
			line2 = 'five,'+str(inventory[1]-int(five_order))+',5\n'
			line3 = 'ten,'+str(inventory[2]-int(ten_order))+',10\n'
			line4 = 'twenty,'+str(inventory[3]-int(ten_order))+',20\n'

			content = line1+line2+line3+line4
			#print content
			with open ('../database/Inventory.scv', 'w') as wf:
				wf.write(content)
			wf.close
			print "<html>"
			print"	<head><title>Monopoly - Bill</title></head>"
			print "	<body>"
			print "  <p>"
			print "  <b>BILL</b><br>"
			if form.has_key("loggedin"):
		                print "asdfasdf"
			print "  ============================<br>"
			print "	 One Monpoly Dollar * " + str(one_order) + "  = $" + str(1*(int(one_order))) + "<br>"
			print "  Five Monopoly Dollars * " + str(five_order) + " = $" + str(5*(int(five_order)))+ "<br>"
			print "  Ten Monopoly Dollars * " + str(ten_order) + " = $" + str(10*(int(ten_order))) + "<br>"
			print "  Twenty Monopoly Dollars * " + str(twenty_order) + " = $" + str(20*(int(twenty_order))) + "<br>"
			print "  ============================<br>"
			print "  <b>TOTAL : $" + str((1*(int(one_order)))+(5*(int(five_order)))+(10*(int(ten_order)))+(20*(int(twenty_order))))+ " CND</b><br>" 
			print "  THANK YOU FOR YOUR PURCHASE"
			print "  </p>"
			print "  To go back to Home page : " + '<a href="http://cs.mcgill.ca/~jlee299/index.html">Home</a><br>'
			print "  To go back to Catalogue page : " + '<a href="http://cs.mcgill.ca/~jlee299/index.html">Catalogue</a>'
			print " </body>"
			print "</html>"
		else:
			print "Sorry! Out of inventory."
	f.close()
main()
