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
    grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 14, 500, 504)
    server = mesa.visualization.ModularServer(
        Inteseccion, [grid], "Rotonda", {"N":20, "width":10, "height":14}
    )
    server.port = 8522
    server.launch()
    
if __name__ == "__main__":
    main()