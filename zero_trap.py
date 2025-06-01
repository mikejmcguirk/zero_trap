import random


def create_origin():
    while True:
        origin = [random.choice([0, 1]) for _ in range(str_len)]
        if sum(origin) > 0:
            return origin


def get_fitness(a):
    total_ones = sum(a)
    if total_ones == 0:
        return len(a) + 1

    return total_ones


def get_winners(population, cnt_pop):
    winners = []
    while len(population) >= 2:
        random.shuffle(population)

        a, b = population[0], population[1]

        if get_fitness(a) >= get_fitness(b):
            winners.append(a)
        else:
            winners.append(b)

        population.remove(a)
        population.remove(b)

    return winners


def get_new_population(winners, cnt_pop):
    new_population = []
    winners.sort(key=get_fitness, reverse=True)
    elite = winners[0]
    new_population.append(elite)

    while len(new_population) < cnt_pop:
        scores = [get_fitness(w) for w in winners]
        a = random.choices(winners, weights=scores, k=1)[0]

        candidates = [b for b in winners if b is not a]
        other_scores = [get_fitness(c) for c in candidates]

        if sum(other_scores) > 0:
            b = random.choices(candidates, weights=other_scores, k=1)[0]
        else:
            b = random.choice(candidates)

        point = random.randint(1, str_len - 1)
        ab = a[:point] + b[point:]
        new_population.append(ab)

    return new_population


str_len = 50
cnt_pop = 100
population = [create_origin() for _ in range(cnt_pop)]
generations = 1000
min_mutation = 0.01
max_mutation = 0.5

iter = 0
for _ in range(generations):
    iter += 1

    winners = get_winners(population, cnt_pop)
    assert len(winners) == cnt_pop / 2

    new_population = get_new_population(winners, cnt_pop)
    assert len(new_population) == cnt_pop, len(new_population)

    seen = set()
    for i in range(len(new_population)):
        str_tuple = tuple(new_population[i])
        if str_tuple in seen:
            for j in range(0, len(new_population[i])):
                new_population[i][j] = 1 - new_population[i][j]
        else:
            seen.add(str_tuple)

    new_population.sort(key=get_fitness, reverse=True)
    best_fitness = get_fitness(new_population[0])

    for i in range(1, len(new_population)):
        this_fitness = get_fitness(new_population[i])
        this_pct = this_fitness / best_fitness
        to_subtract = this_pct * (max_mutation - min_mutation)
        mutation_rate = max_mutation - to_subtract

        for j in range(0, len(new_population[i])):
            do_mutation = random.random()
            if do_mutation > mutation_rate:
                continue

            new_population[i][j] = 1 - new_population[i][j]

    population = new_population
    population.sort(key=get_fitness, reverse=True)
    if get_fitness(population[0]) == str_len + 1:
        break


print("Complete on iter: ", iter)
max_score = max(population, key=lambda x: get_fitness(x))
print("Max Score: ", max_score)
