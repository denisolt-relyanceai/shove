# -*- coding: utf-8 -*-
'''shove load points.'''

from shove.stuf.six import strings
from shove.stuf.utils import lazyimport
from .cache import *
from .store import *

stores = {
    'dbm': DBMStore,
    'file': FileStore,
    'memory': MemoryStore,
    'simple': SimpleStore,
    'lite': SQLiteStore,
}

caches = {
    'file': FileCache,
    'filelru': FileLRUCache,
    'memory': MemoryCache,
    'simple': SimpleCache,
    'memlru': MemoryLRUCache,
    'simplelru': SimpleLRUCache,
    'lite': SQLiteCache,
}


def cache_backend(uri, **kw):
    '''
    Loads the right cache backend based on a URI.

    :argument uri: instance or name :class:`str`
    '''
    if isinstance(uri, strings):
        mod = caches[uri.split('://', 1)[0]]
        # load module if setuptools not present
        if isinstance(mod, strings):
            # split classname from dot path
            module, klass = mod.split(':')
            # load module
            mod = lazyimport(module, klass)
        # load appropriate class from setuptools entry point
        else:
            mod
        # return instance
        return mod(uri, **kw)
    # no-op for existing instances
    return uri


def store_backend(uri, **kw):
    '''
    Loads the right store backend based on a URI.

    :argument uri: instance or name :class:`str`
    '''
    if isinstance(uri, strings):
        mod = stores[uri.split('://', 1)[0]]
        # load module if setuptools not present
        if isinstance(mod, strings):
            # isolate classname from dot path
            module, klass = mod.split(':')
            # load module
            mod = lazyimport(module, klass)
        # load appropriate class from setuptools entry point
        else:
            mod
        # return instance
        return mod(uri, **kw)
    # no-op for existing instances
    return uri
