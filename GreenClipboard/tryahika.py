import matplotlib.pyplot as plt

# Define the data for each skill
skills = ['Network Scanning and Enumeration', 'Password Cracking', 'Cryptography', 'Penetration Testing', 'Programming Languages', 'Tools and Technologies', 'Leadership']
values = [7, 5, 6, 7, 8, 7, 5]

# Define the colors for each skill
colors = ['#2D2D2D', '#404040', '#535353', '#686868', '#7D7D7D', '#929292', '#A7A7A7']

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar chart for the skills
ax.set_ylim([0, 10])
ax.bar(skills, values, color=colors)
ax.set_title('Cybersecurity Skills')
ax.set_xlabel('Skills')
ax.set_ylabel('Level of Proficiency')

# Adjust the font size and rotation of the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=15)

# Adjust the spacing between the bars
plt.subplots_adjust(bottom=0.25)

# Show the chart
plt.show()
