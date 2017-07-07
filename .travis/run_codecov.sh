#!/bin/bash

echo '*** Coverage testing...'

coverage run setup.py test || exit 1

echo '*** Done.'
