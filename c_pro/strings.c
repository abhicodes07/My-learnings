#include<stdio.h>
int main(){
	char str[50];
	printf("Enter the string: ");
	scanf("%[^\n]s", str);
	printf("Entered number: %s", str);
	printf("\n");
	return 0;
}
