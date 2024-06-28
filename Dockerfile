FROM dockerhub.cloud/library/python:3.7

# 配置环境变量
ENV PYTHONUNBUFFERED 1
#ARG PIP_MIRROR

# 安装依赖环境
RUN mkdir /app
COPY requirements.txt /app
# RUN pip install -r /app/requirements.txt -i "${PIP_MIRROR}"
RUN pip install -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 拷贝项目代码
COPY . /app
WORKDIR /app/thrillerbark

RUN chmod +x start.sh

EXPOSE 8000

ENTRYPOINT ["sh", "./start.sh"]

#https://www.idc1680.com/1090.html
