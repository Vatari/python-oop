class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []
        self.result = {}

    def add_pokemon(self, pokemon):
        if pokemon.name in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon.name)
        self.result[pokemon.name] = pokemon.health
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            del self.result[pokemon_name]
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self, final_output=None):
        final_output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for name, health in self.result.items():
            final_output += f"\n- {name} with health {health}"
        return final_output
