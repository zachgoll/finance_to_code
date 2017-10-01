#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int *array;
	size_t used;
	size_t size;
} 		Array;

void	initArray(Array *a, size_t initialSize)
{
	a->array = (int*)malloc(initialSize*sizeof(int));
	a->used = 0;
	a->size = initialSize;
}

void	insertArray(Array *a, int element)
{
	if (a->used == a->size)
	{
		a->size *= 2;
		a->array = (int*)realloc(a->array, a->size*sizeof(int));
	}
	a->array[a->used++] = element;
}

void	freeArray(Array *a)
{
	free(a->array);
	a->array = NULL;
	a->used = 0;
	a->size = 0;
}

int 	main(void)
{
	Array a;
	int   i;

	initArray(&a, 5);

	for(i = 0; i < 100; i++)
		insertArray(&a, i);

	printf("10th element: %d\nUsed: %zu\n", a.array[9], a.used);

	freeArray(&a);
}
