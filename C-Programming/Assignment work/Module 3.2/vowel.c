#include<stdio.h>
void main()
{
	char chara;
	printf("Enter a Character : ");
	scanf("%c",&chara);
	
	switch (chara)
{
	case 'A':
	case 'E':
	case 'I':
	case 'O':
	case 'U':
	case 'a':
	case 'e':
	case 'i':
	case 'o':
	case 'u':
	printf("\n%c is a Vowel",chara);
	
	break;
	
	
	
	default:("\n is Consonant");
	break;
	
	
	}	
	
}