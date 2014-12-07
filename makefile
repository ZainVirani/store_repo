login.cgi : login.o
	gcc -o login.cgi login.o
	chmod a+rx login.cgi
	chmod a+rx *.html
	chmod a+rx *.pl
	chmod a+rx *.py
login.o : login.c
	gcc -c login.c
clean : 
	rm -f login.o
