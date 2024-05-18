import random

class Agent:
    def __init__(self, id):
        self.id = id
        self.location = None
    def move(self, new_location):
        self.location = new_location
class World:
    def __init__(self, grid_size, num_agents):
        self.grid_size = grid_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.agents = [Agent(i) for i in range(num_agents)]
        self.init_world()
    def init_world(self):
        positions = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size)]
        random.shuffle(positions)
        for agent in self.agents:
            if positions:
                location = positions.pop()
                self.grid[location[0]][location[1]] = agent
                agent.location = location
    def find_empty_patch(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] is None:
                    return (i, j)
        return None
    def run_simulation(self, num_steps=10):
        for _ in range(num_steps):
            for agent in self.agents:
                new_location = self.find_empty_patch()
                if new_location:
                    self.grid[agent.location[0]][agent.location[1]] = None
                    self.grid[new_location[0]][new_location[1]] = agent
                    agent.move(new_location)
def main():
    world = World(grid_size=5, num_agents=5)
    world.run_simulation(num_steps=10)
if __name__ == '__main__':
    main()