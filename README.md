# Dance Clone

This project creates a real-time interactive **clone dancer** beside your live webcam feed using **MediaPipe** and **OpenCV**, complete with glowing stick figure visuals and dynamic color transitions. It also provides a **3D plot** of your pose for enhanced visualization using **Matplotlib**.

---

## 📸 Demo

> A mirror-image stick figure clone follows your body movements on screen while the corresponding 3D pose is plotted live.

---

## 🚀 Features

- Real-time pose detection using **MediaPipe**
- Glowing **cyberpunk-style stick figure clone**
- Dynamic color transitions every 3 seconds
- Real-time **3D pose rendering** using `matplotlib`
- Smooth overlay blending for a polished visual
- Webcam integration for easy setup

---

## 🛠️ Dependencies

Install the required Python packages before running:

```bash
pip install opencv-python mediapipe matplotlib numpy
```

---

## 📁 File Structure

```plaintext
.
├── cyberpunk_dance_clone.py  # Main script
└── README.md                 # You're here!
```

---

## 📷 How It Works

### 🔍 Pose Detection
- Uses MediaPipe's `Pose` model to detect 33 keypoints on the human body in real-time from the webcam.

### 🧍 Stick Figure Clone
- A 2D mirrored version of your pose is drawn beside you.
- Connections and joints are styled with glowing effects and dynamic color changes.

### 📊 3D Visualization
- The 3D coordinates of detected landmarks are plotted in an interactive matplotlib window.

---

## 🔄 Pose Connections

These define which body parts are connected in the stick figure :

```python
POSE_CONNECTIONS = [
    (11, 12), (11, 13), (13, 15),  # Left Arm
    (12, 14), (14, 16),            # Right Arm
    (11, 23), (12, 24),            # Torso
    (23, 24), (23, 25), (24, 26),  # Hips
    (25, 27), (26, 28),            # Thighs
    (27, 31), (28, 32)             # Calves
]
```

---

## 🧠 Core Logic

1. **Capture frame** from webcam.
2. **Detect pose** landmarks using MediaPipe.
3. **Mirror pose** and offset it beside the original.
4. Draw a **glow layer** with thick lines and circles.
5. Blend this layer onto the original frame.
6. Plot the **3D pose** using matplotlib.
7. Repeat until user exits (`q` key).

---

## 🖥️ Run the Script

```bash
python cyberpunk_dance_clone.py
```

Press `q` to quit the application.

---

## 🔧 Customization

| Feature             | How to Change                           |
|---------------------|------------------------------------------|
| Glow colors         | Edit the `colors` list in the script     |
| Clone offset        | Modify `clone_offset` variable           |
| Pose smoothing      | Toggle `smooth_landmarks=True/False`     |
| 3D plot aesthetics  | Tweak `ax.set_xlim`, `ax.set_title`, etc |

---

## 🧪 Tested On

- Python 3.9+
- OpenCV 4.x
- MediaPipe 0.10+
- Matplotlib 3.x
- Windows/Linux/MacOS

---

## 📌 Notes

- Ensure your webcam is functional.
- Make sure no other app is using the camera.
- Ideal lighting improves pose detection accuracy.

---

## ✨ Credits

- Built using [MediaPipe](https://google.github.io/mediapipe/) for pose tracking.
- Visualization powered by [OpenCV](https://opencv.org/) and [Matplotlib](https://matplotlib.org/).

---

## 🧠 Future Ideas

- Add gesture-based controls (e.g., switch modes with hand signs)
- Export 3D poses as animation files
- Add audio-reactive visuals
