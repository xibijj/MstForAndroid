'''
MST::update
VER::20131102
'''
from urllib     import urlopen
from os         import path
from MstColor   import *
from MstExploit import ver
from base64     import decodestring as de

url = "http://mstoor.duapp.com/update/"

class update:
    '''update mst plugins&functions'''
    def download(self):
        try:
            #download exploit functions..
            color.cprint("[*] update MstExploit.py..",YELLOW)
            tmp = urlopen(url+"?do=ver").read()
            tmp = tmp.replace("\n","")
            if int(ver)>int(tmp):
                tmp = urlopen(url+"?do=url").read()
                tmp = tmp.replace("\n","")
                res = urlopen(tmp).read()
                res = res.replace("\r","")
                fpp = open("libs/MstExploit.py","w")
                fpp.write(res)
                fpp.close()
                color.cprint("[*] Done ! ",CYAN)
            #download plugins
            color.cprint("[*] update Plugins..",YELLOW)
            tmp = urlopen(url+"?do=vip").readlines()
            for t in tmp:
                t = t.replace("\n","")
                t = t.replace("\r","")
                if len(t)>0:
                    tmp = t.split("{|MST|}")
                    upu = tmp[0]
                    upn = de(tmp[1])
                    upt = de(tmp[2])
                    if upn[len(upn)-3:].upper() != ".PY":
                        upn = upn+".py"
                    uuu = "plugins/%s/%s"%(upt,upn)
                    if not path.exists(uuu):
                        color.cprint("[-] download %s "%upn,GREEN,0)
                        tmp = urlopen(upu).read()
                        tmp = tmp.replace("\r","")
                        fpp = open(uuu,"w")
                        fpp.write(tmp)
                        fpp.close()
                        color.cprint("Done :)",YELLOW)
            color.cprint("[*] All Update Done :)",CYAN)
        except Exception,e:
            print e

if __name__ == '__main__':
    print __doc__
else:
    update=update()
