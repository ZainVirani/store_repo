#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char data[4096];
char *useless;
int quantity[9];
int item=0;

void getfields(char* line){
	char *token;
	token = strtok(line, ",");
	useless = token;
	token = strtok(NULL, ",");
	quantity[item] = token;
}
int main(){
	char inputs[8192];
	char *inputU;
	char *username;
	char c;
	int a=0;
	printf("Content-type: text/html\n\n");
	printf("<html>");
	int n = atoi(getenv("CONTENT_LENGTH"));
	while((c=getchar())!=EOF && a<n){ //read hidden username
		if(a<8192){
			if(c!='+') inputs[a]=c;
			else inputs[a]=' ';
			a++;
		}
	}
	inputs[a]='\0';
	if(inputs!=NULL){ //read username
		char *token;
                token = strtok(inputs, "=");
                token = strtok(NULL, "&");
                inputU = token;
	}
	FILE* fileR = fopen("Inventory.csv", "r");
	fgets(data, 4096, fileR);
	while(!feof(fileR)){ //while end of file has not been reached
		fgets(data, 4096, fileR); //read line
		if(feof(fileR)) break; //if file is end of file, break while loop
		char *tmp = strdup(data);
		getfields(tmp);
		item++;
	}
	fclose(fileR); //close file
	printf("<body onload=\"submitForm()\">");
	printf("<form action = \"catalogue.html\" method = \"get\" name=\"myForm\" id=\"myForm\">");
	printf("<input id=\"quantity1\" type = \"hidden\" name = \"quantity1\" value = \"%d\">", quantity[0]);
	printf("<input id=\"quantity2\" type = \"hidden\" name = \"quantity2\" value = \"%d\">", quantity[1]);
	printf("<input id=\"quantity3\" type = \"hidden\" name = \"quantity3\" value = \"%d\">", quantity[2]);
	printf("<input id=\"quantity4\" type = \"hidden\" name = \"quantity4\" value = \"%d\">", quantity[3]);
	printf("<input id=\"quantity5\" type = \"hidden\" name = \"quantity5\" value = \"%d\">", quantity[4]);
	printf("<input id=\"quantity6\" type = \"hidden\" name = \"quantity6\" value = \"%d\">", quantity[5]);
	printf("<input id=\"quantity7\" type = \"hidden\" name = \"quantity7\" value = \"%d\">", quantity[6]);
	printf("<input id=\"quantity8\" type = \"hidden\" name = \"quantity8\" value = \"%d\">", quantity[7]);
	printf("<input id=\"quantity9\" type = \"hidden\" name = \"quantity9\" value = \"%d\">", quantity[8]);
	printf("<input id=\"username\" type = \"hidden\" name = \"username\" value = \"%s\">", inputU);
	printf("</form>");
	printf("<script type='text/javascript'>document.myForm.submit();</script>");
	printf("</body>");
	printf("</head>");
}


