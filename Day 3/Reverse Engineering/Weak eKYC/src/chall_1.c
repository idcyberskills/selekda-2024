#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdint.h>
#include <unistd.h>


int main(int argc, char const *argv[])
{
	char input[14];
	char id[25];
	int username[] = {87, 83, 65, 95, 99, 97, 110, 100, 105, 100, 52, 116, 101};
	int password[] = {117, 94, 66, 75, 94, 117, 66, 30, 14, 117, 77, 26, 26, 78, 117, 88, 79, 117, 89, 65, 27, 102, 102, 89};
	puts("~ ( ' 0 ' ) ~ I'll accompany you as a royal servant -aseng");
	puts("Welcome to SELEKDA! You have made it to Reverse Engineering Challenge. Please enter your username!");
	scanf("%13s",input);
	input[14] = '\0';
	for(int i=0; i < 14; i++){
		if(input[i] != username[i]) {
			puts("Are you sure? You are not registered here.");
			exit(-1);
		}
	}
	puts("You need to wait for approximately 1 hour to be validated. Please stay still .");
	sleep(3600);
	puts("You're validated! Now we're moving to the next identification verification. Please answer the following security question:");
	puts("Continue this statement with rhymes, I want to attend to Worldskills. I'm the person (fill this....) ");
	scanf("%24s", id);
	id[25] = '\0';
	memfrob(id, 24);
	for(int j=0; j < 24; j++){
		if(id[j] != password[j]){
			puts("Can you at least break me to any point that you could think of?");
			exit(-1);
		}
	}
	memfrob(id, 24);
	printf("Thank you for the verification. Here take your bags and Username card, you're now -> SELEKDA{%s",input);
	for(int k=0; k < 24;k++){
		printf("%c",id[k]);
	}
	printf("}");
	return 0;
}