/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/28 11:27:54 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/29 15:46:47 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);

void	ft_print_alphabet(void)
{
	int current_letter;

	current_letter = 97;
	while (current_letter < 123)
	{
		ft_putchar(current_letter);
		current_letter = current_letter + 1;
	}
	return ;
}
