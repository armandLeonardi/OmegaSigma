# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:22:45 2018

@author: Marsupilami
"""

class country:
    
    version = "2.0"
    
    COUNTRY_NAME = False
    POP = False
    SIGMA = 0
    
    pop_mil = 0
    pop_sciMil = 0
    pop_sciSci = 0
    pop_sciMed = 0
    pop_med = 0
    
    sigma_mil = 0
    sigma_sci = 1
    sigma_med = 0
    
    pop_mil_list = []
    pop_sciMil_list  = []
    pop_sciSci_list  = []
    pop_sciMed_list  = []
    pop_med_list  = []
    
    sigma_mil_list  = []
    sigma_sci_list  = []
    sigma_med_list  = []
    
    def __init__(self,country_name,POP):
        self.COUNTRY_NAME = country_name
        self.POP = POP

    def verif_sumOfPop(self):
        return True if self.pop_mil + self.pop_sciMil + self.pop_sciSci + self.pop_sciMed + self.pop_med == self.POP  else False
        
    def update_SIGMA(self):
        self.SIGMA = self.sigma_mil + self.sigma_med + self.sigma_sci
    
    def update_POP(self):
        self.POP =self.pop_mil + self.pop_sciMil + self.pop_sciSci + self.pop_sciMed  + self.pop_med

    def countryDefeat(self):
        return True if self.pop_mil + self.pop_sciMil + self.pop_sciSci + self.pop_sciMed + self.pop_med <= 0 else False
    
    def viewPlayer(self):
        print("Country name : {0}".format(self.COUNTRY_NAME))
        print("Total OMEGA : {0}".format(self.POP))
        print("   - pop mil : {0}".format(self.pop_mil))
        print("   - pop sciMil :{0}".format(self.pop_sciMil))
        print("   - pop sciSci : {0}".format(self.pop_sciSci))
        print("   - pop sciMed : {0}".format(self.pop_sciMed))
        print("   - pop med : {0}\n".format(self.pop_med))
        print("Total SIGMA : {0}".format(self.SIGMA))
        print("   - research military capital : {0}".format(self.sigma_mil))
        print("   - research scientific capital : {0}".format(self.sigma_sci))
        print("   - research medical capital : {0}\n".format(self.sigma_med))
        
    def affectValues(self):
        self.pop_mil_list.append(self.pop_mil)
        self.pop_sciMil_list.append(self.pop_sciMil)
        self.pop_sciSci_list.append(self.pop_sciSci)
        self.pop_sciMed_list.append(self.pop_sciMed)
        self.pop_med_list.append(self.pop_med)
        
        self.sigma_mil_list.append(self.sigma_mil)
        self.sigma_sci_list.append(self.sigma_sci)
        self.sigma_med_list.append(self.sigma_med)