import os
import urllib
from nameko.dependency_providers import Config
from nameko.web.handlers import http
from urllib.request import urlopen
import sys
import psutil
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy


class HttpService:
    name = "files_client"


    config = Config()

    # Hello User!
    @http('GET', '/')
    def get_method0(self, request):
        print("\n")
        ip = '10.0.1.16'
        print("\n")
        print("IP:  " + str(ip))
        print ("Calling Method 1 with python version: ",sys.version_info[:])
        print("\n")
        sys.stdout.flush()

        # Format output for client
        msg='''
Hello, guys!
##########################################
Files available:
##########################################
URL: 10.0.1.16/files/
a.txt
b.txt
c.txt
d.txt
'''
        return msg

    @http('GET', '/files/')
    def grabpage(self, request):
        content = """function available\n1.a.txt \n2.b.txt \n3.c.txt \n4.d.txt \n"""
        return content        




    # Trailing slash required to avoid 301 redirect which fails. Not resolved.
    @http('GET', '/files/<string:filename>/')
    def get_method1(self, request, filename):
        backEndIp = "10.0.1.17" 
        CONFIG = {'AMQP_URI':"amqp://guest:guest@{}:5672".format(backEndIp)}

        filename = str(filename)
        with ClusterRpcProxy(CONFIG) as rpc:
            data = rpc.files_service.getfiles(filename)
 
        return data

