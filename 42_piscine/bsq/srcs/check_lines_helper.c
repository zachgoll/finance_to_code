/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_lines_helper.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 10:37:47 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 10:45:36 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		check_lines_helper(char *map, int i, int map_start)
{
	int flag;
	int counter;

	flag = 0;
	counter = 0;
	while (map[i] != '\n')
	{
		i++;
		counter++;
	}
	flag = counter;
	i = map_start;
	while (map[i] != '\0')
	{
		counter = 0;
		while (map[i] != '\n')
		{
			i++;
			counter++;
		}
		if (flag != counter)
			return (0);
		i++;
	}
	return (1);
}
