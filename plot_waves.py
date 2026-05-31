import matplotlib.pyplot as plt

times, a, b, c, g, h = [], [], [], [], [], []

print("Reading simulation.log...")

with open("simulation.log", "r") as f:
    for line in f:
        if "Time=" in line:
            parts = line.split("|")
            
            t = int(parts[0].strip().split("=")[1])
            times.append(t)
            
            inputs = parts[1].split()
            a.append(int(inputs[0].split("=")[1]))
            b.append(int(inputs[1].split("=")[1]))
            c.append(int(inputs[2].split("=")[1]))
            
            outputs = parts[2].split()
            g_val = outputs[0].split("=")[1]
            h_val = outputs[1].split("=")[1]
            
            g.append(0.5 if g_val == 'x' else int(g_val))
            h.append(0.5 if h_val == 'x' else int(h_val))

fig, axs = plt.subplots(5, 1, figsize=(10, 8), sharex=True)
fig.suptitle('Digital Logic Waveforms')

axs[0].step(times, a, where='post', color='blue')
axs[0].set_ylabel('Input A')
axs[0].set_ylim(-0.2, 1.2)

axs[1].step(times, b, where='post', color='blue')
axs[1].set_ylabel('Input B')
axs[1].set_ylim(-0.2, 1.2)

axs[2].step(times, c, where='post', color='blue')
axs[2].set_ylabel('Input C')
axs[2].set_ylim(-0.2, 1.2)

axs[3].step(times, g, where='post', color='red')
axs[3].set_ylabel('Output G')
axs[3].set_ylim(-0.2, 1.2)

axs[4].step(times, h, where='post', color='red')
axs[4].set_ylabel('Output H')
axs[4].set_ylim(-0.2, 1.2)
axs[4].set_xlabel('Time (ns)')

for ax in axs:
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels(['0', 'x', '1'])

plt.tight_layout()
plt.show()
