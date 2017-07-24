#include <stdlib.h>
#include <stdio.h>

void	swap(float *x, float *y)
{
	float temp = *x;
	*x = *y;
	*y = temp;
}

float	mean(float *numbers, int n)
{
	float mean = 0;
		
	for (int i = 0; i < n; i++)
		mean += numbers[i];

	return (mean / n);
}

float	median(float *numbers, int n)
{
	float temp = 0;

	if (n % 2 == 1)
		return (numbers[n / 2]);
	else
	{
		temp = numbers[n / 2 - 1];
		temp = (temp + numbers[n / 2]) / 2;
		return (temp);
	}
}

float	mode(float *numbers, int n)
{
	int current = 0;
	int count = 0;
	float mode = numbers[0];

	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (numbers[i] == numbers[j])
				count++;
		}
		if (count > current)
		{
			current = count;
			mode = numbers[i];
		}
		count = 0;
	}
	
	return (mode);
}


int		main()
{
	float	n;
	float	*numbers;
	int		i;

	i = 0;
	scanf("%f", &n);
	numbers = (float*)malloc(sizeof(float)*(n + 1));
	
	while (i < n && scanf("%f", &numbers[i++]) == 1);	
	
	for (int k = 0; k < n - 1; k++)
	{
		for (int z = 0; z < n - k - 1; z++)
		{	
			if (numbers[z] > numbers[z+1])
				swap(&numbers[z], &numbers[z+1]);
		}
	}
	
	
	printf("%.1f\n", mean(numbers, n));
	printf("%.1f\n", median(numbers, n));
	printf("%.0f\n", mode(numbers, n));
	
	return (0);
}
