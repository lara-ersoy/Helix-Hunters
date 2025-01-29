import numpy as np
import pandas as pd

# Parameters
num_residues = 10  # Number of amino acids in the chain
num_frames = 50    # Number of animation frames (time steps)

# Initialize an unfolded protein as a straight line in 3D space
x = np.linspace(0, num_residues-1, num_residues)
y = np.zeros(num_residues)
z = np.zeros(num_residues)

# Store all frames
frames = []

# Simulate folding over time
for frame in range(num_frames):
    # Apply a random bending effect to simulate folding
    y = np.sin(x * np.pi * (1 - frame / num_frames)) * (1 - frame / num_frames)
    z = np.cos(x * np.pi * (1 - frame / num_frames)) * (1 - frame / num_frames)
    
    # Save frame data
    for i in range(num_residues):
        frames.append([frame, i, x[i], y[i], z[i]])

# Convert to DataFrame
df = pd.DataFrame(frames, columns=["Frame", "Residue", "X", "Y", "Z"])

# Save to CSV
df.to_csv("protein_folding.csv", index=False)

print("Protein folding simulation saved to 'protein_folding.csv'")
