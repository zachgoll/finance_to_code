# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/07/12 15:20:02 by zgollwit          #+#    #+#              #
#    Updated: 2017/07/12 20:12:17 by zgollwit         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_display_file 

CC = gcc
SRCS = ft_display_file.c 

OBJECTS = ft_display_file.o

INCLUDES = -I ./includes/

CFLAGS = -Wextra -Werror -Wall

all: $(NAME)

$(NAME): $(OBJECTS)
	@$(CC) -o $(NAME) $(OBJECTS)
	@chmod 755 $(NAME)

$(OBJECTS): $(SRCS)
	@$(CC) -c $(CFLAGS) $(INCLUDES) $(SRCS)

clean:
	@/bin/rm -f *.o

fclean: clean
	@/bin/rm -f $(NAME)
