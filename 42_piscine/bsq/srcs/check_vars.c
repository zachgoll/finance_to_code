/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_vars.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 07:23:13 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/18 12:25:17 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		check_vars(char *map, int position)
{
	char	empty;
	char	obstacle;
	char	full;
	int		i;

	i = position;
	empty = map[i++];
	obstacle = map[i++];
	full = map[i++];
	if (empty == obstacle || empty == full || obstacle == full)
		return (0);
	while (map[i] == ' ' || map[i] == '\t')
		i++;
	if (map[i] != '\n')
		return (0);
	while (map[i] != '\0')
	{
		if (map[i] != empty && map[i] != obstacle && map[i] != '\n')
			return (0);
		i++;
	}
	return (1);
}
