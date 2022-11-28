from Agents.agents import Inteseccion
import mesa
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

def main():
    #model = Inteseccion(5, 1, 10)
    #for i in range(5):
    #    model.step()
    grid = mesa.visualization.CanvasGrid(agent_portrayal, 1, 10, 50, 500)
    server = mesa.visualization.ModularServer(
        Inteseccion, [grid], "Rotonda", {"N":6, "width":1, "height":10}
    )
    server.port = 8522
    server.launch()
    
if __name__ == "__main__":
    main()