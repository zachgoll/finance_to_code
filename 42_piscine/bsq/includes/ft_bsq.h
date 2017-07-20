/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bsq.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/07/17 09:32:00 by zgollwit          #+#    #+#             */
/*   Updated: 2017/07/19 22:00:17 by rvelez           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_BSQ_H
# define FT_BSQ_H

# include <stdlib.h>
# include <fcntl.h>
# include <unistd.h>
# include <sys/types.h>
# include <sys/uio.h>

int		ft_putchar(char c);
int		ft_atoi(char *str);
int		skip_lines(char *map);
int		skip_num(char *map);
int		get_file_size(char *file_str);
char	*redirect_out(char *file_str);
int		get_map_num(char *map);
int		get_map_width(char *map);
int		get_map_height(char *map);
int		check_valid(char *map);
int		check_vars(char *map, int position);
void	make_matrix(int ***map_matrix, char *map, int height, int width);
int		get_min(int x, int y, int z);
int		check_map_lines(char *map, int position);
int		check_lines_helper(char *map, int i, int map_start);
int		convert_char(char *map, char c);
void	get_characters(char **symbols, char *map);
void	find_largest_square(char *symbols, int **map_matrix, int height,
							int width);
char	*read_stdin(void);
void	stdin_helper(void);
void	find_s(char *symbols, int **map_matrix, int n[7]);
void	print_solution(char *symbols, int **map_matrix, int nums[7]);
void	main_helper(char *map);
#endif
