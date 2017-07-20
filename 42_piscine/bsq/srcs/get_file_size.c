/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_size.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/17 10:35:34 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/17 11:29:09 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_bsq.h"

int		get_file_size(char *file_str)
{
	char	buffer[1];
	int		i;
	int		fd;
	int		ret;

	i = 0;
	fd = open(file_str, O_RDONLY);
	if (fd == -1)
	{
		write(2, "Unable to open file.\n", 22);
		return (1);
	}
	while ((ret = read(fd, buffer, 1)))
	{
		buffer[ret] = '\0';
		i++;
	}
	if (close(fd) == -1)
	{
		write(2, "Unable to close file.\n", 23);
		return (1);
	}
	return (i);
}
