/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_program_name.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/05 10:02:10 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/05 10:15:43 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);
void	ft_putstr(char *str);

int		main(int argc, char **argv)
{
	ft_putstr(argv[0]);
	ft_putchar('\n');
	return (0);
}

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
