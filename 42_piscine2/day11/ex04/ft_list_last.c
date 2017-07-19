/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_last.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 14:47:56 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:38:18 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"

t_list	*ft_list_last(t_list *begin_list)
{
	t_list	*cursor;

	cursor = begin_list;
	if (cursor == 0)
		return (cursor);
	while (cursor->next != 0)
	{
		cursor = cursor->next;
	}
	return (cursor);
}
