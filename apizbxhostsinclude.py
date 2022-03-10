#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: Janssen dos Reis Lima
#edited: by João Arthur Rocha

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = ZabbixAPI("URL")
zapi.login(user="", password="")
arq = csv.reader(open('/tmp/hosts.csv'))

linhas = sum(1 for linha in arq)

f = csv.reader(open('/tmp/hosts.csv'), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip] in f:
    hostcriado = zapi.host.create({
        "host": hostname,
        "status": 1,
        "interfaces":[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": "10050"
        }],
        "groups": [{
			"groupid": "32"            
		}],
        "templates":[{
            "templateid": "10267"
        }]
    })


    i += 1
    bar.update(i)

bar.finish
'print' ''