/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_character.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/18 19:58:01 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 06:49:17 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	get_characters(char **symbols, char *map)
{
	char	*char_str;
	int		i;

	i = 0;
	char_str = (char *)malloc(sizeof(char) * 4);
	while (map[i] >= '0' && map[i] <= '9')
		i++;
	char_str[0] = map[i++];
	char_str[1] = map[i++];
	char_str[2] = map[i++];
	char_str[3] = '\0';
	*symbols = char_str;
}
