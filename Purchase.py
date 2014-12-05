#!/usr/bin/python
import re
import cgi
import csv

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage() # parse query
	#if form.has_key("firstname") and form["firstname"].value != "":
	#		print "<h1>Hello", form["firstname"].value, "</h1>"
	#else:
	#	print "<h1>Error! Please enter first name.</h1>"
	
	inventory = []
	baby = form.getvalue("baby")
	firm = form.getvalue("firm")
	funny = form.getvalue("funny")
	ganja = form.getvalue("ganja")
	huh = form.getvalue("huh")
	pointer = form.getvalue("pointer")
	rasta = form.getvalue("rasta")
	skeptic = form.getvalue("skeptic")
	wave = form.getvalue("wave")
	content = ""

	if form.has_key("loggedin"):
		print asdfasdf


	with open ('Inventory.csv', 'r') as f:	
		for line in f:
			line = (line.split(","))
			inventory.append(int(line[1]))

		if ((inventory[1]-int(baby))>=0)and
		((inventory[2]-int(firm))>=0)and
		((inventory[3]-int(funny))>=0)and
		((inventory[4]-int(ganja))>=0)
		((inventory[5]-int(huh))>=0)and
		((inventory[6]-int(pointer))>=0)and
		((inventory[7]-int(rasta))>=0)and
		((inventory[8]-int(skeptic))>=0)and
		((inventory[9]-int(wave))>=0):
			line1 = 'baby,'+str(inventory[1]-int(baby))+',20\n'
			line2 = 'firm,'+str(inventory[2]-int(firm))+',20\n'
			line3 = 'funny,'+str(inventory[3]-int(funny))+',20\n'
			line4 = 'ganja,'+str(inventory[4]-int(ganja))+',20\n'
			line5 = 'huh,'+str(inventory[5]-int(huh))+',20\n'
			line6 = 'pointer,'+str(inventory[6]-int(pointer))+',20\n'
			line7 = 'rasta,'+str(inventory[7]-int(rasta))+',20\n'
			line8 = 'skeptic,'+str(inventory[8]-int(skeptic))+',20\n'
			line9 = 'wave,'+str(inventory[9]-int(wave))+',20\n'

			content = line1+line2+line3+line4+line5+line6+line7+line8+line9
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
