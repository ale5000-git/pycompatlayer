#!/bin/bash

echo '*** Python - Virtualenv setup in progress...'
virtualenv -p "python$1" --setuptools "~/virtualenv/python$1" || exit 1
source "~/virtualenv/python$1/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '3.1' ]]; then
  echo '*** Python - Updating Setuptools...'
  easy_install 'https://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.3.tar.gz' > /dev/null 2>&1 || exit 1
  rm -rf "~/virtualenv/python$1/lib/python$1/site-packages/distribute-"* || exit 1
  pip install setuptools==19.4 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.5' || $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Python - Updating Setuptools...'
  pip install setuptools==1.4.2 || exit 1

  echo '*** Python - Updating Pip...'
  pip install pip==1.1 || exit 1
fi

echo '*** Done.'
