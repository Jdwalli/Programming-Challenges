#include <stdio.h>

int main()
{
    unsigned long int total = 0;

    for (int i = 1; i < 1000; i++)
    {

        if (i % 5 == 0 || i % 3 == 0)
        {
            total = total + i;
        }
        else
        {
            total = total + 0;
        }
    }

    printf("%lu \n", total);

    return 0;
}