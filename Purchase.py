#!/usr/bin/python
import re
import cgi
import csv

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage()
	if form.has_key("username") and form["username"].value != "":
			print "<h1>Hello", form["username"].value, "</h1>"
	else:
		print "<h1>Error! Please enter first name.</h1>"
		
	baby, firm, funny, ganja, huh, pointer, rasta, skeptic, wave = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	
	
	inventory = []
	if form.getvalue("baby") = "on":
		baby = form.getvalue("bbaby")
	if form.getvalue("firm") = "on":
		firm = form.getvalue("bfirm")
	if form.getvalue("funny") = "on":
		funny = form.getvalue("bfunny")
	if form.getvalue("ganja") = "on":
		ganja = form.getvalue("bganja")
	if form.getvalue("huh") = "on":
		huh = form.getvalue("bhuh")
	if form.getvalue("pointer") = "on":
		pointer = form.getvalue("bpointer")
	if form.getvalue("rasta") = "on":
		rasta = form.getvalue("brasta")
	if form.getvalue("skeptic") = "on":
		skeptic = form.getvalue("bskeptic")
	if form.getvalue("wave") = "on":
		wave = form.getvalue("bwave")
	content = ""

	if form.has_key("username"):
		print asdfasdf


	with open ('Inventory.csv', 'r') as f:	
		for line in f:
			line = (line.split(","))
			inventory.append(int(line[1]))

		if ((inventory[1]-int(baby))>=0)and((inventory[2]-int(firm))>=0)and((inventory[3]-int(funny))>=0)and((inventory[4]-int(ganja))>=0)and((inventory[5]-int(huh))>=0)and((inventory[6]-int(pointer))>=0)and((inventory[8]-int(skeptic))>=0)and((inventory[9]-int(wave))>=0):
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
			with open ('Inventory.csv', 'w') as wf:
				wf.write(content)
			wf.close
			print "<html>"
			print"	<head><title>Barack Pics - Bill</title></head>"
			print "	<body>"
			print "  <p>"
			print "  <b>BILL</b><br>"
			if form.has_key("loggedin"):
		                print "asdfasdf"
			print "  ============================<br>"
			print "	 B Baby * " + str(baby) + "  = $" + str(20*(int(baby))) + "<br>"
			print "  B Firm * " + str(firm) + " = $" + str(20*(int(firm)))+ "<br>"
			print "	 B Funny * " + str(funny) + "  = $" + str(20*(int(funny))) + "<br>"
			print "  B Herb * " + str(ganja) + " = $" + str(20*(int(ganja)))+ "<br>"
			print "	 B Huh * " + str(huh) + "  = $" + str(20*(int(huh))) + "<br>"
			print "  B Pointed * " + str(pointer) + " = $" + str(20*(int(pointer)))+ "<br>"
			print "	 B Rasta * " + str(rasta) + "  = $" + str(20*(int(rasta))) + "<br>"
			print "  B Skeptic * " + str(skeptic) + " = $" + str(20*(int(skeptic)))+ "<br>"
			print "	 B Wave * " + str(wave) + "  = $" + str(20*(int(wave))) + "<br>"
			print "  ============================<br>"
			print "  <b>TOTAL : $" + str((20*(int(baby)))+(20*(int(firm)))+(20*(int(funny)))+(20*(int(ganja)))+(20*(int(huh)))+(20*(int(pointer)))+(20*(int(rasta)))+(20*(int(skeptic)))+(20*(int(wave))))+ " CND</b><br>" 
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
