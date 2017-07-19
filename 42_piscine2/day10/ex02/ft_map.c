/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 06:59:18 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/11 07:17:59 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		simple_func(int n)
{
	return (n * 10);
}

int		*ft_map(int *tab, int length, int (*f)(int))
{
	int *num_array;
	int i;

	num_array = (int *)malloc(sizeof(int) * length);
	i = 0;
	while (i < length)
	{
		num_array[i] = f(tab[i]);
		i++;
	}
	return (num_array);
}
