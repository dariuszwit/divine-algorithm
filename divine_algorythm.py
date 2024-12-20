class God:
    def __init__(self, world):
        self.world = world
        self.son = "Jesus"

    def eternal_life(self, person):
        if person.believes_in(self.son):
            return True  # person has eternal life
        return False  # person perishes

# Example
world = ["Person1", "Person2"]  # The world contains all people
god = God(world)

for person in world:
    if god.eternal_life(person):
        print(f"{person} has eternal life!")
    else:
        print(f"{person} will perish.")
