# -*- coding: utf-8 -*-
__version__ = '0.0.1'
import sys
PYTHON2 = sys.version_info[0] < 3
def downloadFile(url,path):
    import os,urllib
    def Schedule(a, b, c):
        '''a:已经下载的数据块b:数据块的大小c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f% %' % per)
    filename = url.split("/")[-1]
    local = os.path.join(path,filename)
    urllib.urlretrieve(url,local,Schedule)

def getJsonObj(url):
    import urllib2,json
    if url is None:
        url = ""
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return json.loads(res)

def pingIP(ip):
    import ping
    result = ping.quiet_ping(ip, timeout=2, count=10, psize=64)
    #return:(丢包率,最大延迟,平均延迟) eg:(10, 15.000104904174805, 13.888915379842123)
    #print(result)
    return result

def portOnLine(address,port):
    import socket
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((address, port))
        s.close()
        return True
    except:
        return False

def list():
    print("list")
    jsonObj = getJsonObj(url=None)
    print(jsonObj["versions"])


def servers():
    print("servers")
    jsonObj = getJsonObj(url=None)

def download(path):
    if path:
        print("download")
    else:
        print("download ./")

def install(path):
    if path:
        print("install")
    else:
        print("install ./")

def pinfo():
    print("""
        =============================
        Frp NAT Downloader for Pyhton
        =============================

        pip install frp
        frp -h
        -----------------------------
        src: https://github.com/nat-cloud/frp
        -----------------------------
        """)

def main():
    # downloadFile("http://dldir1.qq.com/qqfile/qq/QQ8.9/20026/QQ8.9.exe","./")
    # print(getJsonObj("http://127.0.0.1:8000/ajax/t_erp_aliexpress_online_info_page?perpage=1&page=2"))
    # print(pingIP("www.baidu.com"))
    # print(portOnLine("www.baidu.com",81))
    import argparse
    parser = argparse.ArgumentParser(description='frp', prog='frp')
    parser.add_argument('--list', '-l', help='list version', action='store_true')
    parser.add_argument('--servers', '-s', help='free servers', action='store_true')
    parser.add_argument('--path', '-p', help='path')
    parser.add_argument('--download', '-d', help='download program')
    parser.add_argument('--install', '-i', help='install program')
    args = parser.parse_args()
    print(args)
    if args.list:
        list()
    if args.servers:
        servers()
    if args.download:
        download(args.path)
    if args.install:
        install(args.path)
    if not args.list and not args.servers and not args.download and not args.install:
        pinfo()

def _main():
    main()
    
if __name__ == '__main__':
    _main()
