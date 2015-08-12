#!/usr/bin/python2.7
#coding:utf-8
################################
# mst::My Sec Tools            #
# ver::2.0Beta                 #
# mkt::2013-11-03              #
# url::http://mstoor.duapp.com #
################################
from libs.MstUpdate import update
from libs.MstCache  import cache

if __name__ == "__main__":
    try:
        cache.start()
        while True:
            cache.printmst()
            cmd = raw_input('>')
            if   cmd == 'help':
                cache.mainhelp()
            elif cmd == 'exit':
                cache.mainexit()
            elif cmd == 'cls':
                cache.cls()
            elif cmd == 'use':
                cache.usage("use")
            elif cmd == 'show':
                cache.usage("show")
            elif cmd == 'search':
                cache.usage("search")
            elif cmd == 'banner':
                cache.banner()
            elif cmd == 'update':
                update.download()
                cache.start()
            elif len(cmd.split(" ")) == 2:
                n = cmd.split(" ")
                c = n[0]
                g = n[1]
                if   c == 'search':
                    if len(g.replace(" ",""))>0:
                        cache.search(g)
                    else:
                        cache.usage(c)
                elif c == 'show':
                    if   g == 'exploit':
                        cache.showplus("exploit")
                    elif g == 'payload':
                        cache.showplus("payload")
                    elif g == 'multi':
                        cache.showplus("multi")
                    else:
                        cache.usage(c)
                elif c == 'use':
                    if len(g.replace(" ",""))>0:
                        cache.load(g)
                    else:
                        cache.usage(c)
                elif len(cmd.replace(" ",""))>0:
                    cache.execmd(cmd)
            elif len(cmd.replace(" ",""))>0:
                cache.execmd(cmd)
    except KeyboardInterrupt:
        cache.mainexit()
    except Exception,e:
        cache.errmsg(e)
