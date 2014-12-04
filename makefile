login.cgi : login.o catalogue.cgi
	gcc -o login.cgi login.o
	chmod a+rx login.cgi
catalogue.cgi : catalogue.o
	gcc -o catalogue.cgi catalogue.o
	chmod a+rx catalogue.cgi
login.o : login.c
	gcc -c login.c
catalogue.o : catalogue.c
	gcc -c catalogue.c
clean : 
	rm -f login.o
	rm -f catalogue.o
