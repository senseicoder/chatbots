from datetime import datetime
import logging

logger = None

def init(pid, logfile):
  global logger
  logger = logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)
  logger.propagate = False
  fh = logging.FileHandler(logfile, "a")
  fh.setLevel(logging.DEBUG)
  logger.addHandler(fh)
  keep_fds = [fh.stream.fileno()]

def add(line):
  global logger
  logger.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + line)
