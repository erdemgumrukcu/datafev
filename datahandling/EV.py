# -*- coding: utf-8 -*-
"""
@author: egu
"""

class ElectricVehicle(object):
    
    def __init__(self,carID,bCapacity,p_max_ac_ph1=7.7,p_max_ac_ph3=22,p_max_dc=350,minSoC=0.2,maxSoC=1.0):
        """
        This method initializes the car objects.
        """
        self.type         = "Vehicle"
        self.vehicle_id   = carID
        self.bCapacity    = bCapacity*3600     #kWh to kWs
        
        self.p_max_ac_ph1 = p_max_ac_ph1 
        self.p_max_ac_ph3 = p_max_ac_ph3
        self.p_max_dc     = p_max_dc

        self.minSoC = minSoC
        self.maxSoC = maxSoC
        self.soc    = {}
        self.v2x    = {}
        self.x2v    = {}
                              
    def charge(self,ts,tdelta,p_in):
        """
        ts    : datetime
        tdelta: timedelta
        p_in  : float
        
        Charge starting from ts for tdelta by p_in
        p_in>0 charging
        p_in<0 discharging
        """  
        self.soc[ts+tdelta]=self.soc[ts]+p_in*tdelta.seconds/self.bCapacity
        self.v2x[ts]       =-p_in if p_in<0 else 0
        self.x2v[ts]       = p_in if p_in>0 else 0
        
#    def request_available_charger_list(self,server,tdelta,advance_reservation=False):
#        
#        if advance_reservation:
#            period_start=self.t_arr_est
#            period_end  =self.t_dep_est
#            period_step =tdelta
#        else:
#            period_start=self.t_arr_real
#            period_end  =self.t_dep_est
#            period_step =tdelta
#            
#        available_chargers=server.get_available_chargers(period_start,period_end,period_step)
#            
#        return available_chargers
        
    
