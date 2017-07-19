/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/06 11:15:19 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/06 23:39:30 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		*ft_range(int min, int max)
{
	int *int_array;
	int i;
	int size;

	if (max - min <= 0)
	{
		int_array = 0;
		return (int_array);
	}
	size = max - min;
	i = 0;
	int_array = (int *)malloc(sizeof(int) * size);
	while (i < size)
	{
		int_array[i] = min;
		min++;
		i++;
	}
	return (int_array);
}
