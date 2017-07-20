/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_helper.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 11:07:25 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 12:05:58 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	main_helper(char *map)
{
	int		**map_matrix;
	char	*symbols;
	int		dimensions[2];

	dimensions[0] = get_map_height(map);
	dimensions[1] = get_map_width(map);
	get_characters(&symbols, map);
	make_matrix(&map_matrix, map, dimensions[0], dimensions[1]);
	find_largest_square(symbols, map_matrix, dimensions[0], dimensions[1]);
	free(map_matrix);
}
