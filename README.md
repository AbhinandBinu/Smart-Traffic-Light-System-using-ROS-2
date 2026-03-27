# 🚦 Smart Traffic Light System using ROS 2

## 📌 Overview

This project simulates a **Smart Traffic Light System** using ROS 2.  
It demonstrates communication between multiple nodes using the Publisher–Subscriber model.

The system mimics real-world traffic signal behavior and vehicle responses.

---

## ⚙️ System Architecture


Traffic Light Node ─────► /traffic_signal ─────► Vehicle Node
│
└────► Traffic Monitor Node


Bonus:

/emergency ─────► Traffic Light Node (override)


---

## 🧩 Nodes Description

### 🚦 Traffic Light Node
- Publishes traffic signals on `/traffic_signal`
- Sequence: `RED → GREEN → YELLOW → RED`
- Publishes every 3 seconds

---

### 🚗 Vehicle Node
- Subscribes to `/traffic_signal`
- Reacts based on signal:
  - RED → Stop
  - GREEN → Move
  - YELLOW → Slow Down

---

### 📊 Traffic Monitor Node
- Displays current traffic signal
- Helps visualize system state

---

### 🚑 Emergency Node (Bonus)
- Publishes `"EMERGENCY"` on `/emergency`
- Overrides signal to GREEN immediately

---

## 🚀 How to Run

### 1️⃣ Build Workspace
```bash
cd ~/my_ws
colcon build
source install/setup.bash
2️⃣ Run Nodes

Open multiple terminals:

ros2 run traffic_system traffic_light
ros2 run traffic_system vehicle
ros2 run traffic_system monitor
ros2 run traffic_system emergency   # (optional)
📊 Expected Output
Traffic Light
Signal: RED
Signal: GREEN
Signal: YELLOW
Vehicle
STOP
MOVE
SLOW DOWN
Emergency Mode
EMERGENCY triggered → GREEN signal forced
🧠 Key Concepts Covered
ROS 2 Publisher–Subscriber communication
Multi-node system design
Event-driven behavior
Real-time system simulation
🌍 Real-World Applications
Smart traffic control systems
Autonomous vehicle coordination
Emergency vehicle prioritization
👨‍💻 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Autonomous Systems | AI Integration
