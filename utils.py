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
