# Set the title to reflect the plot we are making.
# Add the good_afternoon time variable (time_ga) and amplitude variable (soundwave_ga) to the plot.
# Do the same with the good_morning time variable (time_gm) and amplitude variable (soundwave_gm) to the plot.
# Set the alpha variable to 0.5.

# Setup the title and axis titles
plt.title('Good Afternoon vs. Good Morning')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')

# Add the Good Afternoon data to the plot
plt.plot(time_ga,soundwave_ga, label='Good Afternoon')

# Add the Good Morning data to the plot
plt.plot(time_gm,soundwave_gm,  label='Good Morning',
   # Set the alpha variable to 0.5
   alpha=0.5)

plt.legend()
plt.show()
