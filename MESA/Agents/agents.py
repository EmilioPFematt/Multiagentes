import mesa


class Car(mesa.Agent):
    def __init__(self, unique_id, model, exits):
        super().__init__(unique_id, model)
        self.exit = self.random.choice(exits)
        
    
    def step(self):
        self.move()
    
    def move(self):
        if(self.pos[1] == self.exit):
            new_position = (self.pos[0]+1, self.pos[1])
            if(new_position[0] < self.model.grid.width and self.model.grid.is_cell_empty(new_position)):
                self.model.grid.move_agent(self, new_position)
            elif new_position[0] < self.model.grid.width :
                self.model.grid.move_agent(self, new_position)
        elif self.pos[0] > 1 :
            new_position = (self.pos[0]-1, self.pos[1])
            if(self.model.grid.is_cell_empty(new_position)): 
                self.model.grid.move_agent(self, new_position)
        else :       
            new_position = (self.pos[0], (self.pos[1]+1)%self.model.grid.height)
            if(self.model.grid.is_cell_empty(new_position)): 
                self.model.grid.move_agent(self, new_position)

class Inteseccion(mesa.Model):
    def __init__(self, N, width, height):
        #print(width)
        #print(height)
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        exits = [1, 5, 9, 13]
        ins = [3, 7, 11, 15]
        av_pos2 = []
        for i in range(height):
            av_pos2.append([i for i in range(2, width)])

        for i in range(self.num_agents):
            a = Car(i, self, exits)
            self.schedule.add(a)
            y = a.random.choice(ins)
            while(len(av_pos2[y]) == 0):
                y = a.random.choice(ins)
            self.grid.place_agent(a, (a.random.choice(av_pos2[y]), y))
            av_pos2[y].remove(a.pos[0])
        
    def step(self):
        self.schedule.step()
