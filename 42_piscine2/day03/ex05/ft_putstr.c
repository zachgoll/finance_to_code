/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/30 16:14:32 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/30 23:10:03 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);

void	ft_putstr(char *str)
{
	int counter;

	counter = 0;
	while (*(str + counter) != '\0')
	{
		ft_putchar(*(str + counter));
		counter = counter + 1;
	}
}
