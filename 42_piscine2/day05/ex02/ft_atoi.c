/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/04 11:03:20 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/04 21:40:54 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		validate(char *str);
int		pos_neg(char flag);

int		ft_atoi(char *str)
{
	int	output;
	int i;

	i = 0;
	if (validate(str) == 0)
	{
		return (0);
	}
	else if (validate(str) == -1)
	{
		while (str[i] != '-')
			i++;
		i++;
		while (str[i] >= '0' && str[i] <= '9')
			output = (output * 10) + str[i++] - '0';
		output = -output;
	}
	else
	{
		while (str[i] < '0' || str[i] > '9')
			i++;
		while (str[i] >= '0' && str[i] <= '9')
			output = (output * 10) + str[i++] - '0';
	}
	return (output);
}

int		validate(char *str)
{
	char	flag;
	int		i;

	flag = '0';
	i = 0;
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\v' ||
	str[i] == '\r' || str[i] == '\f' || str[i] == '\n')
		i++;
	if (str[i] == '+' || str[i] == '-')
	{
		flag = str[i];
		i++;
	}
	if (str[i] < '0' || str[i] > '9')
		return (0);
	else
		return (pos_neg(flag));
}

int		pos_neg(char flag)
{
	if (flag == '+')
		return (1);
	else if (flag == '-')
		return (-1);
	else
		return (1);
}
