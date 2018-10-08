import pytest
# import person
from virus import Virus
# import logger as Logger
# import simulation as Simulation

########## PERSON TEST ##########

########## VIRUS TEST ########## 
def test_virus():
    anthrax = Virus(.2, 6.5, "anthrax")
    assert anthrax.name == "anthrax"
    assert anthrax.mortality_rate == .2
    assert anthrax.reproductive_rate == 6.5
    return anthrax
    
# test_virus()
# print(test_virus)
# print(anthrax.mortality_rate)
# print(test_virus.reproductive_rate)


########## LOGGER TEST ##########
########## SIMULATION TEST ##########