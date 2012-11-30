#!/usr/bin/python
#
# Copyright (c) 2012, Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# - Neither the name of the University of California, Berkeley nor the names
#   of its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#
# Commonly used utilities
#
# by Owen Lu and Fernando Garcia Bermudez
#
# v.0.4
#
# Revisions:
#  Owen Lu                          2012-9-15   Adds auto-logging class
#                                   2012-9-24   Adds configuration loader
#  Fernando L. Garcia Bermudez      2012-11-21  Adds Bunch class; improves doc
#  w/Andrew Pullin                  2012-11-29  Adds progress bar function
#

import sys, logging

class PrintAndLog(object):
    '''
    File-like stream object that redirects writes to a logger instance and
    displays them.

    Reference: http://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/
    '''

    def __init__(self, logger, log_level=logging.INFO):
        self.logger    = logger
        self.log_level = log_level
        self.linebuf   = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
            sys.__stdout__.write(line + '\n')

class Bunch(object):
    '''
    Takes a dictionary and creates an object where its member variables
    are the dictionary keys, and each variable is initialized to the
    corresponding dictionary values.

    Reference: http://code.activestate.com/recipes/52308-the-simple-but-handy-collector-of-a-bunch-of-named/
    '''
    def __init__(self, adict):
        self.__dict__.update(adict)


def load_config(configfile, delimiter='=', comments='#'):
    '''
    Load configuration parameters from a text file.

    Parameters
    ----------
    configfile : file
        Filename to read.
    delimiter : str, optional
        The string used to separate variable names from their values;
        default: '='.
    comments : str, optional
        The character used to indicate the start of a comment;
        default: '#'.

    Returns
    -------
    out : dict
        Parameters read from the text file.
    '''
    params = dict()

    for line in open(configfile).readlines():
        if line.strip() != '' and line.strip()[0] != comments:
            [var, val] = line.split(delimiter)
            params[var.strip()] = eval(val)

    return params

def progress(current, total):
    '''Progress bar, originally developed by Andrew Pullin'''
    width  = 25
    dashes = int(float(current) / total * width)
    stars  = width - dashes - 1
    barstring = ' |' + '-'*dashes + '>' + '*'*stars + '|'
    sys.stdout.write('\r' + str(current).rjust(len(str(total))) + '/' \
                                              + str(total) + barstring)
    sys.stdout.flush()
