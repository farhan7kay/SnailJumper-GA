import copy
import math
import os
import random
import numpy as np
import pandas as pd
from player import Player

class Evolution:
    def __init__(self):
        self.fitness_max = []
        self.fitness_avg = []
        self.fitness_min = []
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # players.sort(key=lambda x: x.fitness, reverse=True)
                
        # TODO (Additional: Implement roulette wheel here)
        next_population = self.roulette_wheel(players, num_players)
        
        # TODO (Additional: Implement SUS here)
        # next_population = self.sus_selector(players, num_players)

        # TODO (Additional: Learning curve)
        fitness_arr = [x.fitness for x in players]
        self.fitness_max.append(max(fitness_arr))
        self.fitness_avg.append(sum(fitness_arr) / len(fitness_arr))
        self.fitness_min.append(min(fitness_arr))

        df = pd.DataFrame(
            {'max': self.fitness_max, 'min': self.fitness_min, 'avg': self.fitness_avg})

        df.to_csv('a.csv')
        
        return next_population
        # return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
          
            parents = self.sus_selector(prev_players, num_players)
            random.shuffle(parents)
            children = []
            for i in range(0, len(parents), 2) :
                children += self.next_generation(parents[i], parents[i+1])
            return children

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
    
    def roulette_wheel(self, players, num_players):
        next_population = []
        population_fitness = sum([player.fitness for player in players])
        probability = [player.fitness /
                       population_fitness for player in players]
        next_population = np.random.choice(
            players, size=num_players, p=probability, replace=False)
        return list(next_population)

    def q_tournament(self, x, num, q= 2) :
        next_population = []
        for i in range(num) :
            rnd = round(np.random.random() * (len(x)-1))
            max = x[rnd]
            for j in range(q - 1) :
                rnd = round(np.random.random() * (len(x)-1))
                temp = x[rnd]
                if temp.fitness > max.fitness :
                    max = temp
            next_population.append(max)
        return next_population

    def sus_selector(self, players, num_players):
        probas_num = []
        sum_fitness = 0
        for player in players:
            sum_fitness += player.fitness
        for player in players:
            probas_num.append(player.fitness / sum_fitness)
        for i in range(1, len(players)):
            probas_num[i] += probas_num[i - 1]

        random_number = np.random.uniform(0, 1 / num_players, 1)
        step = (probas_num[len(probas_num) - 1] - random_number) / num_players
        
        next_population = []
        for i in range(num_players):
            now = (i + 1) * step
            for i, proba in enumerate(probas_num):
                if now <= proba:
                    next_population.append(self.clone_player(players[i]))
                    break
        return next_population

    def next_generation(self, parent_1, parent_2):
        children = []

        clone_child_1 = self.clone_player(parent_1)
        clone_child_2 = self.clone_player(parent_2)

        clone_child_1.nn.w1 ,  clone_child_2.nn.w1 = self.crossover(parent_1.nn.w1 , parent_2.nn.w1)
        clone_child_1.nn.w2 , clone_child_2.nn.w2  = self.crossover(parent_1.nn.w2, parent_2.nn.w2)
        clone_child_1.nn.b1, clone_child_2.nn.b1 = self.crossover(parent_1.nn.b1, parent_2.nn.b1)
        clone_child_1.nn.b2, clone_child_2.nn.b2 = self.crossover(parent_1.nn.b2, parent_2.nn.b2)

        clone_child_1 = self.mutation(clone_child_1)
        clone_child_2 = self.mutation(clone_child_2)
        children.append(clone_child_1)
        children.append(clone_child_2)

        # new_players.sort(key=lambda x: x.fitness, reverse=True)
        # new_players = new_players[: num_players]
        return children
    
    def crossover(self , array1 , array2):
        crossover_place = math.floor(array1.shape[0]/2)
        random_number = np.random.uniform(0, 1, 1)
        crossover_probability = 0.8
        if(random_number > crossover_probability):      
            return array1 , array2
        else:
            return np.concatenate((array1[:crossover_place], array2[crossover_place:]), axis=0), np.concatenate((array2[:crossover_place], array1[crossover_place:]), axis=0)


    def mutation(self , chromosome):
        mutate_probability = 0.5

        random_number = np.random.uniform(0, 1, 1)
        if(random_number <= mutate_probability) :

            chromosome.nn.w1 += np.random.normal(0,0.3,size=chromosome.nn.w1.shape)
            chromosome.nn.w2 += np.random.normal(0,0.3,size=chromosome.nn.w2.shape)

            chromosome.nn.b1 += np.random.normal(0, 0.3, size=chromosome.nn.b1.shape)
            chromosome.nn.b2 += np.random.normal(0, 0.3, size=chromosome.nn.b2.shape)

        return chromosome
