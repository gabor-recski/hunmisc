
from subprocess import Popen, PIPE

class AbstractSubprocessClass(object):
    """
    Simple abstract wrapper class for commands that need to be
    called with Popen and communicate with them
    """
    def __init__(self, runnable, encoding="utf-8"):
        self._runnable = runnable
        self._encoding = encoding
        self._closed = True

    def start(self):
        #print self._runnable
        #print self.options
        self._process = Popen([self._runnable] + self.options,
                              stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self._closed = False

    def stop(self):
        if not self._closed:
            # HACK: communicate() sometimes blocks here
            self._process.terminate()
        self._closed = True

    def __exit__(self, exc_type, exc_value, traceback):
        if not self._closed:
            self.stop()

    def __del__(self):
        if not self._closed:
            self.stop()
