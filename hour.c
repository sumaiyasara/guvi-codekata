#include<stdio.h>
void main()
{
int minz,hrz;
scanf("%d",&minz);
hrz=minz/60;
minz=minz%60;
printf("%d %d",hrz,minz);
}
