# -*- coding: utf-8 -*-
class mstplugin:
    '''crack sub_domain'''
    infos = [
        ['Plugin','Web_pathscan'],
        ['Author','mst'],
        ['Update','2013/11/02'],
        ['site','http://mstoor.duapp.com']
        ]
    opts  = [
        ['DOMAIN','google.com','Url'],
        ['SUBDIC','dicts/sub_domain.lst','dic path'],
        ['THREAD','10','start threads']
        ]
    def exploit(self):
        dicts=open(SUBDIC).readlines()
        color.cprint("SCANN %s =>SUB DOMAINS"%DOMAIN.upper(),YELLOW)
        color.cprint("===================="+"="*len(DOMAIN),GREY)
        def bb(dic):
            domain = dic.strip("\n")+"."+DOMAIN
            res = fuck.urltoip(domain)
            if res != False:
                log="%-35s %-25s"%(domain,res)
                color.cprint(log+"\n",GREEN,0)
                fuck.writelog('sub_domain_%s'%DOMAIN,log)
            else:
                color.cprint("%-35s %-25s\n"%(domain,"{NULL}"),RED,0)
        fuck.thread(bb,dicts,THREAD)
        color.cprint("[*] ALL SCAN DONE ! SAVE TO output/sub_domain_%s.log!"%DOMAIN,YELLOW)
