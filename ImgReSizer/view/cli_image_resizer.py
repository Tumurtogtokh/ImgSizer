#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This is where your module level help string goes.

.. module:: `CLI for Image Re-Sizer`
   :platform: Unix
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Tumurtogtokh Davaakhuu <tumurtogtokh@gmail.com>

------------------------------------------------------------
USE: python <PROGNAME> (options)
OPTIONS:
    -h : print this help message
    -t FILE : target size FILE
    -i FILE : image urls FILE
    -l : keep log configuration (default: without)
------------------------------------------------------------
'''
# IMPORT STANDARD
import getopt
import sys
import os

# GLOBAL CONSTANTS
TARGET_ERR = "** ERROR: must specify target sizes file (opt: -t FILE) **"
IMG_URL_ERR = "** ERROR: must specify image url file (opt: -i FILE) **"

# =============================================================================
# Command line processing

class CommandLine:
    '''
    CLI interface for controlling the app
    '''
    def __init__(self):
        self.exit = False
        self.img_urls_file = ''
        self.target_file = ''
        self.keep_log = False

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hl:t:i:l',
                                       ['help', 'target sizes', 'img url', 'keeplog'])
            opts = dict(opts)

        # ---------------------------------------------------------------------
            if '-h' in opts:
                self.print_help()
                self.exit = True
                return

            if len(args) > 0:
                print("** ERROR: no arg files - only options! **", file=sys.stderr)
                self.print_help()
                return

            if '-t' in opts:
                self.target_file = opts['-t']
            else:
                print(TARGET_ERR, file=sys.stderr)
                self.print_help()
                return

            if '-i' in opts:
                self.img_urls_file = opts['-i']
            else:
                print(IMG_URL_ERR, file=sys.stderr)
                self.print_help()
                return

            if '-l' in opts:
                self.keep_log = True

        except getopt.GetoptError as err:
            self.exit = True
            self.print_help()
            print("Specify correct **kwargs")

    def print_help(self):
        '''
        Displays help
        '''
        prog_name = sys.argv[0]
        # prog_name = progname.split('/')[-1] # strip off extended path
        # help = __doc__.replace('<PROGNAME>', prog_name, 1)
        print(__doc__.replace('<PROGNAME>', prog_name, 1), file=sys.stderr)

    def process_img_url_file(self):
        '''
        Return list of url
        '''
        urls = []
        if not os.path.isfile(self.img_urls_file):
            print(IMG_URL_ERR, file=sys.stderr)
            return urls
        with open(self.img_urls_file, 'r') as fin:
            for line in fin:
                if line.strip():
                    urls.append(line.strip())
        return urls

    def process_target_file(self):
        '''
        Returns target size list from input arg
        '''
        target = []
        if not os.path.isfile(self.target_file):
            print(TARGET_ERR, file=sys.stderr)
            return target
        with open(self.target_file, 'r') as fin:
            for line in fin:
                if line.strip():
                    target.append(int(line.strip()))
        return target

# =============================================================================
# MAIN

# if __name__ == '__main__':
    # config = CommandLine()
    # print(config.process_img_url_file())
    # print(config.process_target_file())

    # if config.exit:
    #     sys.exit(0)