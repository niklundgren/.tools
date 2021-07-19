# MATPLOTLIB COMMANDS

# Increase legend line width
leg = plt.legend()
for line in leg.get_lines():
    line.set_linewidth(4)

# Adjust z-order
plt.plot(..., zorder=100)
