/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_concat_params.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/06 16:27:07 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/06 23:31:30 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		get_size(int argc, char **argv);
int		ft_strlen(char *str);
char	*concat(char *str, int length, int argc, char **argv);

char	*ft_concat_params(int argc, char **argv)
{
	int		length;
	char	*storage;

	length = get_size(argc, argv);
	storage = (char *)malloc(sizeof(char) * (length + argc));
	concat(storage, length, argc, argv);
	return (storage);
}

int		get_size(int argc, char **argv)
{
	int i;
	int length;

	length = 0;
	i = 1;
	while (i < argc)
	{
		length += ft_strlen(argv[i]);
		i++;
	}
	return (length);
}

int		ft_strlen(char *str)
{
	int counter;

	counter = 0;
	while (*(str + counter) != '\0')
	{
		counter = counter + 1;
	}
	return (counter);
}

char	*concat(char *str, int length, int argc, char **argv)
{
	int i;
	int j;
	int cur;

	j = 1;
	i = 0;
	cur = 0;
	while (argc > 1)
	{
		if (argv[j] == NULL)
			j++;
		while (argv[j][cur] != '\0')
		{
			str[i] = argv[j][cur];
			cur++;
			i++;
		}
		str[i] = '\n';
		i++;
		argc--;
		j++;
		cur = 0;
	}
	str[i] = '\0';
	return (str);
}
