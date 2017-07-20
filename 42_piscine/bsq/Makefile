# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/07/17 07:56:39 by zgollwit          #+#    #+#              #
#    Updated: 2017/07/19 11:13:47 by zgollwit         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = bsq 

CC = gcc

SRCS = srcs/*.c map.c 

OBJECTS = *.o

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

re:	fclean all
