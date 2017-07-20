/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   make_matrix.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 10:01:46 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 07:49:34 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	make_matrix(int ***map_matrix, char *map, int height, int width)
{
	int		**map_m;
	int		i;
	int		row;
	int		column;

	i = 0;
	row = 0;
	column = 0;
	map_m = (int **)malloc(sizeof(int*) * height);
	while (map[i] != '\n' && map[i] != '\0')
		i++;
	while (map[++i] != '\0')
	{
		map_m[row] = (int *)malloc(sizeof(int) * (width + 1));
		while (map[i] != '\n')
		{
			map_m[row][column] = convert_char(map, map[i]);
			column++;
			i++;
		}
		column = 0;
		row++;
	}
	*map_matrix = map_m;
}
