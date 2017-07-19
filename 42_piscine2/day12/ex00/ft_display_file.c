/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/12 15:23:19 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:25:24 by zgollwit         ###   ########.fr       */
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
	{
		write(2, "Invalid argument.\n", 19);
		return (1);
	}
	while ((ret = read(fd, buf, 1)))
	{
		buf[ret] = '\0';
		write(1, buf, 1);
	}
	if (close(fd) == -1)
	{
		write(2, "Unable to close file.\n", 23);
		return (1);
	}
	return (0);
}

int		main(int argc, char **argv)
{
	if (argc == 1)
	{
		write(2, "File name missing.\n", 20);
		return (1);
	}
	if (argc > 2)
	{
		write(2, "Too many arguments.\n", 21);
		return (1);
	}
	ft_display_file(argv[1]);
	return (0);
}
