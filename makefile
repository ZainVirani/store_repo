login : login.o
	gcc -o login login.o
login.o : login.c clean
	gcc -c login.c
clean : 
	rm -f login.o
