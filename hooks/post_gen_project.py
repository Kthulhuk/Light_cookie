#!/usr/bin/env python
import os


if __name__ == '__main__':
    os.system('git init')
    os.system('cp hooks/* .git/hooks')
    os.system('chmod +x .git/hooks/pre-commit')
    os.system('rm -r hooks')
    os.system('git checkout master')
