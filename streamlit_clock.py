import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time

st.set_page_config(page_title="Analog + Digital Clock", layout="centered")
st.title("🕒 Analog + Digital Clock")

fig, ax = plt.subplots(figsize=(5, 5), facecolor='black')
ax.set_facecolor("black")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')

circle = plt.Circle((0, 0), 1, color='white', fill=False, linewidth=4)
ax.add_artist(circle)

for i in range(12):
    angle = np.deg2rad(i * 30)
    x_outer = np.sin(angle)
    y_outer = np.cos(angle)
    x_inner = 0.85 * x_outer
    y_inner = 0.85 * y_outer
    ax.plot([x_inner, x_outer], [y_inner, y_outer], color='white', linewidth=3)
    ax.text(0.75 * x_outer, 0.75 * y_outer, str(i if i != 0 else 12),
            fontsize=14, ha='center', va='center', color='yellow')

placeholder = st.empty()

while True:
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    [l.remove() for l in ax.lines[1:]]

    hour_angle = np.deg2rad((hour + minute / 60) * 30)
    minute_angle = np.deg2rad((minute + second / 60) * 6)
    second_angle = np.deg2rad(second * 6)

    ax.plot([0, 0.5 * np.sin(hour_angle)], [0, 0.5 * np.cos(hour_angle)],
            linewidth=6, color='white')
    ax.plot([0, 0.7 * np.sin(minute_angle)], [0, 0.7 * np.cos(minute_angle)],
            linewidth=4, color='cyan')
    ax.plot([0, 0.9 * np.sin(second_angle)], [0, 0.9 * np.cos(second_angle)],
            linewidth=2, color='red')

    placeholder.markdown(f"## 🕹️ Digital Time: `{now.strftime('%I:%M:%S %p')}`")
    placeholder.pyplot(fig)
    time.sleep(1)
