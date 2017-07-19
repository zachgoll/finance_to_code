/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   btree_level_count.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/14 14:58:25 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/14 15:00:00 by zgollwit         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_btree.h"

int		btree_level_count(t_btree *root)
{
	int a;
	int b;

	if (root == 0)
		return (0);
	else
	{
		a = get_height(root->left);
		b = get_height(root->right);
		if (a > b)
			return (a + 1);
		else
			return (b + 1);
	}
}
