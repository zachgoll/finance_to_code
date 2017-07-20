/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_map_lines.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 11:39:22 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 21:59:47 by rvelez           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		check_map_lines(char *map, int position)
{
	int i;
	int map_start;

	i = position + 4;
	map_start = i;
	i = map_start;
	if (check_lines_helper(map, i, map_start) == 0)
		return (0);
	else
		return (1);
}
