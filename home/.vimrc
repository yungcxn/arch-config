call plug#begin()

Plug 'catppuccin/vim', { 'as': 'catppuccin' }

call plug#end()

let g:lightline = {'colorscheme': 'catppuccin_mocha'}

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
