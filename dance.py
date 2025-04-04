import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import time

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, smooth_landmarks=True, 
                     min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

# Define Pose Connections for Stick Figure
POSE_CONNECTIONS = [(11, 12), (11, 13), (13, 15),  # Left Arm
                    (12, 14), (14, 16),  # Right Arm
                    (11, 23), (12, 24),  # Upper Body
                    (23, 24), (23, 25), (24, 26),  # Hips
                    (25, 27), (26, 28),  # Upper Legs
                    (27, 31), (28, 32)]  # Lower Legs

# Set up 3D plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
plt.ion()  # Interactive mode ON

# Color List for Dynamic Changes
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]
color_index = 0
last_color_change = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    # Change colors every 3 seconds
    if time.time() - last_color_change > 3:
        color_index = (color_index + 1) % len(colors)
        last_color_change = time.time()

    glow_color = colors[color_index]

    if results.pose_landmarks:
        height, width, _ = frame.shape
        center_x = width // 2
        clone_offset = width // 4  # Move the clone beside the original

        landmarks_2d = [(int(lm.x * width), int(lm.y * height)) for lm in results.pose_landmarks.landmark]
        mirror_2d = [(center_x - (x - center_x) + clone_offset, y) for x, y in landmarks_2d]
        landmarks_3d = [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]

        glow_layer = np.zeros_like(frame, dtype=np.uint8)

        for i, j in POSE_CONNECTIONS:
            cv2.line(glow_layer, mirror_2d[i], mirror_2d[j], glow_color, 10)
            cv2.line(glow_layer, mirror_2d[i], mirror_2d[j], (255, 255, 255), 3)

        for x, y in mirror_2d:
            cv2.circle(glow_layer, (x, y), 10, glow_color, -1)
            cv2.circle(glow_layer, (x, y), 5, (255, 255, 255), -1)

        frame = cv2.addWeighted(frame, 0.8, glow_layer, 0.6, 0)

        # Update 3D Plot
        ax.clear()
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_title("3D Pose Visualization")
        for i, j in POSE_CONNECTIONS:
            x_vals, y_vals, z_vals = zip(landmarks_3d[i], landmarks_3d[j])
            ax.plot(x_vals, y_vals, z_vals, marker='o', color='cyan')
        plt.draw()
        plt.pause(0.01)

    cv2.imshow("Cyberpunk Dance Clone", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()
