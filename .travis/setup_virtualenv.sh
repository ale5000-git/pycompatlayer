#!/bin/bash

if [[ -n "$1" ]]; then VER="$1"; else VER="$Python"; fi

echo '*** Python - Virtualenv setup in progress...'
virtualenv -p "python$VER" --setuptools "$HOME/virtualenv/python$VER" || exit 1
source "$HOME/virtualenv/python$VER/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$VER"

if [[ $VER == '3.1' ]]; then
  echo '*** Python - Updating Setuptools...'
  easy_install 'https://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.3.tar.gz' > /dev/null 2>&1 || exit 1
  rm -rf "$HOME/virtualenv/python$VER/lib/python$VER/site-packages/distribute-"* || exit 1
  pip install setuptools==19.4 || exit 1
elif [[ $VER == '2.5' || $VER == '2.4' ]]; then
  echo '*** Python - Updating Setuptools...'
  pip install setuptools==1.4.2 || exit 1

  echo '*** Python - Updating Pip...'
  pip install pip==1.1 || exit 1
fi

echo '*** Done.'
