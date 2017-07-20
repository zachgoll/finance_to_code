/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   find_largest_square.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 21:07:13 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:54:22 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	find_largest_square(char *symbols, int **map_matrix,
		int height, int width)
{
	int n[7];

	n[0] = height;
	n[1] = width;
	n[2] = 0;
	n[3] = 0;
	n[4] = 0;
	n[5] = -1;
	n[6] = 0;
	find_s(symbols, map_matrix, n);
}
