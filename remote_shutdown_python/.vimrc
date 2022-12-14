set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax on
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
so ~/configs/.vim/plugins.vim
so ~/configs/.vim/coc-mapping.vim
" so ~/configs/.vim/maps.vim
colorscheme blue
colorscheme gruvbox
" highlight Normal ctermbg=NONE
set laststatus=2
set noshowmode

""" Searching 
set hlsearch
set incsearch
set ignorecase
set smartcase
set noerrorbells visualbell t_vb=
autocmd GUIEnter * set visualbell t_vb=
