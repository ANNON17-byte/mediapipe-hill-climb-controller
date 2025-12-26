🏎️ MediaPipe Hill Climb Controller

Control Hill Climb Racing using body gestures in real time with computer vision.

This project uses MediaPipe Pose Detection, OpenCV, and PyDirectInput to map hand movements to in-game controls like acceleration and braking.

✨ Features

🎥 Real-time webcam capture

🧍 Full-body pose detection using MediaPipe Holistic

✋ Gesture-based game control

⌨️ Low-level keyboard input using PyDirectInput (game-compatible)

🪟 Optimized for Windows (DirectShow backend)

🛠️ Tech Stack
<p align="left"> <img src="https://skillicons.dev/icons?i=python,opencv,github" /> <img src="https://img.shields.io/badge/MediaPipe-Google-blue?logo=google&logoColor=white" /> <img src="https://img.shields.io/badge/PyDirectInput-Game%20Control-red" /> </p>

Python 3.10

MediaPipe (Holistic / Pose)

OpenCV

PyDirectInput

📂 Project Structure
mediapipe-hill-climb-controller/
├── hillclimb.py        # Main gesture control script
├── mp_env/             # Virtual environment (ignored in Git)
├── .gitignore
└── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/ANNON17-byte/mediapipe-hill-climb-controller.git
cd mediapipe-hill-climb-controller

2️⃣ Create a Virtual Environment
python -m venv mp_env


Activate it:

Windows

mp_env\Scripts\activate

3️⃣ Install Dependencies
pip install mediapipe==0.10.20 opencv-contrib-python pydirectinput

4️⃣ Launch Hill Climb Racing

Open Hill Climb Racing (PC / Emulator)

Ensure controls are:

Right Arrow → Accelerate

Left Arrow → Brake

Keep the game window focused

⚠️ On Windows, run the terminal or VS Code as Administrator for PyDirectInput to work reliably.

5️⃣ Run the Script
python hillclimb.py


Press q to quit.

🧍 Gesture Controls
Gesture	Action
Raise left hand	Accelerate
Raise right hand	Brake
Hands below midline	Idle
🧠 How It Works
Webcam
  ↓
MediaPipe Pose Detection
  ↓
Gesture Logic (Hand Height)
  ↓
PyDirectInput (Keyboard Events)
  ↓
Hill Climb Racing

⚠️ Important Notes

Ensure good lighting for accurate pose detection

Keep upper body visible in the camera frame

Close apps that may be using the webcam (Zoom, Camera app)

This project is designed for Windows
