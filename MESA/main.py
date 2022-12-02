from .Agents.agents import Inteseccion
import mesa
import math
#import matplotlib.pyplot as plot

def conv_x(x, d):
    #print(x, d)
    return (x+1)*math.cos(math.radians(d*22.5 % 360))

def conv_y(x, d):
    #print(x, d)
    return (x+1)*math.sin(math.radians(d*22.5 % 360))

def agent_portrayal(agent, shape = "circle", color = "red", filled = True, size = 0.3):
    colors = ["red", "blue", "green"]
    portrayal = {
        "Shape":shape,
        "Color":colors[agent.unique_id%3],
        "Filled":filled,
        "Layer":0,
        "r":size
    }
    return portrayal

def generate_data(N = 5, width = 10, height = 16):
    model = Inteseccion(N, width, height)
    data = []
    agents = []
    while True :
        new_agents = []
        for i in range(len(model.schedule.agents)):
            x = model.schedule.agents[i].pos[0]
            y = model.schedule.agents[i].pos[1]
            new_agents.append({'id':i, 'x':conv_x(x, y), 'y':conv_y(x, y)})
        if new_agents == agents :
            break
        else :
            for i in new_agents:
                data.append(i)
            agents = new_agents
            model.step()
    #print(data)
    return data


def main():
    grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 16, 500, 512)
    server = mesa.visualization.ModularServer(
        Inteseccion, [grid], "Rotonda", {"N":5, "width":10, "height":16}
    )
    server.port = 8522
    server.launch()
    
if __name__ == "__main__":
    #generate_data()
    main()