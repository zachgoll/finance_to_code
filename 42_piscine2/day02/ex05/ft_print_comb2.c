/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/29 19:45:39 by zgollwit          #+#    #+#             */
/*   Updated: 2017/06/29 19:50:10 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_putchar(char c);
void	print_nums(int a, int b, int c, int d);
void	ft_print_comb2(void);
void	helper(int a, int b, int c, int d);

void	print_nums(int a, int b, int c, int d)
{
	ft_putchar(a);
	ft_putchar(b);
	ft_putchar(32);
	ft_putchar(c);
	ft_putchar(d);
	if (a == 57 && b == 56 && c == 57 && d == 57)
	{
		return ;
	}
	ft_putchar(44);
	ft_putchar(32);
}

void	helper(int a, int b, int c, int d)
{
	while (a < 58)
	{
		while (b < 58)
		{
			while (c < 58)
			{
				while (d < 58)
				{
					print_nums(a, b, c, d);
					d = d + 1;
				}
				c = c + 1;
				d = 48;
			}
			c = a;
			b = b + 1;
			d = b + 1;
		}
		b = 48;
		a = a + 1;
		c = a;
		d = b + 1;
	}
}

void	ft_print_comb2(void)
{
	int a;
	int b;
	int c;
	int d;

	a = 48;
	b = 48;
	c = 48;
	d = 49;
	helper(a, b, c, d);
	return ;
}
