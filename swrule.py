#!/usr/bin/python
import sys
import httplib
import json

class StaticEntryPusher(object):
    
    def __init__(self, server):
        self.server = server
    
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
    
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
    
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
    
    def rest_call(self, data, action):
        path = '/wm/staticentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret

pusher = StaticEntryPusher('127.0.0.1')
flow1= {
    "switch":"00:00:00:00:00:00:00:01",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_2",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow2= {
    "switch":"00:00:00:00:00:00:00:02",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_3",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow3= {
    "switch":"00:00:00:00:00:00:00:01",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_4",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow4= {
    "switch":"00:00:00:00:00:00:00:04",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_5",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow5= {
    "switch":"00:00:00:00:00:00:00:05",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_6",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow6= {
    "switch":"00:00:00:00:00:00:00:06",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_7",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow7= {
    "switch":"00:00:00:00:00:00:00:07",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_8",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow8= {
    "switch":"00:00:00:00:00:00:00:08",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_9",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow9= {
    "switch":"00:00:00:00:00:00:00:09",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_10",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow10= {
    "switch":"00:00:00:00:00:00:00:10",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_11",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow11= {
    "switch":"00:00:00:00:00:00:00:11",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_12",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow12= {
    "switch":"00:00:00:00:00:00:00:12",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_13",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow13= {
    "switch":"00:00:00:00:00:00:00:13",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_14",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow14= {
    "switch":"00:00:00:00:00:00:00:14",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_15",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow15= {
    "switch":"00:00:00:00:00:00:00:15",
    "eth_type":"0x0806",
    "cookie":"0","name":"flow_mod_16",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow16= {
    "switch":"00:00:00:00:00:00:00:16",
    "eth_type":"0x0806",
    "cookie":"0","name":"flow_mod_17",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow17= {
    "switch":"00:00:00:00:00:00:00:17",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_18",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow18= {
    "switch":"00:00:00:00:00:00:00:18",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_19",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow19= {
    "switch":"00:00:00:00:00:00:00:19",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_20",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow20= {
    "switch":"00:00:00:00:00:00:00:20",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_21",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow21= {
    "switch":"00:00:00:00:00:00:00:21",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_22",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow22= {
    "switch":"00:00:00:00:00:00:00:22",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_23",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow23= {
    "switch":"00:00:00:00:00:00:00:23",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_24",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow24= {
    "switch":"00:00:00:00:00:00:00:24",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_25",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow25= {
    "switch":"00:00:00:00:00:00:00:25",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_26",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow26= {
    "switch":"00:00:00:00:00:00:00:26",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_27",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow27= {
    "switch":"00:00:00:00:00:00:00:27",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_28",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow28= {
    "switch":"00:00:00:00:00:00:00:28",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_29",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow29= {
    "switch":"00:00:00:00:00:00:00:29",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_30",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}
flow30= {
    "switch":"00:00:00:00:00:00:00:30",
    "eth_type":"0x0806",
    "cookie":"0",
    "name":"flow_mod_01",
    "activate":"true",
    "arp_tpa":"10.0.0.3",
    "priority":"32768",
    "arp_opcode":"1",
    "actions":"set_field=eth_src->00:00:00:00:00:01, set_field=eth_dst->ff:ff:ff:ff:ff:ff, set_field=arp_spa->10.0.0.3, set_field=arp_sha->00:00:00:00:00:01, set_field=arp_tpa->10.255.255.255, set_field=arp_tha->ff:ff:ff:ff:ff:ff, output=in_port"
}

pusher.set(flow1)

pusher.set(flow2)

pusher.set(flow3)

pusher.set(flow4)

pusher.set(flow5)

pusher.set(flow6)

pusher.set(flow7)

pusher.set(flow8)

pusher.set(flow9)

pusher.set(flow10)

pusher.set(flow11)

pusher.set(flow12)

pusher.set(flow13)

pusher.set(flow14)

pusher.set(flow15)

pusher.set(flow16)

pusher.set(flow17)

pusher.set(flow18)

pusher.set(flow19)

pusher.set(flow20)

pusher.set(flow21)

pusher.set(flow22)

pusher.set(flow23)

pusher.set(flow24)

pusher.set(flow25)

pusher.set(flow26)

pusher.set(flow27)

pusher.set(flow28)

pusher.set(flow29)

pusher.set(flow30)

