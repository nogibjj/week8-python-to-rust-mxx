import resource
import random
import time
from heapq import heappush, heappop


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        if isinstance(other, Fruit):
            if self.name == "Fig" and other.name != "Fig":
                return False
            elif self.name != "Fig" and other.name == "Fig":
                return True
            else:
                return self.name < other.name

    def __repr__(self):
        return self.name


def generate_fruit_salad():
    fruits = ["Apple", "Orange", "Pear", "Peach", "Banana", "Fig", "Fig", "Fig", "Fig"]
    fruit_salad = []

    figs_count = 0
    while figs_count < 2:
        fruit = random.choice(fruits)
        if fruit == "Fig":
            figs_count += 1
            heappush(fruit_salad, Fruit("Fig"))
        else:
            heappush(fruit_salad, Fruit(fruit))

    return fruit_salad


if __name__ == "__main__":
    start_time = time.time()

    fruit_salad = generate_fruit_salad()
    print("Random Fruit Salad With Two Servings of Figs:")
    while fruit_salad:
        print(heappop(fruit_salad))

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    # Resource usage
    print("Resource usage:")
    print(resource.getrusage(resource.RUSAGE_SELF))
