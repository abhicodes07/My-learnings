#include <stdio.h>
// This is function definition
void struct_func(char str[]){
	struct str{ 
		int Id;
		char name[50];
		int class;
		int eng_marks;
		int math_marks;
		int sci_marks;
		int com_marks;
		int py_marks;
		int total;
		int percentage;
	};
	
	int no_std;
	printf("Enter the number of students: ");
	scanf("%d", &no_std); 
	struct str std[no_std];
	for(int i=0; i<no_std; i++){
		printf("Enter the student ID: ");
		scanf("%d", &std[i].Id);
		printf("Enter the name of the student: ");
		scanf("%s", std[i].name);
		printf("Enter the class of the student: ");
		scanf("%d", &std[i].class);
		printf("Enter the English marks: ");
		scanf("%d",&std[i].eng_marks);
		printf("Enter the Maths marks: ");
		scanf("%d",&std[i].math_marks);
		printf("Enter the Science marks: ");
		scanf("%d",&std[i].sci_marks);
		printf("Enter the computer marks: ");
		scanf("%d",&std[i].com_marks);
		printf("Enter the Python marks: ");
		scanf("%d",&std[i].py_marks);
	}
	printf("\n\tINFORMATION OF THE STUDENTS\n");
	// PRINTING THE INFORMATION
	for(int j=0;j<no_std;j++){
		printf("\tStudent Name = %s\n\tStudent ID = %d\n\tClass = %d\n\tEnglish Marks = %d\n\tMaths Marks = %d\n\tScience Marks= %d\n\tComputer Marks = %d\n\tPython Marks = %d\n",std[j].name,std[j].Id,std[j].class,std[j].eng_marks,std[j].math_marks,std[j].sci_marks,std[j].com_marks,std[j].py_marks);
	 // PRITNING TOTAL & PERCENTAGE
		printf("\tTotal marks: %d\n", std[j].total = std[j].eng_marks+std[j].math_marks+std[j].sci_marks+std[j].com_marks+std[j].py_marks);	 
		printf("\tTotal percentage: %d\n", std[j].percentage = std[j].total%5);
	}
}

int main(){
	char structure_name[50];
	printf("Enter the structure name: ");
	scanf("%s", structure_name);
	printf("\n");
	struct_func(structure_name);
	return 0;
}
