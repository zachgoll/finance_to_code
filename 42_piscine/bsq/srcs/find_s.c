/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   largest_square.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 09:07:48 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:54:41 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	find_s(char *symbols, int **map_matrix, int n[7])
{
	int		copy[n[0]][n[1]];

	while (++n[5] < n[0])
	{
		while (n[6] < n[1])
		{
			if (n[5] == 0 || n[6] == 0)
				copy[n[5]][n[6]] = map_matrix[n[5]][n[6]];
			else if (map_matrix[n[5]][n[6]] == 1)
				copy[n[5]][n[6]] = (get_min(copy[n[5] - 1][n[6] - 1],
									copy[n[5] - 1][n[6]],
									copy[n[5]][n[6] - 1]) + 1);
			else
				copy[n[5]][n[6]] = 0;
			if (copy[n[5]][n[6]] > n[4])
			{
				n[2] = n[5];
				n[3] = n[6];
				n[4] = copy[n[5]][n[6]];
			}
			n[6]++;
		}
		n[6] = 0;
	}
	print_solution(symbols, map_matrix, n);
}
