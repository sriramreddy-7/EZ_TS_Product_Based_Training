#include<stdio.h>
int main()
{
int r,c;
scanf("%d",&r);
scanf("%d",&c);
int m[r][c],i,j,n[r][c];
for(i=0;i<r;i++)
{
    for(j=0;j<c;j++)
    {
        printf("Enter the Element: \n");
        scanf("%d",&m[i][j]);
    }
}
for(i=0;i<r;i++)
{
    for(j=0;j<c;j++)
    {
        printf("\t%d",m[i][j]);
    }
    printf("\n");
}
int temp=0;
for(i=0;i<r;i++)
{
    for(j=0;j<c;j++)
    {
       n[i][j]=m[j][i];
    }
    printf("\n");
}
for(i=0;i<r;i++)
{
    for(j=0;j<c;j++)
    {
       printf("\t%d",n[i][j]);
    }
    printf("\n");
}
printf("\n");
int k[r][c];
for(i=r-1;i>=0;i--)
{
    for(j=c-1;j>=0;j--)
    {
        printf("\t%d",n[j][i]);
        k[j][i]=n[i][j];
    }
    printf("\n");
}
printf("kkkkk");
for(i=r-1;i>=0;i--)
{
    for(j=c-1;j>=0;j--)
    {
        printf("\t%d",k[j][i]);
    }
    printf("\n");
}
return 0;
}