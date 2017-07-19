/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_size.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 14:36:13 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:37:22 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

int		ft_list_size(t_list *begin_list)
{
	t_list	*cursor;
	int		counter;

	counter = 0;
	cursor = begin_list;
	while (cursor != 0)
	{
		cursor = cursor->next;
		counter++;
	}
	return (counter);
}
