/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_reverse_alphabet.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/28 18:31:56 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/29 15:49:27 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);

void	ft_print_reverse_alphabet(void)
{
	int current_letter;

	current_letter = 122;
	while (current_letter > 96)
	{
		ft_putchar(current_letter);
		current_letter = current_letter - 1;
	}
	return ;
}
