import itertools
import math
import random
import matplotlib.pyplot as plt


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        return math.hypot(self.x - city.x, self.y - city.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

def generate_cities(size):
    return [City(x=int(random.random() * 1000), y=int(random.random() * 1000)) for _ in range(size)]

def path_cost(route):
    return sum([city.distance(route[index - 1]) for index, city in enumerate(route)])


def visualize_tsp(title, cities):
    fig = plt.figure()
    fig.suptitle(title)
    x_list, y_list = [], []
    for city in cities:
        x_list.append(city.x)
        y_list.append(city.y)
    x_list.append(cities[0].x)
    y_list.append(cities[0].y)

    plt.plot(x_list, y_list, 'ro')
    plt.plot(x_list, y_list, 'g')
    plt.show(block=True)


class BruteForce:
    def __init__(self, cities):
        self.cities = cities

    def run(self):
        self.cities = min(itertools.permutations(self.cities), key=lambda path: path_cost(path))
        return path_cost(self.cities)



class SimAnneal(object):
    def __init__(self, cities, temperature=-1, alpha=-1, stopping_temperature=-1, stopping_iter=-1):
        self.cities = cities
        self.num_cities = len(cities)
        self.temperature = math.sqrt(self.num_cities) if temperature == -1 else temperature
        self.T_save = self.temperature
        self.alpha = 0.999 if alpha == -1 else alpha
        self.stopping_temperature = 1e-8 if stopping_temperature == -1 else stopping_temperature
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1
        self.route = None
        self.best_fitness = float("Inf")
        self.progress = []
        self.cur_cost = None

    def greedy_solution(self):
        start_node = random.randint(0, self.num_cities)  # стартуем с рандомной ноды
        unvisited = self.cities[:]
        del unvisited[start_node]
        route = [cities[start_node]]
        while len(unvisited):
            index, nearest_city = min(enumerate(unvisited), key=lambda item: item[1].distance(route[-1]))
            route.append(nearest_city)
            del unvisited[index]
        current_cost = path_cost(route)
        self.progress.append(current_cost)
        return route, current_cost

    def accept_probability(self, candidate_fitness):
        return math.exp(-abs(candidate_fitness - self.cur_cost) / self.temperature)

    def accept(self, guess):
        guess_cost = path_cost(guess)
        if guess_cost < self.cur_cost:
            self.cur_cost, self.route = guess_cost, guess
            if guess_cost < self.best_fitness:
                self.best_fitness, self.route = guess_cost, guess
        else:
            if random.random() < self.accept_probability(guess_cost):
                self.cur_cost, self.route = guess_cost, guess

    def run(self):
        self.route, self.cur_cost = self.greedy_solution()
        while self.temperature >= self.stopping_temperature and self.iteration < self.stopping_iter:
            guess = list(self.route)
            left_index = random.randint(2, self.num_cities - 1)
            right_index = random.randint(0, self.num_cities - left_index)
            guess[right_index: (right_index + left_index)] = reversed(guess[right_index: (right_index + left_index)])
            self.accept(guess)
            self.temperature *= self.alpha
            self.iteration += 1
            self.progress.append(self.cur_cost)

        print("Идеальное полученное расстояние", self.best_fitness)

    def visualize_routes(self):
        visualize_tsp('Имитация отжига при решение задачи Комивояжера', self.route)

    def plot_learning(self):
        fig = plt.figure(1)
        plt.plot([i for i in range(len(self.progress))], self.progress)
        plt.ylabel("Дистанция")
        plt.xlabel("Итерации")
        plt.show(block=False)


if __name__ == "__main__":
    inputType=int(input("Выберите метод вычисления задачи Комивояжера\n1. Метод полного перебора\n2. Метод имитаци отжига\n0. Выход\n"))
    if inputType==1:
        city_count=8
        print(f"Вычисляем растояние между {city_count} городами")
        brute = BruteForce(generate_cities(city_count))
        print(brute.run())
        visualize_tsp('Длина пути по графу методом полного перебора ', brute.cities)
    elif inputType==2:
        print("Метод имитаци отжига")
        cities = generate_cities(64)
        sa = SimAnneal(cities, stopping_iter=14000)
        sa.run()
        sa.plot_learning()
        sa.visualize_routes()
    else:
        print("Выходим")
    
    print("Программа закрывается")
