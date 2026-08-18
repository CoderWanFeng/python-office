# -*- coding: utf-8 -*-
"""允许 ``python -m gui`` 直接启动。"""

import sys

from gui.app import main

if __name__ == "__main__":
    sys.exit(main())
