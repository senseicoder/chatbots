from datetime import datetime
import logging

pid = "/var/run/passchat.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/var/log/passchat.log", "a")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]

def addlog(line):
  global logger
  logger.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + line)
