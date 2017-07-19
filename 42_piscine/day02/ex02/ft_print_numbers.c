/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/28 18:39:43 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/29 15:56:40 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);

void	ft_print_numbers(void)
{
	int current_num;

	current_num = 48;
	while (current_num < 58)
	{
		ft_putchar(current_num);
		current_num = current_num + 1;
	}
	return ;
}
