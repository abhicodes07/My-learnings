#include<stdio.h>
#include<string.h>
int main(){
	char str[50];
	printf("Enter the string: ");
	scanf("%[^\n]s", str);
	printf("You entered: %s\n",str);

	printf("%s\n", &str[10]);	
	// int length = 0;
	// int height = strlen(str);
	
	// while(height > 1){
		// if(str[length])
	// }
	return 0;
}
