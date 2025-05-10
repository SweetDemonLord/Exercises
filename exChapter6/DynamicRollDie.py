"""Dynamic construction of a histogram of dice roll frequencies"""
from matplotlib import animation
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys

def update(frame_number, rolls, faces, frequencies):
    """Customizes the chart content for each animation frame"""
    # Rolling a die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1

    # Adjust chart for updated frequencies
    plt.cla() # Clear old content of current chart
    axes = sns.barplot(faces, frequencies, palette='bright')
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10) # Axis scaling by 10%

    # Output frequency and percentage above each column
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

    # Getting command line arguments for frame count and throws per frame
    number_of_frames = int(sys.argv[1])
    rolls_per_frame = int(sys.argv[2])

    sns.set_style('whitegrid') # White background with grey lines
    figure = plt.figure('Rolling a Six-Sided Die') # Drawing for animation
    values = list(range(1, 7)) # Designation of faces for output on the x-axis
    frequencies = [0] * 6 # Six element frequency list

    # Setting up and running an animation that calls the update function
    die_animation = animation.FuncAnimation(
        figure, update, repeat=False, frames=number_of_frames, interval=33,
        fargs=(rolls_per_frame, values, frequencies))
plt.show() # Window output
