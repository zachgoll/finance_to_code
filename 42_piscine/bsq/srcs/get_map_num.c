/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_map_num.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 09:36:38 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:09:15 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		get_map_num(char *map)
{
	int		i;
	char	*map_number;

	i = 0;
	map_number = (char*)malloc(sizeof(char) * skip_lines(map));
	while (map[i] >= '0' && map[i] <= '9')
	{
		map_number[i] = map[i];
		i++;
	}
	map_number[i] = '\0';
	i = ft_atoi(map_number);
	free(map_number);
	return (i);
}
