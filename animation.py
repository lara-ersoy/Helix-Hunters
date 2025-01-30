import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def random_folding(length):
    """
    Genereert een willekeurige vouwing van een eiwit in 3D met 'H', 'C' en 'P' labels.
    """
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    position = np.array([0, 0, 0])
    path = [position]

    # Random genereren van aminozuurtypes (H, C, P)
    amino_types = random.choices(['H', 'C', 'P'], k=length)

    for _ in range(length - 1):
        new_dir = random.choice(directions)
        new_pos = position + np.array(new_dir)

        # Zorg ervoor dat er geen overlap is
        while any(np.array_equal(new_pos, p) for p in path):
            new_dir = random.choice(directions)
            new_pos = position + np.array(new_dir)

        path.append(new_pos)
        position = new_pos

    return np.array(path), amino_types

def animate_folding(path, amino_types, save_as="protein_folding.gif"):
    """
    Maakt een 3D-animatie van het vouwproces en slaat deze op als een GIF zonder FFmpeg.
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
    ax.set_title("3D Eiwit Vouwing Animatie")

    # Donkeroranje lijn voor de vouwing
    line, = ax.plot([], [], [], color='darkorange', linewidth=3, alpha=0.9)

    # Oranje bolletjes voor aminozuren
    scatter = ax.scatter([], [], [], color='orange', s=100, edgecolors='black', zorder=3)

    # Labels voor aminozuren (horizontaal geplaatst)
    labels = [ax.text(0, 0, 0, "", fontsize=12, color="black", horizontalalignment='center') for _ in range(len(path))]

    def update(frame):
        xdata = path[:frame+1, 0]
        ydata = path[:frame+1, 1]
        zdata = path[:frame+1, 2]

        line.set_data(xdata, ydata)
        line.set_3d_properties(zdata)

        scatter._offsets3d = (xdata, ydata, zdata)

        for i in range(frame+1):
            labels[i].set_position((xdata[i], ydata[i]))
            labels[i].set_3d_properties(zdata[i])
            labels[i].set_text(amino_types[i])

        return line, scatter, *labels

    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=400, repeat=False)

    # Opslaan als GIF zonder FFmpeg
    ani.save(save_as, writer="pillow", fps=5)

    print(f"✅ Animatie opgeslagen als: {save_as}")

    plt.show()

if __name__ == "__main__":
    protein_length = 20  # Lengte van het eiwit
    folding_path, amino_types = random_folding(protein_length)

    # Opslaan als GIF zonder FFmpeg
    animate_folding(folding_path, amino_types, save_as="protein_folding.gif")
