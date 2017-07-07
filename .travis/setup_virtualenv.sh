#!/bin/bash

echo '*** Python Virtualenv setup in progress...'
virtualenv "~/virtualenv/python$1" || exit 1
rm -f "~/virtualenv/python$1/bin/python" || exit 1
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1" || exit 1
source "~/virtualenv/python$1/bin/activate" || exit 1
export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Installing Python Setuptools...'
  pip install setuptools==0.7.3 > /dev/null 2>&1 || exit 1
  rm -rf "~/virtualenv/python$1/lib/python$1/site-packages/distribute-"* || exit 1

  pip install setuptools==1.4.2 || exit 1
fi

echo '*** Done.'
