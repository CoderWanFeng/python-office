# -*- coding: UTF-8 -*-
"""支持 ``python -m office`` 作为 ``po`` 命令的等价入口。"""

import sys

from office.cli.main import main

if __name__ == "__main__":
    sys.exit(main())
