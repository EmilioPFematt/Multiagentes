import mesa

class Car(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        self.move()
    
    def move(self):
        pos_adj = self.model.grid.get_neighborhood(
            self.pos,
            moore = False,
            include_center = False
        )
        neighbors = [i.pos for i in self.model.grid.get_neighbors(self.pos, False)]
        val = [i for i in pos_adj if i not in neighbors]
        new_position = self.pos
        if(len(val) != 0):
            new_position = self.random.choice(val)
        self.model.grid.move_agent(self, new_position)

class Inteseccion(mesa.Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = mesa.space.Grid(width, height, False)
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(self.num_agents):
            a = Car(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (self.random.randrange(width), self.random.randrange(height)))
        
    def step(self):
        self.schedule.step()