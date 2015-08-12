# -*- coding: utf-8 -*-
class mstplugin:
    infos = [
        ['port','Í¬IPport[chinaz]°æ'],
        ['Author','mst'],
        ['Update','2013/11/02'],
        ['site','http://mstoor.duapp.com']
        ]
    opts  = [
        ['URL','mstoor.duapp.com','portport']
        ]
    def exploit(self):
        '''port'''
        chinaz = 'http://tool.chinaz.com/Same/'
        value  = {'s':URL}
        try:
            color.cprint("[*] Sending data..",YELLOW)
            tmp = fuck.urlpost(chinaz,value).read().decode("utf-8")
            if len(tmp)>0:
                color.cprint("[+] Formate data..",YELLOW)
                res = fuck.find('.</span> <a href=[^>]+ target=_blank>',tmp)
                reslen,resiii,reslog = len(res),1,"sameIP_web[chinaz]_%s"%RURL
                for r in res:
                    ok= r[18:].split("'")[0]
                    color.cprint("[%s/%s] %s"%(resiii,reslen,ok),GREEN)
                    fuck.writelog(reslog,ok)
                    resiii+=1
                color.cprint("[*] Get data Successful !LOG:output/%s.log"%reslog,CYAN)
            else:
                color.cprint("[-] Nothing :(",RED)
        except Exception,e:
            color.cprint("[!] Err:%s"%e,RED)

