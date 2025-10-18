import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phased Array Antenna Model", layout="centered")

st.title(" Phased Array Antenna Simulator")
st.markdown("""
Model and visualize how antenna arrays steer radio waves by controlling the **phase** and **geometry** of their elements.
""")

# Sidebar controls
st.sidebar.header(" Simulation Parameters")

num_elements = st.sidebar.slider("Number of Elements", 2, 32, 8)
element_spacing = st.sidebar.slider("Element Spacing (in wavelengths)", 0.1, 2.0, 0.5, 0.1)
frequency = st.sidebar.number_input("Frequency (GHz)", 1.0, 30.0, 3.0, 0.1)
steering_angle = st.sidebar.slider("Steering Angle (°)", -90, 90, 30)
amplitude_taper = st.sidebar.checkbox("Use Amplitude Tapering (e.g., Hamming Window)", False)

st.sidebar.markdown("---")
st.sidebar.write(" Adjust parameters to see how the beam pattern changes in real time.")

# Constants
c = 3e8  # speed of light
wavelength = c / (frequency * 1e9)
k = 2 * np.pi / wavelength  # wave number
d = element_spacing * wavelength
angles = np.linspace(-np.pi/2, np.pi/2, 1000)

# Array factor calculation
n = np.arange(num_elements)
if amplitude_taper:
    weights = np.hamming(num_elements)
else:
    weights = np.ones(num_elements)

phase_shift = -k * d * np.sin(np.deg2rad(steering_angle))
AF = np.zeros_like(angles, dtype=complex)
for i in range(num_elements):
    AF += weights[i] * np.exp(1j * (k * d * i * np.sin(angles) + i * phase_shift))

AF_dB = 20 * np.log10(np.abs(AF) / np.max(np.abs(AF)))

# Plotting
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6,6))
ax.plot(angles, np.maximum(AF_dB, -40), color='dodgerblue', lw=2)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_title(f"Array Pattern (Steered to {steering_angle}°)", va='bottom')
ax.set_rlim(-40, 0)

st.pyplot(fig)

# Optional details
with st.expander(" Show Array Factor Equation"):
    st.latex(r"""
    AF(\theta) = \sum_{n=0}^{N-1} w_n \, e^{j(k d n \sin(\theta) + n \phi)}
    """)
    st.markdown("""
    - \( w_n \): amplitude weight (Hamming/Uniform)  
    - \( d \): element spacing  
    - \( \phi \): phase shift for steering  
    - \( k = \frac{2\pi}{\lambda} \): wave number
    """)

st.success(" Simulation complete. Adjust parameters to see real-time updates!")
