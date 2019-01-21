import os
import urllib
from nameko.web.handlers import http
from urllib.request import urlopen
import sys
import psutil
from nameko.rpc import rpc, RpcProxy

class FilesService:
    
    name = "files_service"
     
    @rpc
    def getfiles(self, filename):
        filename = str(filename)
        try:
            with open("./files/"+filename, "r") as fh:
                content = fh.read()
            return content
        except:
            message = 'No such files...'
            return message
