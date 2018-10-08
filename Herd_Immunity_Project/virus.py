#source article is from https://www.theguardian.com/news/datablog/ng-interactive/2014/oct/15/visualised-how-ebola-compares-to-other-infectious-diseases
#data taken from https://docs.google.com/spreadsheets/d/1kHCEWY-d9HXlWrft9jjRQ2xf6WHQlmwyrXel6wjxkW8/edit#gid=0
#only untreated statistics are used

class Virus:
    def __init__(self, mortality_rate, reproductive_rate, name):
        self.name = name
        self.mortality_rate = mortality_rate
        self.reproductive_rate = reproductive_rate
   
    # def anthrax(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .2
    #     self.reproductive_rate = 6.5
    # def bird_flu(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .6
    #     self.reproductive_rate = 1
    # def bubonic_plague(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .6
    #     self.reproductive_rate = 1
    # def c_difficile(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .24
    #     self.reproductive_rate = 1.25
    # def camplobacter(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .012
    #     self.reproductive_rate = .19
    # def chicken_pox(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = 0
    #     self.reproductive_rate = 8.5
    # def cholera(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .0163
    #     self.reproductive_rate = 2.13
    # def dengue_fever(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .05
    #     self.reproductive_rate = 3
    # def diphtheria(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .075
    #     self.reproductive_rate = 6.5
    # def e_coli(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .04
    #     self.reproductive_rate = 1.15
    # def ebola(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .5
    #     self.reproductive_rate = 2.5
    # def enterovirus(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .0006
    #     self.reproductive_rate = 3.5
    # def hepatitus_b(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .0075
    #     self.reproductive_rate = 4.04
    # def hiv(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .8
    #     self.reproductive_rate = 3.5
    # def influenza(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .025
    #     self.reproductive_rate = 3
    # def lyme_disease(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .002
    #     self.reproductive_rate = 4.4
    # def malaria_p_falciparum(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .005
    #     self.reproductive_rate = 80
    # def malaria_p_malariae(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .005
    #     self.reproductive_rate = 16
    # def measles(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .003
    #     self.reproductive_rate = 15
    # def mers(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .45
    #     self.reproductive_rate = .5
    # def mrsa(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .2
    #     self.reproductive_rate = 1.63
    # def mumps(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .01
    #     self.reproductive_rate = 12.5
    # def norovirus(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = .0001
    #     self.reproductive_rate = 2
    # def pertussis(self, mortality_rate, reproductive_rate):
    #     self.mortality_rate = 
    #     self.reproductive_rate = 
