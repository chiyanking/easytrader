# -*- coding: utf-8 -*-
import logging
import sys

logger = logging.getLogger("easytrader")
logger.setLevel(logging.DEBUG)
logger.propagate = False

fmt = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(filename)s %(lineno)s: %(message)s"
)
# ch = logging.StreamHandler()
#
# ch.setFormatter(fmt)
# logger.handlers.append(ch)

sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(fmt)
logger.addHandler(sh)
