/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_solution.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 21:08:18 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:55:21 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	print_solution(char *symbols, int **map_matrix, int nums[7])
{
	int i;
	int j;

	i = 0;
	j = 0;
	while (i < nums[0])
	{
		while (j < nums[1])
		{
			if (i <= nums[2] && i >= (nums[2] - nums[4] + 1) &&
				j <= nums[3] && j >= (nums[3] - nums[4] + 1))
				ft_putchar(symbols[2]);
			else if (map_matrix[i][j] == 0)
				ft_putchar(symbols[1]);
			else
				ft_putchar(symbols[0]);
			j++;
		}
		ft_putchar('\n');
		j = 0;
		i++;
	}
}
