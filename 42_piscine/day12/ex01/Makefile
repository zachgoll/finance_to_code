# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zgollwit <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/07/12 15:20:02 by zgollwit          #+#    #+#              #
#    Updated: 2017/07/12 20:13:04 by zgollwit         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_cat 

CC = gcc
SRCS = ft_cat.c 

OBJECTS = ft_cat.o

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
