/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/30 15:54:05 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/30 16:10:32 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int result;
	int remainder;

	result = (*a / *b);
	remainder = (*a % *b);
	*a = result;
	*b = remainder;
	return ;
}
