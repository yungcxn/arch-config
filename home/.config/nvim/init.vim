call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
Plug 'norcalli/nvim-colorizer.lua'
Plug 'petertriho/nvim-scrollbar'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'scrooloose/nerdtree'
Plug 'PhilRunninger/nerdtree-visual-selection'
Plug 'majutsushi/tagbar'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

hi Normal guibg=NONE ctermbg=NONE

colorscheme catppuccin-mocha

lua require("colorizer").setup()

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
highlight Normal guibg=none

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif


nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

nnoremap <F8> :TagbarToggle<CR>
