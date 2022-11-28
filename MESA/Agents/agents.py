import mesa


class Car(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        self.move()
    
    def move(self):
        #pos_adj = self.model.grid.get_neighborhood(
        #   self.pos,
        #    moore = True,     
        #    include_center = False
        #)
        #print(self.pos,pos_adj)
        #val = [i for i in pos_adj if i not in neighbors]
        new_position = (self.pos[0], (self.pos[1]+1)%self.model.grid.height)
        if(self.model.grid.is_cell_empty(new_position)):
            self.model.grid.move_agent(self, new_position)
        
        #print(self.pos)

        
class Inteseccion(mesa.Model):
    def __init__(self, N, width, height):
        #print(width)
        #print(height)
        self.num_agents = N
        self.grid = mesa.space.SingleGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        for i in range(self.num_agents):
            a = Car(i, self)
            self.schedule.add(a)
            self.grid.position_agent(a, "random", "random")
        
    def step(self):
        self.schedule.step()