#include <stdio.h>

int main()
{

//get input
printf( "Enter a string: " );
char s[255];
scanf( "%[^\n]s" , s );

//print output
printf( "'%s' converted to binary is: " , s );

//for each character, print it's binary aoutput
int i,c,power;

for( i=0 ; s[i]!='\0' ; i++ )
{
//c holds the character being converted
c = s[i];

//for each binary value below 256 (because ascii values < 256)
for( power=7 ; power+1 ; power-- )
//if c is greater than or equal to it, it is a 1
if( c >= (1<<power) )
{
c -= (1<<power); //subtract that binary value
printf("1");
}
//otherwise, it is a zero
else
printf("0");
}


return 0;
}
