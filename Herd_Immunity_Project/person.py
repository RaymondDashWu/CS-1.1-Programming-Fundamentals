import random
random.seed(42)

class Person(object):    
    def __init__(self, _id, is_vaccinated = bool, infected = object):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def did_survive_infection(self):
        if self.is_vaccinated == False and self.infected == None:
            return None
        if self.infected != None:
            if random.random() >= self.infected.mortality_rate:
                self.is_vaccinated = True
                self.infected = None
                return True
            else:
                self.is_alive = False
                return False
        else:
            return True