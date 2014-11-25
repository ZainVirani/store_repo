#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
	FILE* fileR = fopen("Members.csv", "r");
	char username[1025];
	while(!feof(fileR)){ //while end of file has not been reached
		fgets(username, 1024, fileR); //read line
		if(feof(fileR)) break; //if file is end of file, break while loop
		
	}
	fclose(fileR); //close file

}


