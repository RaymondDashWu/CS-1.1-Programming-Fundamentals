import random, sys
import logging
random.seed(42)
from person import Person
from logger import *
from virus import Virus

class Simulation(object):
    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.initial_infected = initial_infected
        self.next_person_id = 0
        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.vacc_percentage = vacc_percentage
        self.total_dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        # self.logger = logging.basicConfig(filename = "logger.log", level = logging.INFO, format = "%(asctime)s: %(message)s")
        self.logger = Logger(self.file_name)
        self.newly_infected = []
        # self.population = self._create_population(initial_infected)

    def _create_population(self):
        infected_count = 0
        while len(self.population) != self.population_size:
            if infected_count != self.initial_infected:
                self.population.append(Person(self.next_person_id, is_vaccinated = False, infected = self.virus))
                infected_count += 1
            # if random.random() > self.vacc_percentage:
            #     population.append(Person(self.next_person_id, infected = True))
            #     infected_count += 1
            else:
                self.population.append(Person(self.next_person_id, is_vaccinated = False, infected = None))
                
                # if random.random() < self.vacc_percentage:
                #     self.population.append(Person(self.next_person_id, is_vaccinated = True, infected = None))
                # elif random.random() >= self.vacc_percentage:
                #     self.population.append(Person(self.next_person_id, is_vaccinated = False, infected = None))
            self.next_person_id += 1
        self.current_infected = infected_count
        # self.population = population

    def _simulation_should_continue(self):
        # check for deaths and infected population
        self.current_infected = 0
        death_counter = 0
        
        for i in self.population:
            if i.is_alive == False:
                death_counter += 1

        for i in self.population:
            if i.infected is not None and i.is_alive == True:
                self.current_infected += 1

        # self.total_infected = self.current_infected
        print(self.current_infected)
        print("death counter line 66 " + str(death_counter))
        if len(self.population) - death_counter == 1:
            print("Everyone except Vincent Price has died. He is the last man on earth.")
            return False
        if death_counter == len(self.population):
            print("The virus " + self.virus_name + " has wiped out the entire planet. ")
            return False
        if self.current_infected == 0:
            print("The virus " + self.virus_name + " has stopped spreading. There are a total of " + str(len(self.population) - death_counter) + " people alive.")
            return False
        else:
            #print("TESTING *** currently infected: " + str(self.current_infected))
            # print("TESTING *** population remaining: " + str(len(self.population) - death_counter))
            return True

        # if len(population) != pop_size:
        #     return True
        # elif infected_count = len(population):
        #     print("The entire world has been infected with {}!".format(virus_name))
        #     return False
        # elif infected_:
        # else:
        #     simulation = False
        #     break

    def run(self):
        new = 0
        time_step_counter = 0
        self._create_population()
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            
            for person in self.population:
                self.logger.log_infection_survival(person, person.did_survive_infection())
            print(self.current_infected)
            self._infect_newly_infected()
            for person in self.population:
                if person.is_alive and person.infected is not None:
                    new +=1
            print(new)

            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        print(self.current_infected)
        print("The simulation has ended after " + str(time_step_counter) + " turns.")

    def time_step(self):
        turn_count = 1
        for person in self.population:
            if person.is_alive == True:
                while turn_count <= 100:
                    random_selection = random.choice(self.population)
                    while random_selection.is_alive == False or random_selection._id == person._id:
                        random_selection = random.choice(self.population)
                    self.interaction(person, random_selection)
                    turn_count += 1
                turn_count = 1
            else:
                pass

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person, did_infect = False, person2_vacc = True, person2_sick = False)
        elif random_person.infected == True:
            self.logger.log_interaction(person, random_person, did_infect = True, person2_vacc = False, person2_sick = False)
        elif random_person.is_alive == True and random_person.is_vaccinated == False:
            if random.random() < self.basic_repro_num:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, did_infect = True, person2_vacc = False, person2_sick = False)
            else:
                self.logger.log_interaction(person, random_person, did_infect = False, person2_vacc = False, person2_sick = False)
        else:
            print("Scenario I didn't think of. Line 249")

    def _infect_newly_infected(self):
        for id in self.newly_infected:
            for person in self.population:
                if id == person._id:
                    person.infected = self.virus
        self.newly_infected.clear()

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()

# simulation_test = Simulation(1000, .5, "C. Difficile", .7, .25, 100)
# simulation_test.run()