#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char data[4096];
char *name;
char *username;
char *password;

void getfields(char* line){
	char *token;
	token = strtok(line, ",");
	name = token;
	token = strtok(NULL, ",");
	username = token;
	token = strtok(NULL, ",");	
	password = token;
}
int main(){
	char inputs[8192];
	char *inputU;
	char *inputP;
	char c;
	int a=0;
	int found = 0;
	printf("Content-type: text/html\n\n");
	printf("<html>");
	int n = atoi(getenv("CONTENT_LENGTH"));
	if(n==0){
                printf("<p>Error: no data passed to script.</p>");
                printf("<meta http-equiv=\"refresh\" content=\"0; error.html\">");
                printf("</html>");
        }
	while((c=getchar())!=EOF && a<n){
		if(a<8192){
			if(c!='+') inputs[a]=c;
			else inputs[a]=' ';
			a++;
		}
	}
	inputs[a]='\0';
	if(inputs == NULL){
		printf("<p>Error: no data passed to script.</p>");
		printf("<meta http-equiv=\"refresh\" content=\"0; error.html\">");
		printf("</html>");
	}
	else{
		char *token;
		token = strtok(inputs, "=");
		token = strtok(NULL, "&");
		inputU = token;
		token = strtok(NULL, "=");
		token = strtok(NULL, "&");
		inputP = token;
	}
	FILE* fileR = fopen("Members.csv", "r");
	while(!feof(fileR)){ //while end of file has not been reached
		fgets(data, 4096, fileR); //read line
		if(feof(fileR)) break; //if file is end of file, break while loop
		char *tmp = strdup(data);
		getfields(tmp);
		if(strcmp(inputU, username)==0){
			found = 1;
			break;
		}
	}
	fclose(fileR); //close file
	if(found==0){
		printf("<p>Username or password is incorrect.\n</p>");
		printf("<meta http-equiv=\"refresh\" content=\"0; error.html\">");
		printf("</html>");
	}
	else{
		if(strcmp(inputP, password)==0){
			printf("<p>Login successful! Welcome, %s!\n</p>", name);
			FILE* fileW = fopen("LoggedIn.csv", "a");
			fprintf(fileW, "%s,\n", inputU);
			fclose(fileW);
			printf("<body onload=\"submitForm()\">");
			printf("<form action = \"catalogue.html\" method = \"get\" name=\"myForm\" id=\"myForm\">");
			printf("<input id=\"username\" type = \"hidden\" name = \"username\" value = \"%s\"><br>", inputU);
			printf("</form>");
			printf("<script type='text/javascript'>document.myForm.submit();</script>");
			printf("</body>");
		}
		else{
			printf("<p>Username or password is incorrect.\n</p>");
			printf("<meta http-equiv=\"refresh\" content=\"0; error.html\">");
			printf("</html>");
		}
	}
	printf("</head>");
}


