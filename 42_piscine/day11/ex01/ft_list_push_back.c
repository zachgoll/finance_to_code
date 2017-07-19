/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_push_back.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 10:32:32 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:34:22 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void		ft_list_push_back(t_list **begin_list, void *data)
{
	t_list	*cursor;

	cursor = *begin_list;
	if (cursor == 0)
	{
		*begin_list = ft_create_elem(data);
		return ;
	}
	while (cursor->next != 0)
	{
		cursor = cursor->next;
	}
	cursor->next = ft_create_elem(data);
}
