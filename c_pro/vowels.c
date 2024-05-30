#include<stdio.h>
int main(){
	char ch;
	printf("Enter any alphabet: ");
	scanf("%c", &ch);
	if(ch=='a'||ch=='A'){
		printf("Entered alphabet is a vowel.");
	}
	else if(ch=='e'||ch=='E'){
		printf("Entered alphabet is a vowel.");
	}
	else if(ch=='i'||ch=='I'){
		printf("Entered alphabet is a vowel.");
	}		
	else if(ch=='o'||ch=='O'){
			printf("Entered number is a vowel.");
		}
	else if(ch=='u'||ch=='U'){
			printf("Entered alphabet is a vowel.");
		}
	else{
		printf("Entered alphabet is a consonant");
	}
	return 0;
}
