class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_workers = sum([w.salary for w in self.workers])
        if self.__budget >= total_salary_workers:
            self.__budget -= total_salary_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum([a.money_for_care for a in self.animals])
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__find_entity_str(self.animals, 'Lion')
        result += self.__find_entity_str(self.animals, 'Tiger')
        result += self.__find_entity_str(self.animals, 'Cheetah')
        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__find_entity_str(self.workers, 'Keeper')
        result += self.__find_entity_str(self.workers, 'Caretaker')
        result += self.__find_entity_str(self.workers, 'Vet')
        return result.strip()

    @staticmethod
    def __find_entity_str( entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result
