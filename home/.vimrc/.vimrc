let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()



call plug#end()


set nocompatible
filetype on
filetype plugin on
filetype indent on
syntax on
set number
set shiftwidth=2
set tabstop=2 
set expandtab
set nobackup
set incsearch
set showcmd
set showmode
set showmatch
set hlsearch
set wildmenu
set wildmode=list:longest
set wildignore=*.png,*.gif,*.pdf,*.pyc,*.exe,*.flx,*.img
