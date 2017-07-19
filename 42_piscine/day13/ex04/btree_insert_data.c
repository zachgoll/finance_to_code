/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   btree_insert_data.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/14 09:18:26 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/14 12:44:33 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_btree.h"

void	btree_insert_data(t_btree **root, void *item,
		int (*cmpf)(void *, void *))
{
	t_btree *temp;

	temp = *root;
	if (temp == 0)
	{
		temp = btree_create_node(item);
		*root = temp;
		return ;
	}
	if ((*cmpf)(item, temp->item) < 0)
		btree_insert_data(&temp->left, item, (*cmpf));
	else
		btree_insert_data(&temp->right, item, (*cmpf));
}
