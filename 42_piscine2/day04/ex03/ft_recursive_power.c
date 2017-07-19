/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/01 13:05:13 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/01 13:18:44 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_recursive_power(int nb, int power)
{
	if (nb > 0)
	{
		while (power > 0)
		{
			return (nb * ft_recursive_power(nb, (power - 1)));
		}
		return (1);
	}
	else if (nb == 0)
		return (1);
	else
		return (0);
}
