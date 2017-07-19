/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/12 15:23:19 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/13 18:56:12 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_cat.h"

int		ft_display_file(char *file_name)
{
	int		fd;
	int		ret;
	char	buf[1];

	fd = open(file_name, O_RDONLY);
	if (fd == -1)
		return (errno);
	while ((ret = read(fd, buf, 1)))
	{
		buf[ret] = '\0';
		write(1, buf, 1);
	}
	if (close(fd) == -1)
		return (errno);
	return (0);
}

int		main(int argc, char **argv)
{
	int i;

	i = 1;
	if (argc == 1)
	{
		write(2, "File name missing.\n", 20);
		return (1);
	}
	while (i < argc)
	{
		ft_display_file(argv[i]);
		i++;
	}
	return (0);
}
