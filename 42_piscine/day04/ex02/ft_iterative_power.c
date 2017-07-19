/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/01 12:37:31 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/01 12:51:06 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_iterative_power(int nb, int power)
{
	int i;

	i = nb;
	if (power > 0)
	{
		while (power > 0)
		{
			i = nb * i;
			power--;
		}
		return (i);
	}
	else if (power == 0)
		return (1);
	else
		return (0);
}
