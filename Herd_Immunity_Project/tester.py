# Used with permission of Mintri1199. 
# https://github.com/Mintri1199/
# Was attempting to convert to Pytest version but ran out of time -RW

import pytest
import random
random.seed(42)
from virus import Virus
from person import Person
from simulation import Simulation
import unittest

########## PERSON TEST ##########:
class PersonTest(unittest.TestCase):
    # Set up the virus objects for tests
    def setUp(self):
        self.weak_virus = Virus("Weak", 0, 0)
        self.deadly_virus = Virus("Deadly", 0.99, 0.99)


    # Checking the instantiation of person object with virus
    def test_person_instantiation(self):
        new_person = Person(1, False, self.weak_virus)
        assert new_person.infected is self.weak_virus
        assert new_person.is_alive is True
        assert new_person._id is 1
        assert new_person.is_vaccinated is False

    # Check two cases of person objects
    def test_did_survive_method(self):
        dying_person = Person(1, False, self.deadly_virus)
        healthy_person = Person(2, False, self.weak_virus)

        assert dying_person.did_survive_infection() is False
        assert dying_person.is_alive is False
        assert dying_person.infected is not None

        assert healthy_person.did_survive_infection() is True
        assert healthy_person.is_alive is True
        assert healthy_person.infected is None


# PYTEST
# weak_virus = Virus("Huggles", 0.1, 0.1)
# strong_virus = Virus("Death Curse", 1, 1)

# def test_person_init():
#     new_person = Person(1, False, weak_virus)
#     assert new_person._id == 1
#     assert new_person.is_vaccinated == False
#     assert new_person.infected == weak_virus
#     assert new_person.is_alive == True

# def test_did_survive():
#     dead_person_bwahaha = Person(1, False, strong_virus)
#     healthy_person = Person(2, False, weak_virus)

#     assert dead_person_bwahaha.did_survive_infected() == False
#     assert dead_person_bwahaha.is_alive == False
#     assert dead_person_bwahaha.infected != None

#     assert healthy_person.did_survive_infected == True
#     assert healthy_person.is_alive == True
#     assert healthy_person.infected == None


# ########## VIRUS TEST ########## 
def test_virus():
    anthrax = Virus("anthrax", .2, 6.5)
    assert anthrax.name == "anthrax"
    assert anthrax.mortality_rate == .2
    assert anthrax.reproductive_rate == 6.5

# ########## LOGGER TEST ##########
# # TODO

# ########## SIMULATION TEST ##########
class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.new_sim = Simulation(10000, 0.25, "Ebola", 0.5, 0.25, 100)
        self.smaller_sim = Simulation(10, 0.25, "Ebola", 0.5, 0.25, 5)

    def test_create_population_method(self):
        infected_count = 0

        self.new_sim._create_population()
        assert len(self.new_sim.population) == 10000

        for person in self.new_sim.population:
            if person.infected is not None:
                infected_count += 1

        assert infected_count == 100

    def test_should_continue_method(self):
        self.new_sim._create_population()
        assert self.new_sim._simulation_should_continue() is True

    def test_should_continue_method_deaths_case(self):
        self.new_sim._create_population()

        for person in self.new_sim.population:
            person.is_alive = False
        assert self.new_sim._simulation_should_continue() is False

    def test_should_continue_method_cure_case(self):
        self.new_sim._create_population()

        for person in self.new_sim.population:
            person.is_alive = True
            person.infected = None
            person.is_vaccinated = True
        assert self.new_sim._simulation_should_continue() is False

    def test_newly_infected_method_empty_list(self):
        self.new_sim._create_population()
        self.new_sim.newly_infected = [10000, 9999, 9998, 9997]
        self.new_sim._infect_newly_infected()
        assert len(self.new_sim.newly_infected) == 0

    def test_newly_infected_method(self):
        list = [10000, 9999, 9998, 9997]
        self.new_sim.newly_infected = list
        self.new_sim._infect_newly_infected()
        for id in list:
            for person in self.new_sim.population:
                if person._id == id:
                    assert person.infected is not None

    def test_unique_interaction(self):
        self.smaller_sim._create_population()
        number_of_interaction = 1
        for person in self.smaller_sim.population:
            while number_of_interaction <= 100:
                rando = random.choice(self.smaller_sim.population)
                # Prevent interaction with dead corpse and with it self
                while rando.is_alive is False or rando._id == person._id:
                    rando = random.choice(self.smaller_sim.population)
                assert person._id is not rando._id
                assert rando.is_alive is True
                self.smaller_sim.interaction(person, rando)
                number_of_interaction += 1
            number_of_interaction = 1


# # PYTEST
# danceoff_world = Simulation(100000, .01, "Dancing disease", .2, .5, 100)
# rapbattle_world = Simulation(100, .25, "Rap Battle disease", .5, .25, 1)

# def test_create_population():
#     infected_count = 0

#     danceoff_world._create_population()
#     assert len(danceoff_world.population) == 100000

#     for person in danceoff_world.population:
#         if person.infected != None:
#             infected_count += 1
#     assert infected_count == 100