# .x-cmd/Dockerfile — `po` CLI 的干净环境测试镜像
#
# 用法：
#   docker build -f .x-cmd/Dockerfile -t po-test .
#   docker run --rm po-test                          # 跑 E2E 测试（.x-cmd/test.sh，real 模式）
#   docker run --rm po-test pytest tests/test_code/test_cli.py   # 跑 pytest 套件
#   docker run --rm po-test po --help                # 直接体验 po 命令
#   docker run --rm -it po-test bash                 # 交互 shell
#
# 说明：
# - 基于 python:3.10-slim，已装 PyMuPDF 运行时系统库（libgl1 / libglib2.0-0），
#   解决 slim 镜像缺 libGL.so.1 的问题
# - apt 与 pip 均走 aliyun 镜像（国内网络）；海外环境可删除两处 mirror 配置
# - 只装核心 CLI 依赖（popdf/poexcel/poimage/pofile/wftools/pomarkdown/pocode），
#   全量 install_requires 含 poocr/pospider/moviepy 等重型包，安装极慢且非核心所需
#   —— 这正是 office/__init__ 懒加载的价值：核心功能不依赖全家桶
# - 安装的是构建上下文里的本地代码；要测远端分支可改为：
#   pip install git+https://github.com/x-cmd-sourcecode/python-office@x-cmd-261025-po-cli

FROM python:3.10-slim

# --- apt: aliyun 镜像 + PyMuPDF 运行时依赖 ---
RUN sed -i 's|deb.debian.org|mirrors.aliyun.com|g; s|security.debian.org|mirrors.aliyun.com|g' \
        /etc/apt/sources.list.d/debian.sources 2>/dev/null; \
    sed -i 's|deb.debian.org|mirrors.aliyun.com|g' /etc/apt/sources.list 2>/dev/null; \
    apt-get update -qq && \
    apt-get install -y -qq --no-install-recommends libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# --- 安装本仓库（提供 po 入口与版本元数据）+ 核心依赖 ---
COPY . /app/python-office
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ \
        --no-deps /app/python-office && \
    pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ \
        popdf poexcel poimage pofile wftools pomarkdown pocode poprogress \
        rich loguru pytest

# --- 默认跑 E2E 测试（repo 副本优先于已安装副本） ---
ENV PYTHONPATH=/app/python-office
WORKDIR /app/python-office
CMD ["bash", ".x-cmd/test.sh"]
