#include <omp.h>
#include <stdio.h>

int main()
{

int i;
int n=10;
float a[n];
float b[n];

for (i = 0; i < n; i++)
    a[i] = i;

#pragma omp parallel for
/* i is private by default */
for (i = 1; i < n; i++)
    {
     b[i] = (a[i] + a[i-1]) / 2.0;
    }

for (i = 1; i < n; i++)
    printf("%f ", b[i]);
printf("\n");
}
