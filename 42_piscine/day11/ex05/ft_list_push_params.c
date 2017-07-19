/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_push_params.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 14:52:48 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:39:24 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

t_list		*ft_list_push_params(int ac, char **av)
{
	int		i;
	t_list	*head;
	t_list	*temp;
	t_list	*cursor;

	i = ac - 2;
	if (ac == 1)
	{
		head = 0;
		return (head);
	}
	head = ft_create_elem(av[ac - 1]);
	cursor = head;
	while (i > 0)
	{
		temp = ft_create_elem(av[i]);
		while (cursor->next != 0)
		{
			cursor = cursor->next;
		}
		cursor->next = temp;
		i--;
	}
	return (head);
}
