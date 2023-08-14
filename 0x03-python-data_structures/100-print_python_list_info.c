#include <stdio.h>

unsigned long long factorial(unsigned int n) 
{
    if (n == 0 || n == 1) 
    {
        return 1;
    } 
    else 
    {
        return n * factorial(n - 1);
    }
}

int main() 
{
    unsigned int num;
    
    printf("Enter a positive integer: ");
    scanf("%u", &num);
    
    if (num < 0) 
    {
        printf("Factorial is not defined for negative numbers.\n");
    } 
    else 
    {
        unsigned long long result = factorial(num);
        printf("Factorial of %u is %llu\n", num, result);
    }
    
    return 0;
}
