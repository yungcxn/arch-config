call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.
Plug 'folke/tokyonight.nvim'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'petertriho/nvim-scrollbar'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

colorscheme tokyonight-storm

hi Normal guibg=NONE ctermbg=NONE

lua require'colorizer'.setup()

lua require("scrollbar").setup()
set nocompatible
filetype on
filetype plugin on
filetype indent on
syntax on
set number
set shiftwidth=2
set tabstop=2 softtabstop=2 
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
set clipboard=unnamedplus
filetype plugin on
set cursorline
set ttyfast
set autoindent smartindent
