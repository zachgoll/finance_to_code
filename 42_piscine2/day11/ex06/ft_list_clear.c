/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_clear.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/11 18:40:13 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/12 21:45:33 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"
#include <stdlib.h>

void	ft_list_clear(t_list **begin_list)
{
	t_list	*cursor;
	t_list	*temp;

	cursor = *begin_list;
	while (cursor != 0)
	{
		temp = cursor->next;
		free(cursor);
		cursor = temp;
	}
	*begin_list = 0;
}
