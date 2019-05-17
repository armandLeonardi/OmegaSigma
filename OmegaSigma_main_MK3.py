# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:11:15 2019

@author: X188212
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:18:03 2018
@author: Marsupilami
"""

from math import *

class Country:
    
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
        

class OmegaSigma:
    
    version = "2.1"
    
    player1 = False
    player2 = False
    
    alphaForce = 0.1
    alphaMed = 0.1
    
    t = 0
    T = 100
    
    def __init__(self):
        print("Start OMEGA_SIGMA ¦ 1")
        print("Settings ¦ 2")
        choice = int(input("In [OS]: "))
        continu = True
        
        while continu:
            if choice == 1:
                k = True
                while k:
                    try:
                        print("Create player1 :")
                        name_country1 = input("In [OS]: Player1 country name : ")
                        pop_country1 = int(input("In [OS]: Player1 total population : "))
                        self.player1 =  Country(name_country1,pop_country1)
                    
                        print("Create player2 :")
                        name_country2 = input("In [OS]: Player2 country name : ")
                        pop_country2 = int(input("In [OS]: Player2 total population : "))
                        self.player2 =  Country(name_country2,pop_country2)
                        k = False
                    except:
                        print("Error for players creation. Please try again.",end="\n")
                
                self.start()
                self.t = 0
                
                k = True
                while k:
                    following = input("New game ? [y/n] : ")
                    if  following == 'n':
                        continu = False
                        k = False
                    elif following == 'y':
                        k = False
                    else:
                        print("Please select a right command")
                        choice = 1
                
            elif choice == 2:
                print("[Out] Version : ")
                print(self.version)
                
                print("[Out] AlphaForce : ")
                print(self.alphaForce)
                
                print("[Out] AlphaMed : ")
                print(self.alphaMed)
    
                print("[Out] t : ")
                print(self.t)
                
                print("[Out] T : ")
                print(self.T)
                
                choice = int(input("In [OS]: "))
                
            else:
                print("Please enter a write command.")
                choice = int(input("In [OS]: "))
    
    def computeMilForce(self,player):
        return self.alphaForce*player.pop_mil + player.sigma_mil
        
    def computeMed(self,player):
        return self.alphaMed*player.pop_med + player.sigma_med
    
    def updateSigma(self,player):
        self.updateSigmaForce(player)
        self.updateSigmaMed(player)
        self.updateSigmaSci(player)
    
    def updateSigmaForce(self,player):
        pop_sciMil = log(player.pop_sciMil) if player.pop_sciMil > 0 else 0
        player.sigma_mil = pop_sciMil**player.sigma_sci + player.sigma_mil 
        
    def updateSigmaSci(self,player):
        pop_sciSci = log(player.pop_sciSci) if player.pop_sciSci > 0 else 0
        player.sigma_sci = pop_sciSci + player.sigma_sci
        
    def updateSigmaMed(self,player):
        pop_sciMed = log(player.pop_sciMed) if player.pop_sciMed > 0 else 0
        player.sigma_med = pop_sciMed**player.sigma_sci + player.sigma_med
    
    def setPop(self,player):
        isOk = False
        while isOk == False:
            totalPop = player.POP
            print("______________________________")
            print("{0} ¦ {1} ¦ {2} set ressources ->".format(player.COUNTRY_NAME,player.POP,player.SIGMA))

            # pop mil
            pop_mil = float(input("Military population : "))
            totalPop -= pop_mil
            player.pop_mil = pop_mil
            print("Rest {0}".format(totalPop))
            
            # pop sciMil
            pop_sciMil =  float(input("Scientific population for military research : "))
            player.pop_sciMil = pop_sciMil
            totalPop -= pop_sciMil
            print("Rest {0}".format(totalPop))
            
            # pop sciSci
            pop_sciSci = float(input("Scientific population for scientific research :"))
            player.pop_sciSci = pop_sciSci
            totalPop -= pop_sciSci
            print("Rest {0}".format(totalPop))
            
            # pop sciMed
            pop_sciMed = float(input("Scientific population for medical research : "))
            player.pop_sciMed = pop_sciMed
            totalPop -= pop_sciMed
            print("Rest {0}".format(totalPop))
            
            
            # pop med
            pop_med = float(input("Medical population : "))
            player.pop_med = pop_med
            totalPop -= pop_med
            print("Rest {0}".format(totalPop))
            
            isOk = player.verif_sumOfPop()
            
            if isOk == True:
                print("{0} finish to set ressouces".format(player.COUNTRY_NAME))
            else:
                print("ERROR : sum of subpopulation is different to total population\n")
                player.viewPlayer()

        print("______________________________\n")

    
    def start(self):
        
        while self.t <= self.T :
            print("Step : {0}".format(self.t))
            # set ressources (pop) for mil, med and sci
            
            self.setPop(self.player1) # player 1
            self.setPop(self.player2) # player 2
            
            self.player1.affectValues() 
            self.player2.affectValues() 
            
            print("______________________________ FIGHT TIME\n")
            
            # compute military forces
            
            milForce_player1 = self.computeMilForce(self.player1)
            milForce_player2 = self.computeMilForce(self.player2)
            
            print("{0} ¦ military pop : {1} -> military forces : {2}\n".format(self.player1.COUNTRY_NAME,self.player1.pop_mil,milForce_player1))
            print("{0} ¦ military pop : {1} -> military forces : {2}\n".format(self.player2.COUNTRY_NAME,self.player2.pop_mil,milForce_player2))

            # reduce pop for both players
            
            self.player1.pop_mil-= int(milForce_player2)
            self.player2.pop_mil-= int(milForce_player1)
                        
            # compute pop from med for both players            
            
            medPopGain_player1 = self.computeMed(self.player1)
            medPopGain_player2 = self.computeMed(self.player2)
            
            print("{0} ¦ military population gain from medical : {1}\n".format(self.player1.COUNTRY_NAME,medPopGain_player1))
            print("{0} ¦ military population gain from medical : {1}\n".format(self.player2.COUNTRY_NAME,medPopGain_player2))

            # add pop from med for both players
            
            self.player1.pop_mil += int(medPopGain_player1)
            self.player2.pop_mil += int(medPopGain_player2)
            
            # update Sigma
            
            self.updateSigma(self.player1)
            self.updateSigma(self.player2)            
            
            # update players variables
            
            self.player1.update_SIGMA()
            self.player2.update_SIGMA()
            
            self.player1.update_POP()
            self.player2.update_POP()
            
            print("______________________________ END FIGHT TIME\n")

            # end step repports

            print("______________________________ STEP REPPORT\n")

            self.player1.viewPlayer()
            self.player2.viewPlayer()

            print("______________________________ END STEP REPPORT\n")

            # win condition
            
            if self.player1.countryDefeat() == True:
                print("Congratulation {0} you win the war.".format(self.player2.COUNTRY_NAME))    
                self.t = self.T + 1
            elif self.player2.countryDefeat() == True:
                print("Congratulation {0} you win the war.".format(self.player1.COUNTRY_NAME))            
                self.t = self.T + 1
            elif self.t == self.T:
                print("Time up ! The war is too long...")
        
            self.t += 1
                
                    
OS = OmegaSigma()