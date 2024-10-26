# Protocol stack and corresponding layers 
#
# Author: securityalert1st
# 
#
#
# Protocol 	    Layer
#----------------------------------------
# Applaction     HTTP/FTP/SNMP/TELNET etc.
# Transport      TCP/UDP
# Network        IP/ICMP,Routing
# LINK           Network interface, drivers


import socket
import ipaddress

class ApplacationLayer:
    def __init__(self, data):
        self.data = data
    def get_data(self):
        self.data_type = "Applaction"
        if self.data.startswith("HTTP"):
            self.data_type = "HTTP"
            return self.data
        elif self.data.startswith("FTP"):
            self.data_type = "FTP"
            return self.data
        elif self.data.startswith("SNMP"):
            self.data_type = "SNMP"
            return self.data
        elif self.data.startswith("TELNET"):
            self.data_type = "TELNET"
            return self.data
        else:
            self.data_type = "Other/Unknown"
            return self.data
    def get_data_type(self):
        return self.data_type
    

class TransportLayer:
    def __init__(self, data):
        self.data = data
    def get_data(self):
        if self.data.startswith("TCP"):
            self.data_type = "TCP"
            return self.data
        elif self.data.startswith("UDP"):
            self.data_type = "UDP"
            return self.data
        else:  
            self.data_type = "Other/Unknown"
            return self.data

    def get_data_type(self):
        return self.data_type
    
class NetworkLayer:
    def __init__(self, data):
        self.data = data
    def get_data(self):
        if self.data.startswith("IP"):
            self.data_type = "IP"
            return self.data
        elif self.data.startswith("ICMP"):
            self.data_type = "ICMP"
            return self.data
        elif self.data.startswith("Routing"):
            self.data_type = "Routing"
            return self.data
        else:
            self.data_type = "Other/Unknown"
            return self.data
    def get_data_type(self):
        return self.data_type
    
class LinkLayer:
    def __init__(self, data):
        self.data = data
    def get_data(self):
        if self.data.startswith("Network interface"):
            self.data_type = "Network interface"
            ipaddress.ip_interface(self.data)
            return self.data
    def get_data_type(self):
        return self.data_type
    
class GetFramePacket:
    def __init__(self, data):
        self.data = data
        self.applaction_layer = ApplacationLayer(data)
        self.transport_layer = TransportLayer(data)
        self.network_layer = NetworkLayer(data)
        self.link_layer = LinkLayer(data)
    def get_applaction_layer(self):
        return self.applaction_layer
    def get_transport_layer(self):
        return self.transport_layer
    def get_network_layer(self):
        return self.network_layer
    def get_link_layer(self):
        return self.link_layer
    def get_data(self):
        return self.data
    def get_data_type(self):
        return self.applaction_layer.get_data_type() + "/" + self.transport_layer.get_data_type() + "/" + self.network_layer.get_data_type() + "/" + self.link_layer.get_data_type()
    
    





