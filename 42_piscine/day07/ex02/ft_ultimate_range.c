/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/06 14:12:47 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/06 23:13:22 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		ft_ultimate_range(int **range, int min, int max)
{
	int *int_array;
	int i;
	int size;

	size = max - min;
	if (size <= 0)
	{
		*range = 0;
		return (0);
	}
	int_array = (int *)malloc(sizeof(int) * size);
	if (int_array == NULL)
		return (0);
	i = 0;
	while (i < size)
	{
		int_array[i] = min;
		min++;
		i++;
	}
	*range = int_array;
	return ((i - 1) * sizeof(int));
}
