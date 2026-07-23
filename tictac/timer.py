import time
import functools


class timer:
    """timer - context manager and decorator for measuring code execution time

    usage:
        # context manager
        with timer("task"):
            ...

        # decorator
        @timer
        def func(): ...

        @timer("task", unit="ms")
        def func(): ...
    """

    def __init__(self, name=None, unit="s", output=None):
        if callable(name):
            self._func = name
            self._name = name.__name__
        else:
            self._func = None
            self._name = name

        self._unit = unit
        self._output = output
        self._start = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        assert self._start is not None
        elapsed = time.perf_counter() - self._start
        self._print(elapsed)

    def __call__(self, *args, **kwargs):
        if self._func is not None:
            with self:
                return self._func(*args, **kwargs)

        func = args[0]
        self._name = self._name or func.__name__

        @functools.wraps(func)
        def wrapper(*a, **kw):
            with timer(self._name, self._unit, self._output):
                return func(*a, **kw)

        return wrapper

    def _format(self, elapsed):
        if self._unit == "ms":
            return f"{elapsed * 1000:.2f} ms"
        elif self._unit == "min":
            return f"{elapsed / 60:.2f} min"
        return f"{elapsed:.2f} sec"

    def _print(self, elapsed):
        msg = f"[tictac] {self._name}: {self._format(elapsed)}"
        if self._output:
            self._output(msg)
        else:
            print(msg)
