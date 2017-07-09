#!/bin/bash

echo '*** Python - Virtualenv setup in progress...'
virtualenv "~/virtualenv/python$1" || exit 1
rm -f "~/virtualenv/python$1/bin/python" || exit 1
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1" || exit 1
source "~/virtualenv/python$1/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '2.5' || $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Python - Installing Setuptools...'
  easy_install 'https://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.3.tar.gz' > /dev/null 2>&1 || exit 1
  rm -rf "~/virtualenv/python$1/lib/python$1/site-packages/distribute-"* || exit 1
  easy_install 'https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz' || exit 1

  echo '*** Python - Installing Pip...'
  pip install pip==1.1 || exit 1
fi

echo '*** Done.'
