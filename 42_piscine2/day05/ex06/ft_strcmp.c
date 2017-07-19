/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/04 20:19:30 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/04 22:40:40 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		compare(char a, char b);

int		ft_strcmp(char *s1, char *s2)
{
	int i;

	i = 0;
	if (s1[i] == '\0' || s2[i] == '\0')
		return (compare(s1[i], s2[i]));
	while (s1[i] != '\0' && s2[i] != '\0')
	{
		if (s1[i] != s2[i])
			return (compare(s1[i], s2[i]));
		i++;
	}
	if (s1[i] != s1[i])
		return (compare(s1[i], s2[i]));
	return (0);
}

int		compare(char a, char b)
{
	if (a < b)
		return (-1);
	else
		return (1);
}
