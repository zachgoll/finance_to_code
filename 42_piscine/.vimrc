execute pathogen#infect()
syntax enable

" Spaces and Tabs

set tabstop=4		" Number of spaces a tab counts for, or equivalently, the number of visual spaces per tab
set	softtabstop=4  " Number of spaces inserted when you hit the tab key, or removed when you hit backspace
" set expandtab       This can be uncommented to turn all tabs into spaces, so
" tab becomes a shortcut for four spaces

" -------------------------------------------------------------------------------------------------------------
" UI

set number	"shows line numbers
set showcmd	 "shows command you are typing in the bottom bar
set	cursorline "Highlight the current line
filetype indent on " load filetype specific indent files
"" If I have a python file open, the above command automatically loads
" ~/.vim/indent/python.vim ever time that type of file is open

set	wildmenu	"visual autocomplete for command menu
set showmatch	"Matches parens and brackets

" -------------------------------------------------------------------------------------------------------------
"  Searching

set	incsearch  "search as characters are entered

" -------------------------------------------------------------------------------------------------------------
"  Movement

" nnoremap j gj    " Now we can move vertically by VISUAL line rather than actual line
" nnoremap k gk 

" move to beginning/end of line
nnoremap B ^
nnoremap E $

" $/^ doesn't do anything
nnoremap $ <nop>
nnoremap ^ <nop>

" -----------------------------
"  Leaders

let mapleader=","   " leader is now comma
inoremap jk <esc> " Now, when you press the sequence "jk", you will effectively be pressing <esc>.  If you need
" to actually type jk, you can type j, and then wait for the timeout of the
" leader, and press k

" toggle the Gundo plugin - basically displays a tree of undos
nnoremap <leader>u :GundoToggle<CR>

" Shortcuts to edit the vimrc file
nnoremap <leader>ev :vsp $MYVIMRC<CR>
nnoremap <leader>ez :vsp ~/.zshrc<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>

" Save the current window configuration.  Here, you can now 'super save' by
" typing ',s'
nnoremap <leader>s :mksession<CR>

" Ctrlp settings

"let g:ctrlp_match_window = 'bottom,order:ttb'
"let g:ctrlp_switch_buffer = 0
"let g:ctrp_working_path_mode = 0
let g:ctrlp_user_command = 'ag %s -1 --nocolor --hidden -g""'
let g:ctrlp_user_command = 'ag %s -1 --nocolor -g ""'

" ----------------------------------

" Allows tmux mode
if exists('$TMUX')
	let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
	let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
else
	let &t_SI = "\<Esc>]50;CursorShape=1\x7"
	let &t_EI = "\<Esc>]50;CursorShape=0\x7"
endif

augroup configgroup
	autocmd!
	autocmd VimEnter * highlight clear SignColumn
	autocmd BufWritePre *.php,*.py,*.js,*.txt,*.hs,*.java,*.md
				\:call <SID>StripTrailingWhitespaces()
	autocmd FileType java setlocal noexpandtab
	autocmd FileType java setlocal list
	autocmd FileType java setlocal listchars=tab:+\ ,eol:-
	autocmd FileType java setlocal formatprg=par\ -w80\ -T4
	autocmd FileType php setlocal expandtab
	autocmd FileType php setlocal list
	autocmd FileType php setlocal listchars=tab:+\ ,eol:-
	autocmd FileType php setlocal formatprg=par\ -w80\ -T4
	autocmd FileType ruby setlocal tabstop=2
	autocmd FileType ruby setlocal shiftwidth=2
	autocmd FileType ruby setlocal softtabstop=2
	autocmd FileType ruby setlocal commentstring=#\ %s
	autocmd FileType python setlocal commentstring=#\ %s
	autocmd BufEnter *.cls setlocal filetype=java
	autocmd BufEnter *.zsh-theme setlocal filetype=zsh
	autocmd BufEnter Makefile setlocal noexpandtab
	autocmd BufEnter *.sh setlocal tabstop=2
	autocmd BufEnter *.sh setlocal shiftwidth=2
	autocmd BufEnter *.sh setlocal softtabstop=2
augroup END

set backup
set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set backupskip=/tmp/*,/private/tmp/*
set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set writebackup
