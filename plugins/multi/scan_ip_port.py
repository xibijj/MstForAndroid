# -*- coding: utf-8 -*-
class mstplugin:
    '''portIPport≥Ã∞ÊBy mst'''
    infos = [
        ['Plugin','ºÚµ•IPportport'],
        ['Author','mst'],
        ['Ver','3.0'],
        ['Update','20131102'],
        ['site','http://mstoor.duapp.com']
        ]
    opts  = [
        ['HOST','127.0.0.1','scan ip'],
        ['THREAD','5','start threads']
        ]
    ports = [
        ['21','FTP'],
        ['22','SSH'],
        ['23','TELNET'],
        ['25','SMTP'],
        ['80','HTTP'],
        ['135','SMB'],
        ['139','SMB'],
        ['443','HTTPS'],
        ['445','SMB'],
        ['1080','PROXY'],
        ['1433','MSSQL'],
        ['1723','VPN'],
        ['3306','MYSQL'],
        ['3389','MSTSC'],
        ['5432','POSTGRE'],
        ['8080','PROXY']
        ]
    def exploit(self):
        '''plugin exploit '''
        color.cprint("    %-32s %-8s %-10s %-20s"%("RHOST","PORT","STATUE","DESCRIPTION"),YELLOW)
        color.cprint("    %-32s %-8s %-10s %-20s"%("-"*32,"-"*8,"-"*10,"-"*20),GREY)
        def th(args):
            port,desc = args[0],args[1]
            if fuck.checkport(HOST,port):
                color.cprint("    %-32s %-8s %-10s %-20s\n"%(HOST,port,"OPEN",desc),GREEN,0)
                fuck.writelog("scan_ip_port",HOST+"::"+port+"::"+desc+"::OPEN")
            else:
                color.cprint("    %-32s %-8s %-10s %-20s\n"%(HOST,port,"CLOSE",desc),WHITE,0)
        fuck.thread(th,self.ports,THREAD)
