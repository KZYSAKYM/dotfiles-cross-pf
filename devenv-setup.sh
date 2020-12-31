#!/usr/bin/env bash

RECIPES="\
  nvim_dependencies \
  nvim_config \
  vim \
  vim_config \
  nvim \
  rust \
  bat \
  exa \
  findfd \
  procs \
  ripgrep \
  rls \
  zsh \
  zsh_prezto \
  zsh_config \
  curl \
  ranger \
  npm \
  bash-language-server \
  typescript-language-server \
  vscode-html-languageserver-bin \
  bash-it \
  fzf \
  tmux \
  tmux_config \
"

python3 main.py --recipe $RECIPES
