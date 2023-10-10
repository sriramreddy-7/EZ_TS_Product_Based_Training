#include<stdio.h>
int i,j,r,c;
void gms(int a[],int n)
{
int max=9,min=1;
int m[r][c];
for(i=1;i<=r;i++)
{
    for(j=1;j<=c;j++)
    {
        if((i/2)==(max/2) && (j/2)==(max/2))
        {
            m[i][j]=i;
        }
    }

}
}
void main()
{
    scanf("%d",&r);
    scanf("%d",&c);
    int a[r][c];
    for (i=0;i<=r;i++)
    {
        for(j=0;j<=c;j++)
        {
            scanf("%d",&a[i][j]);
        }
       
    }
    //gms(a,r,c);
}