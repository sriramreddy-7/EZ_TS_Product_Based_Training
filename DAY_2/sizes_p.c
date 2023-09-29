#include<stdio.h>
struct a
{
    int x;
    char y;
    double z;
};
/*struct a
{
    double x;
    char y;
    int z;
};*/
/*struct a
{
    int x;
    int y;
    char z;
};*/
/*struct a
{
    char x;
    int y;
    int z;
};*/
/*struct a
{
    char x;
    double y;
    double z;
};*/
/*struct a
{
    char x;
    double y;
    int z;
};*/
/*struct a
{
     // Size is 16
    char x;
    int y; 
    double z;
};*/
/*struct a
{
    int x; // Size 24
    double y;
    char z;
};*/
int main()
{
    struct a yes;
    printf("%d",sizeof(yes));
    return 0;
}