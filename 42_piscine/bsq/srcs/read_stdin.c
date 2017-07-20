/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   read_stdin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/19 11:24:07 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 12:04:32 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

char	*read_stdin(void)
{
	char	buffer[1];
	char	*map_str;
	int		ret;
	int		fd;
	int		i;

	i = 0;
	fd = open("map", O_WRONLY);
	while ((ret = read(STDIN_FILENO, buffer, 1)))
	{
		buffer[ret] = '\0';
		write(fd, buffer, 1);
		i++;
	}
	close(fd);
	if (ret == -1)
	{
		write(2, "Unable to read stdin\n", 21);
		return (0);
	}
	fd = open("map", O_RDONLY);
	map_str = (char *)malloc(sizeof(char) * (i + 1));
	read(fd, map_str, i);
	close(fd);
	return (map_str);
}
