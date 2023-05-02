" setting
set fenc=utf-8
set nobackup
set noswapfile
set autoread
set hidden
set showcmd
set modeline

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
:command NumOff set nonumber

" Tab
:function FnTab8()
:  setlocal noexpandtab
:  setlocal tabstop=8
:  setlocal shiftwidth=8
:endfunction

:function FnTab4()
:  setlocal expandtab
:  setlocal tabstop=4
:  setlocal shiftwidth=4
:endfunction

:function FnTab2()
:  setlocal expandtab
:  setlocal tabstop=2
:  setlocal shiftwidth=2
:endfunction

:command Tab2 call FnTab2()
:command Tab4 call FnTab4()
:command Tab8 call FnTab8()

" ----------------------------- -----------------------------

" Set default Tab4
call FnTab4()

set ignorecase
set smartcase
set incsearch
set wrapscan
set hlsearch
nmap <Esc><Esc> :nohlsearch<CR><Esc>

noremap <C-j> <C-d>
noremap <C-k> <C-u>

noremap <C-h> ^
noremap <C-l> $
nnoremap <C-a> gg V G

" Using <C-c> also As <Esc>
noremap <C-c> <Esc>
noremap <C-c><C-c> <Esc>:

" For Window
"" Change WIndow with mouse
" :set mouse=n
:set mouse=a
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
let g:VIM_CONFIG_HOME=g:CONFIG_HOME . '/vim'
let g:DEIN_TOML_NVIM=g:NVIM_CONFIG_HOME . '/dein.toml'
let g:DEIN_TOML_VIM=g:VIM_CONFIG_HOME . '/dein.toml'
let g:DEIN_TOML_LAZY_NVIM=g:NVIM_CONFIG_HOME . '/dein_lazy.toml'
let g:DEIN_TOML_LAZY_VIM=g:VIM_CONFIG_HOME . '/dein_lazy.toml'
let g:DEIN_TOML_LINUX_NVIM=g:NVIM_CONFIG_HOME . '/dein.linux.toml'
let g:DEIN_TOML_LINUX_VIM=g:VIM_CONFIG_HOME . '/dein.linux.toml'
let g:DEIN_TOML_WIN_NVIM=g:NVIM_CONFIG_HOME . '/dein.windows.toml'
let g:DEIN_TOML_WIN_VIM=g:VIM_CONFIG_HOME . '/dein.windows.toml'
if !has('nvim')
	let g:DEIN_TOML=g:DEIN_TOML_VIM
	let g:DEIN_TOML_LAZY=g:DEIN_TOML_LAZY_VIM
  let g:DEIN_TOML_LINUX=g:DEIN_TOML_LINUX_VIM
  let g:DEIN_TOML_WIN=g:DEIN_TOML_WIN_VIM
else
	let g:DEIN_TOML=g:DEIN_TOML_NVIM
	let g:DEIN_TOML_LAZY=g:DEIN_TOML_LAZY_NVIM
  let g:DEIN_TOML_LINUX=g:DEIN_TOML_LINUX_NVIM
  let g:DEIN_TOML_WIN=g:DEIN_TOML_WIN_NVIM
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
  if !exists('vscode')

    if has('unix') || has('mac')
      call dein#load_toml(g:DEIN_TOML_LINUX, {'lazy': 0})
    elseif has('win32') || has('win64')
      call dein#load_toml(g:DEIN_TOML_WIN, {'lazy': 0})
    endif

    call dein#load_toml(g:DEIN_TOML, {'lazy': 0})
    " Load Plugins after vim is launched
    call dein#load_toml(g:DEIN_TOML_LAZY, {'lazy': 1})

  endif

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

" ctags:
"    C-] : jump definition
"    C-t : return
nnoremap <C-]> g<C-]>
inoremap <C-]> <ESC>g<C-]>
:set tags^=.git/tags,.svn/tags,./tags,*/.git/tags;~

" Change Tab setting per filetype
augroup ftTab
  autocmd!
  " C like Lang
  autocmd BufNewFile,BufRead *.c      call FnTab8()
  autocmd BufNewFile,BufRead *.cpp    call FnTab2()
  autocmd BufNewFile,BufRead *.h      call FnTab8()
  autocmd BufNewFile,BufRead *.hpp    call FnTab2()
  autocmd BufNewFile,BufRead *.cc     call FnTab2()
  " Other Programing Lang
  autocmd BufNewFile,BufRead *.py     call FnTab4()
  autocmd BufNewFile,BufRead *.rb     call FnTab4()
  autocmd BufNewFile,BufRead *.rs     call FnTab4()
  autocmd BufNewFile,BufRead *.go     call FnTab4()
  autocmd BufNewFile,BufRead *.cs     call FnTab4()
  autocmd BufNewFile,BufRead *.java   call FnTab4()
  autocmd BufNewFile,BufRead *.lua    call FnTab4()
  autocmd BufNewFile,BufRead *.sh     call FnTab2()
  autocmd BufNewFile,BufRead *.vim    call FnTab2()
  autocmd BufNewFile,BufRead *.ps1    call FnTab2()
  autocmd BufNewFile,BufRead *.bat    call FnTab2()
  " bitbake
  autocmd BufNewFile,BufRead *.bb         call FnTab4()
  autocmd BufNewFile,BufRead *.bbappend   call FnTab4()
  autocmd BufNewFile,BufRead *.bbclass    call FnTab4()
  autocmd BufNewFile,BufRead *.inc        call FnTab4()
  autocmd BufNewFile,BufRead *.cfg        call FnTab4()
  autocmd BufNewFile,BufRead *.conf       call FnTab4()
  " Web Lang
  autocmd BufNewFile,BufRead *.js     call FnTab2()
  autocmd BufNewFile,BufRead *.jsx    call FnTab2()
  autocmd BufNewFile,BufRead *.ts     call FnTab2()
  autocmd BufNewFile,BufRead *.tsx    call FnTab2()
  autocmd BufNewFile,BufRead *.xhtml  call FnTab2()
  autocmd BufNewFile,BufRead *.html   call FnTab2()
  autocmd BufNewFile,BufRead *.htm    call FnTab2()
  autocmd BufNewFile,BufRead *.xml    call FnTab2()
  autocmd BufNewFile,BufRead *.css    call FnTab2()
  autocmd BufNewFile,BufRead *.scss   call FnTab2()
  " Other
  autocmd BufNewFile,BufRead *.md     call FnTab2()
  autocmd BufNewFile,BufRead *.rst    call FnTab2()
  autocmd BufNewFile,BufRead *.txt    call FnTab2()
  autocmd BufNewFile,BufRead *.svg    call FnTab2()
  autocmd BufNewFile,BufRead *.ini    call FnTab2()
  autocmd BufNewFile,BufRead *.log    call FnTab2()
  autocmd BufNewFile,BufRead *.csv    call FnTab8()
  autocmd BufNewFile,BufRead *.json   call FnTab2()
  autocmd BufNewFile,BufRead *.yaml   call FnTab2()
  autocmd BufNewFile,BufRead *.yml    call FnTab2()
  autocmd BufNewFile,BufRead *.toml   call FnTab2()
  autocmd BufNewFile,BufRead Makefile call FnTab8()
  autocmd BufNewFile,BufRead *.make   call FnTab8()
  autocmd BufNewFile,BufRead Kconfig  call FnTab8()
  autocmd BufNewFile,BufRead CMake*   call FnTab4()
  autocmd BufNewFile,BufRead *.cmake  call FnTab4()
augroup END

if exists('g:nvui')
        autocmd InsertEnter * NvuiIMEEnable
        autocmd InsertLeave * NvuiIMEDisable
endif
