#!/bin/bash

if [[ -n "$1" ]]; then VER="$1"; else VER="$Python"; fi

if [[ $VER == '3.1' ]]; then
  VENV_VER='13.1.2'
elif [[ $VER == '2.5' ]]; then
  VENV_VER='1.9.1'
elif [[ $VER == '2.4' ]]; then
  VENV_VER='1.7.2'
fi

if [[ -n "$VENV_VER" ]]; then
  echo '*** Python - Installing Virtualenv...'
  wget -q "https://pypi.python.org/packages/source/v/virtualenv/virtualenv-${VENV_VER}.tar.gz" || exit 1
  tar -xz -f "virtualenv-${VENV_VER}.tar.gz" || exit 1
  cd "virtualenv-${VENV_VER}/" || exit 1
  "python$VER" setup.py install --prefix="$HOME/.local" || exit 1
  cd .. || exit 1
fi

echo '*** Python - Virtualenv setup in progress...'
"virtualenv-$VER" -p "python$VER" "$HOME/virtualenv/python$VER" || exit 1
source "$HOME/virtualenv/python$VER/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$VER"

if [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  echo '*** Python - Downgrading Pip (Workaround for missing SSL in Python 2.5)...'
  easy_install pip==1.2.1 || exit 1
fi

echo '*** Done.'
