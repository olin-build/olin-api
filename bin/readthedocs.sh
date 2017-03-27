#! /bin/bash

BGRED=`echo -e "\033[41m"`
FGBLUE=`echo -e "\033[35m"`
BGGREEN=`echo -e "\033[42m"`

NORMAL=`echo -e "\033[m"`

echo -e "\e[32mAfter this script runs, navigate to http://localhost:8000 to view the docs.\033[m"
source venv/bin/activate && cd ./docs/ && make html && cd _build/html/ && python -m http.server
