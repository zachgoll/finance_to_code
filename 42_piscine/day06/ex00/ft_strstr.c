/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/04 19:39:07 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/04 22:06:16 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(char *str, char *to_find)
{
	int match;
	int i;
	int j;

	i = 0;
	j = 0;
	if (to_find[0] == '\0')
		return (str);
	while (str[i] != '\0')
	{
		if (str[i++] == to_find[j])
		{
			match = 1;
			j++;
		}
		else
		{
			if (match == 1 && to_find[j] == '\0')
				return (to_find);
			i++;
			match = 0;
			j = 0;
		}
	}
	return (0);
}
