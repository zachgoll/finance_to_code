/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stdin_helper.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 20:15:46 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 20:52:32 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

void	stdin_helper(void)
{
	char *map_str;

	map_str = read_stdin();
	if (check_valid(map_str) == 1)
		main_helper(map_str);
	else
		write(2, "map error", 10);
	free(map_str);
}
