import urllib.request
import urllib.parse

import sys

class Md2Html:

    API_ADDRESS = 'https://api.github.com/markdown/raw'

    def __init__(self):
        self.__proxy_setting = "none"
    
    def set_proxy(self, proxy):
        self.__proxy_setting = proxy

    def to_html(self, source: str, output: str):
        with open(source, 'br') as file:
            data = file.read()

        # プロキシ設定
        if self.__proxy_setting != "none":
            proxy = urllib.request.ProxyHandler({"https": self.__proxy_setting})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)

        # git markdown api へアクセス
        request = urllib.request.Request(Md2Html.API_ADDRESS)
        request.add_header('Content-Type','text/plain')
        f = urllib.request.urlopen(request,data)

        # header 部分を取得
        with open('css/header.txt','br') as file:
            header = file.read()

        with open(output,'bw') as file:
            file.write(header)
            
        with open(output,'a') as file:
            file.write("\n<body>\n")

        with open(output,'ba') as file:
            file.write(f.read())
        
        with open(output,'a') as file:
            file.write("\n</body>\n</html>\n")
