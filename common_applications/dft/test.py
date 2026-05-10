# importing the required packages and modules
import cmath
import math
import matplotlib.pyplot as plt
from dft_class import DFT
# ==============================================================================
# digital time domain signal 
fs = 1000
N = 256
f0 = 100

x = [5 * math.cos(2 * math.pi * f0 * n / fs) for n in range(N)]
# ==============================================================================
# Running the DFT
dft = DFT(fs, N)
freq_axis, dft_seq = dft.dft(x)
phy_freq_axis = dft.physical_freq_axis(freq_axis)
phy_dft_seq = dft.physical_dft_shift(dft_seq)

# --- Magnitude spectrum ---
magnitude = [abs(u) for u in dft_seq]
phy_magnitude = [abs(v) for v in phy_dft_seq]

# --- Plot ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))

ax1.plot(x[:100])
ax1.set_title("time domain signal")

ax2.plot(freq_axis, magnitude)
ax2.set_title("raw DFT sequence")

ax3.plot(phy_freq_axis, phy_magnitude)
ax3.set_title("DFT with physical frequency axis")


fig.patch.set_alpha(0)
for ax in (ax1, ax2, ax3):
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['top'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.spines['right'].set_color('lightgrey')
    ax.tick_params(colors='lightgrey')
    ax.xaxis.label.set_color('lightgrey')
    ax.yaxis.label.set_color('lightgrey')
    ax.title.set_color('lightgrey')
    ax.patch.set_alpha(0)

plt.tight_layout()
plt.show()