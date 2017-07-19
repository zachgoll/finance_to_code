/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 07:48:18 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/11 08:02:34 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_is_sort(int *tab, int length, int (*f)(int, int))
{
	int i;

	i = 0;
	while (i < length - 1)
	{
		if (length == 1)
			return (1);
		else if (f(tab[i], tab[i + 1]) < 0 || f(tab[i], tab[i + 1]) == 0)
			i++;
		else
			return (0);
	}
	return (1);
}
