# 📡 Model_Phased_Array_Antenna

### Modelling an Antenna Array using Python

This project demonstrates how to **model and visualize a phased array antenna** using Python. By adjusting parameters such as the **number of elements**, their **geometric arrangement**, and the **relative amplitudes and phases**, the antenna can **direct radio waves** toward a desired direction — a key principle in radar, wireless communication, and satellite systems.

---

## 🧠 Concept Overview

A **phased array antenna** consists of multiple radiating elements. The overall radiation pattern is shaped by **interference** between signals from these elements.
By controlling:
- **Amplitude** and **phase** of each element’s signal
- **Spacing** and **geometry** of the array

…we can **steer the main beam** without physically moving the antenna.

---

## 🧩 Features

- Simulation of **linear antenna arrays**
- Adjustable parameters for:
  - Number of elements
  - Element spacing
  - Frequency / wavelength
  - Phase shift for beam steering
- Visualization of **radiation patterns** using **Matplotlib**
- Interactive tuning of beam direction and array design

---

## 🛠️ Technologies Used

- **Python 3.x**
- **NumPy** – for mathematical and array computations
- **Matplotlib** – for plotting radiation patterns and beam steering results

---

## 📁 Project Structure

```
Model_Phased_Array_Antenna/
│
├── phased_array.py          # Main simulation script
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── plots/                   # Folder for saved radiation pattern images
```

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Model_Phased_Array_Antenna.git
   cd Model_Phased_Array_Antenna
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulation:**
   ```bash
   python phased_array.py
   ```

---

## ⚙️ Example Parameters

You can modify parameters inside `phased_array.py` such as:
```python
num_elements = 8
element_spacing = 0.5  # in wavelengths
steering_angle = 30    # degrees
frequency = 3e9        # 3 GHz
```

---

## 📊 Example Output

The script will generate a **polar plot** or **2D pattern** showing how the antenna’s beam direction changes based on your chosen parameters.

Example visualization:
```
🔹 Main lobe steered to 30°
🔹 Side lobes visible at ±60°
🔹 Gain variation across directions
```

---

## 🧭 Applications

- Radar beamforming
- Satellite communication
- 5G base stations
- Directional Wi-Fi antennas
- Radio astronomy arrays

---

## 📜 License

This project is open-source under the **MIT License**.
Feel free to use, modify, and share with attribution.

---

## 👨‍💻 Author

**Gaafer Gouda**
Aerospace Engineer & Data Science Enthusiast
- 💡 Interests: Antenna Modeling, Signal Processing, AI, and Space Systems
- 🌐 [LinkedIn](https://linkedin.com/) | [GitHub](https://github.com/)
