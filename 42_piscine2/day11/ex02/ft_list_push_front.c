/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_push_front.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 14:22:12 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:35:59 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

void		ft_list_push_front(t_list **begin_list, void *data)
{
	t_list	*cursor;
	t_list	*temp;

	cursor = *begin_list;
	if (cursor == 0)
	{
		*begin_list = ft_create_elem(data);
		return ;
	}
	temp = ft_create_elem(data);
	temp->next = *begin_list;
	*begin_list = temp;
}
