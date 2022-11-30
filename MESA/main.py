from Agents.agents import Inteseccion

def main():
    model = Inteseccion(5, 1, 10)
    print([x.pos for x in model.schedule.agents])
    for i in range(10):
        model.step()
        print([x.pos for x in model.schedule.agents])

if __name__ == "__main__":
    main()