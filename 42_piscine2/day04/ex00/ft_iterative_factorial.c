/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/01 09:21:00 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/01 12:32:23 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_iterative_factorial(int nb)
{
	int n;

	n = nb;
	if (nb > 0)
	{
		while (nb > 1)
		{
			n = n * (nb - 1);
			nb--;
		}
		return (n);
	}
	else if (nb == 0)
		return (1);
	else
		return (0);
}
