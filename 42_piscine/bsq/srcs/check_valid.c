/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_valid.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 07:21:14 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:21:39 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		check_valid(char *map)
{
	int		i;
	int		size_temp;
	int		width;
	int		height;

	width = get_map_width(map);
	height = get_map_height(map);
	i = 0;
	if (map)
	{
		if (map[i] >= '0' && map[i] <= '9')
		{
			size_temp = get_map_num(map);
			i = skip_num(map);
			if (size_temp < 1 || size_temp != height
				|| check_vars(map, i) == 0)
				return (0);
			if (check_map_lines(map, i) == 0)
				return (0);
			return (1);
		}
		return (0);
	}
	else
		return (0);
}
