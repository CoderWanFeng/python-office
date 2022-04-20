yum install python-setuptools
easy_install pip
pip install shadowsocks

nohup ssserver -c shadowsocks.json -d start &

