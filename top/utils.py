import time
import logging
from functools import wraps


DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

level = logging.DEBUG
log = logging.getLogger(__name__)
log.setLevel(level)
logFormatter = logging.Formatter("__%(asctime)s %(levelname)s: %(message)s")

consoleHandler =logging.StreamHandler()
consoleHandler.setLevel(level)
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)


def fun_time1(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


def fun_time2(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        resut = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, v) for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, resut))
        return resut
    return clocked


def log_me(fun):
    @wraps(fun)
    def wrap_me(*args, **kwargs):
        args_lst = []
        if args:
            args_lst.append(', '.join(map(str, args)))
        if kwargs:
            args_lst.append(', '.join('{0}={1}'.format(k, v) for k, v in kwargs.items()))
        args_str = ', '.join(args_lst)
        result = None
        t0 = time.time()
        try:
            result = fun(*args, **kwargs)
        except Exception as error:
            log.exception('Error: {0}'.format(error))
        elapsed = time.time() - t0
        log.info('[%0.8fs] %s(%s) -> %r ' % (elapsed, fun.__name__, args_str, result))

        return result
    return wrap_me
