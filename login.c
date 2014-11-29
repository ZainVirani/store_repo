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
	char inputUser[4096]={'\0'};
	char inputPass[4096]={'\0'};
	char *inputU;
	char *inputP;
	int found = 0;
	printf("Enter your username: ");
	gets(inputUser);
	printf("Enter your password: ");
	gets(inputPass);
	inputU=inputUser;
	inputP=inputPass;
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
		printf("Username or password is incorrect.\n");
		exit;
	}
	else{
		if(strcmp(inputP, password)==0){
			printf("Login successful! Welcome, %s!\n", name);
		}
		else{
			printf("Username or password is incorrect.\n");
			exit;
		}
	}		
}


