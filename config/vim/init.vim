" setting
set fenc=utf-8
set nobackup
set noswapfile
set autoread
set hidden
set showcmd

set number
set cursorline
set virtualedit=onemore
set smartindent
set visualbell
set showmatch
set laststatus=2
set wildmode=list:longest
nnoremap j gj
nnoremap k gk

" Alias for set number
:command NumOn  set number
:command NumOff set number!

" Tab
"set expandtab
set tabstop=8
set shiftwidth=8

:function FnTab8()
:  set expandtab!
:  set tabstop=8
:  set shiftwidth=8
:endfunction

:function FnTab4()
:  set expandtab
:  set tabstop=4
:  set shiftwidth=4
:endfunction

:function FnTab2()
:  set expandtab
:  set tabstop=2
:  set shiftwidth=2
:endfunction

:command Tab2 call FnTab2()
:command Tab4 call FnTab4()
:command Tab8 call FnTab8()

set ignorecase
set smartcase
set incsearch
set wrapscan
set hlsearch
nmap <Esc><Esc> :nohlsearch<CR><Esc>
nnoremap <silent> m, :Unite mark<CR>

noremap gj gk
noremap gk gj
noremap <C-j> <C-d>
noremap <C-k> <C-u>

noremap <C-h> ^
noremap <C-l> $
noremap <C-s> :w<CR>
noremap <C-a> gg V G

" Using <C-d> also As <Esc>
imap <C-d> <Esc>
noremap! <C-d> <Esc>
imap <C-d><C-d> <Esc>:
noremap! <C-d><C-d> <Esc>:
" Using <C-q><C-q> as quit and save
imap <C-q><C-q> <Esc>:wq<CR>
noremap! <C-q><C-q> <Esc>:wq<CR>

" ranger-explorer
nnoremap <silent><Leader>c :RangerOpenCurrentDir<CR>
nnoremap <silent><Leader>f :RangerOpenProjectRootDir<CR>
nnoremap <silent><Leader>r :RangerCurrentDirectoryNewTab<CR>

nnoremap <C-f> :RangerCurrentDirectoryNewTab<CR>

" QuickRun
nnoremap <C-r> :QuickRun<CR>

" VimFiler
" nnoremap <C-f> :VimFiler<CR>

" For Window
"" Change WIndow with mouse
:set mouse=n
if !has('nvim')
	:set ttymouse=xterm2
endif

set hlsearch

"dein Scripts----------------------------
if &compatible
  set nocompatible       " Be iMproved
endif

let g:CACHE_HOME=empty($XDG_CACHE_HOME) ? expand('$HOME/.cache') : $XDG_CACHE_HOME
let g:DEIN_HOME=g:CACHE_HOME . '/dein'
let g:DEIN_PATH=g:DEIN_HOME . '/repos/github.com/Shougo/dein.vim'
let g:CONFIG_HOME=empty($XDG_CONFIG_HOME) ? expand('$HOME/.config') : $XDG_CONFIG_HOME
let g:NVIM_CONFIG_HOME=g:CONFIG_HOME . '/nvim'
let g:DEIN_TOML_NVIM=g:NVIM_CONFIG_HOME . '/dein.toml'
let g:DEIN_TOML_VIM=expand('$HOME') . '/dein.toml'
let g:DEIN_TOML_LAZY_NVIM=g:NVIM_CONFIG_HOME . '/dein_lazy.toml'
let g:DEIN_TOML_LAZY_VIM=expand('$HOME') . '/dein_lazy.toml'
if !has('nvim')
	let g:DEIN_TOML=g:DEIN_TOML_VIM
	let g:DEIN_TOML_LAZY=g:DEIN_TOML_LAZY_VIM
else
	let g:DEIN_TOML=g:DEIN_TOML_NVIM
	let g:DEIN_TOML_LAZY=g:DEIN_TOML_LAZY_NVIM
endif

if !isdirectory(g:DEIN_PATH)
  call system('git clone https://github.com/Shougo/dein.vim' . ' ' . shellescape(g:DEIN_PATH))
endif

" Required:
let &runtimepath = g:DEIN_PATH . "," . &runtimepath

" Required:
if dein#load_state(g:DEIN_HOME)
  call dein#begin(g:DEIN_HOME)

  " Load TOML
  " Load Plugins when vim is launched
  call dein#load_toml(g:DEIN_TOML, {'lazy': 0})
  " Load Plugins after vim is launched
  call dein#load_toml(g:DEIN_TOML_LAZY, {'lazy': 1})

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------

" Plugin Setting
:set tags=tags
