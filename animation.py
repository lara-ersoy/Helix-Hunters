import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def random_folding(length):
    """
    Genereert een willekeurige vouwing van een eiwit in 3D.
    """
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    position = np.array([0, 0, 0])
    path = [position]

    for _ in range(length - 1):
        new_dir = random.choice(directions)
        new_pos = position + np.array(new_dir)
        
        while any(np.array_equal(new_pos, p) for p in path):  # Voorkomt overlap
            new_dir = random.choice(directions)
            new_pos = position + np.array(new_dir)

        path.append(new_pos)
        position = new_pos

    return np.array(path)

def animate_folding(path):
    """
    Maakt een 3D-animatie van het vouwproces met betere zoom en schaal.
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Automatische limieten instellen op basis van min/max van de eiwitvouwing
    x_min, y_min, z_min = np.min(path, axis=0)
    x_max, y_max, z_max = np.max(path, axis=0)
    padding = 2  # Extra ruimte rondom de vouwing

    ax.set_xlim([x_min - padding, x_max + padding])
    ax.set_ylim([y_min - padding, y_max + padding])
    ax.set_zlim([z_min - padding, z_max + padding])

    ax.set_xlabel('X-as')
    ax.set_ylabel('Y-as')
    ax.set_zlabel('Z-as')
    ax.set_title("3D Eiwit Vouwing Animatie (Ingezoomd)")

    # Verbeterde visualisatie
    line, = ax.plot([], [], [], 'o-', markersize=10, linewidth=3, color='b', alpha=0.8)

    def update(frame):
        xdata = path[:frame+1, 0]
        ydata = path[:frame+1, 1]
        zdata = path[:frame+1, 2]
        line.set_data(xdata, ydata)
        line.set_3d_properties(zdata)
        return line,

    ani = FuncAnimation(fig, update, frames=len(path), interval=400, repeat=False)

    plt.show()

if __name__ == "__main__":
    protein_length = 20  # Lengte van het eiwit
    folding_path = random_folding(protein_length)
    animate_folding(folding_path)
