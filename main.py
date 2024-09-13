import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to read the TSV and extract relevant data
def read_tsv(file_path):
    try:
        # Reading the file, skipping metadata
        data = pd.read_csv(file_path, delimiter='\t', skiprows=12, low_memory=False)  # Skipping metadata rows

        # Skipping every 10th row
        data = data.iloc[::10].reset_index(drop=True)

        # Displaying the columns for debugging purposes
        print("Columns in the dataset:")
        print(data.columns)

        return data
    except pd.errors.EmptyDataError as e:
        print(f"Error reading the TSV file: {e}")
        return None

# Function to plot data for multiple markers and BlueROV positions
def plot_data(data, max_points=3000):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Limit the number of points to plot
    data = data.head(max_points)

    # Define marker column intervals
    marker_intervals = [(30, 31, 32), (34, 35, 36), (38, 39, 40), (42, 43, 44),
                        (46, 47, 48), (50, 51, 52), (54, 55, 56), (58, 59, 60),
                        (62, 63, 64), (66, 67, 68), (70, 71, 72), (74, 75, 76),
                        (78, 79, 80), (82, 83, 84)]

    # Reduce density of points by selecting every nth point (e.g., every 200th point)
    interval = 50
    data_interval = data.iloc[::interval].reset_index(drop=True)

    # Plot each marker's data in yellow
    for x_col, y_col, z_col in marker_intervals:
        x_data = data_interval.iloc[:, x_col]
        y_data = data_interval.iloc[:, y_col]
        z_data = data_interval.iloc[:, z_col]

        # Plotting each marker's data
        ax.scatter(x_data, y_data, z_data, label=f'Marker {marker_intervals.index((x_col, y_col, z_col)) + 1}',
                   c='black', marker='o')

    # Extracting specific columns for BlueROV X, Y, Z
    bluerov_x = data_interval.iloc[:, 2]  # BlueROV X is column 2
    bluerov_y = data_interval.iloc[:, 3]  # BlueROV Y is column 3
    bluerov_z = data_interval.iloc[:, 4]  # BlueROV Z is column 4

    # Plotting BlueROV X, Y, Z in blue with thicker markers
    ax.scatter(bluerov_x, bluerov_y, bluerov_z, label='BlueROV Position', c='blue', marker='^',
               s=100)  # s=100 for thicker markers

    # Adding plot labels and legend
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    ax.set_title('3D Plot of Multiple Markers and BlueROV Positions')
    #ax.legend()
    plt.show()

def main():
    # Path to the TSV file
    file_path = 'circle.tsv'

    # Read the TSV file
    data = read_tsv(file_path)

    # If data was successfully read, plot the markers
    if data is not None:
        plot_data(data, max_points=500)  # Limit the number of points plotted to 500

# Standard Python boilerplate
if __name__ == '__main__':
    main()
