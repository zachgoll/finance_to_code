/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   convert_char.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 14:00:54 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 07:32:38 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		convert_char(char *map, char c)
{
	char	empty;
	char	obstacle;
	int		i;

	i = 0;
	while (map[i] >= '0' && map[i] <= '9')
		i++;
	empty = map[i++];
	obstacle = map[i++];
	if (c == empty)
		return (1);
	else
		return (0);
}
