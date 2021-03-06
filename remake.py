#!/usr/bin/env python2.7

from __future__ import print_function
from makefile import Makefile
import argparse
import os
import sys


def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='makefile to use')
    parser.add_argument('-n', '--just-print', action='store_true',
                        help='Don\'t run commands. Only print them.')
    parser.add_argument('target', nargs='?',
                        help='target in the makefile to run')
    args = parser.parse_args()
    return args


def error(msg):
    print('Error: {}'.format(msg), file=sys.stderr)
    sys.exit(1)


def main():
    args = read_arguments()
    if args.file:
        # if -f flag was used to specify the makefile
        file_name = args.file
        # quit if this is not a valid file path
        if not os.path.exists(file_name) or not os.path.isfile(file_name):
            error('The file {} could not be found.'.format(file_name))
    else:
        file_name = ''
        # search the current directory for a makefile
        for path in os.listdir(os.getcwd()):
            if os.path.isfile(path):
                if os.path.basename(path).lower() == 'makefile':
                    file_name = path
                    break
        # quit if no makefile was found
        if not file_name:
            error('Makefile not found.')

    mkfile = Makefile(file_name, args.target, args.just_print)
    mkfile.run_makefile()


if __name__ == '__main__':
    main()
