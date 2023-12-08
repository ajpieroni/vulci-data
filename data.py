# TO RUN:
# /opt/homebrew/bin/python3.11 ./data.py

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path = './16_tracking_data_trial_1.txt'
df = pd.read_csv(file_path, delimiter='\t', skiprows=[1])
df.columns = df.columns.str.strip()

fig = plt.figure(figsize=(20, 8))

#3D Scatter Plot of Gaze Points
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(df['point x'], df['point y'], df['point z'], c='blue', marker='o')
ax1.set_xlabel('Point X')
ax1.set_ylabel('Point Y')
ax1.set_zlabel('Point Z')
ax1.set_title('3D Plot of Gaze Points')

# old 3D Trajectory Plot of Gaze Path

# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot(df['point x'], df['point y'], df['point z'], color='blue', marker='o', markersize=2, linestyle='-', linewidth=1)
# ax2.set_xlabel('Point X')
# ax2.set_ylabel('Point Y')
# ax2.set_zlabel('Point Z')
# ax2.set_title('3D Trajectory of Gaze Path')

normalized_time = (df['seconds'] - df['seconds'].min()) / (df['seconds'].max() - df['seconds'].min())

# color map for time
colors = plt.cm.viridis(normalized_time)

# 3D Trajectory Plot of Gaze Path
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df['point x'], df['point y'], df['point z'], c=colors, marker='o')
ax.plot(df['point x'], df['point y'], df['point z'], color='grey', linestyle='-', linewidth=1, alpha=0.5)

ax.set_xlabel('Point X')
ax.set_ylabel('Point Y')
ax.set_zlabel('Point Z')
ax.set_title('3D Trajectory of Gaze Path with Time Gradient')

# color legend
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Time (Normalized)')

# Time series analysis plot
fig_ts, ax1 = plt.subplots(figsize=(12, 8))

# xyz coords
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Point X, Y, Z', color='tab:red')
ax1.plot(df['seconds'], df['point x'], color='tab:red', label='Point X')
ax1.plot(df['seconds'], df['point y'], color='tab:green', label='Point Y')
ax1.plot(df['seconds'], df['point z'], color='tab:blue', label='Point Z')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.legend(loc='upper left')

# pupil diam
ax2 = ax1.twinx()
ax2.set_ylabel('Pupil Diameter', color='tab:purple')
ax2.plot(df['seconds'], df['pupil diameter'], color='tab:purple', linestyle='dashed', label='Pupil Diameter')
ax2.tick_params(axis='y', labelcolor='tab:purple')
ax2.legend(loc='upper right')

fig_ts.tight_layout()
plt.title('Time Series Analysis of Gaze Data')
plt.show()
# show
