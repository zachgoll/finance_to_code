/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split_whitespaces.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/07 22:25:46 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/07 22:35:52 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		count_strings(char *str);
char	*alloc_strings(char *str, int *index);
char	**ft_split_whitespaces(char *str);

char	**ft_split_whitespaces(char *str)
{
	int		i;
	int		len;
	int		index;
	char	**ptr;

	len = count_strings(str);
	ptr = (char**)malloc(sizeof(char*) * (len + 1));
	i = 0;
	index = 0;
	while (str[0] == ' ' || str[0] == '\t' || str[0] == '\n')
		str++;
	while (str[i] != '\0')
		ptr[index++] = alloc_strings(str, &i);
	ptr[index] = 0;
	return (ptr);
}

int		count_strings(char *str)
{
	int i;
	int j;
	int flag;

	i = 0;
	j = 0;
	flag = 0;
	while (str[i] != '\0')
	{
		while (str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
		{
			flag = 1;
			if (str[i] != '\0')
				i++;
			else
				break ;
		}
		while (str[i] == '\n' || str[i] == '\t' || str[i] == ' ')
			i++;
		if (flag == 1)
			j++;
		flag = 0;
	}
	return (j);
}

char	*alloc_strings(char *str, int *index)
{
	int		len;
	int		i;
	int		j;
	char	*str_ptr;

	len = *index;
	i = len;
	while (str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
	{
		if (str[i] != '\0')
			i++;
		else
			break ;
	}
	j = i;
	while (str[i] == '\n' || str[i] == '\t' || str[i] == ' ')
		i++;
	*index = i;
	i = -1;
	str_ptr = (char *)malloc(j - len + 1);
	while (++i < j - len)
		str_ptr[i] = str[len + i];
	str_ptr[i] = '\0';
	return (str_ptr);
}
