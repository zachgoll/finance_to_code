/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rvelez <rvelez@student.42.us.org>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/03 14:47:04 by rvelez            #+#    #+#             */
/*   Updated: 2017/07/03 19:59:43 by rvelez           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(char *str)
{
	int i;
	int n;
	int negative_mult;

	n = 0;
	i = 0;
	negative_mult = 1;
	while (str[i] == ' ' || (str[i] >= '\t' && str[i] <= '\r'))
		i++;
	if (str[i] == '-')
		negative_mult = -1;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i] >= '0' && str[i] <= '9')
	{
		if (str[i] < '0' || str[i] > '9')
			return (n * negative_mult);
		n = 10 * n + (str[i] - '0');
		i++;
	}
	return (n * negative_mult);
}
