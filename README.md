Gesture Recognition Project

This project uses OpenCV and MediaPipe to detect hand gestures (Rock, Paper, Scissors) via a webcam.
The code processes real-time video input, identifies key hand landmarks, and classifies the gestures based on landmark positions.

Features

Real-Time Gesture Detection: Detects hand gestures (Rock, Paper, Scissors) in real-time.
Gesture Persistence Check: Prevents duplicate gesture detection by requiring gestures to be held for a minimum time.
Customizable: Easily add more gestures by defining landmark-based rules.

Requirements

Python 3.x
OpenCV
MediaPipe

Install the dependencies with the following command:

pip install opencv-python mediapipe

Usage
Clone the repository:

git clone https://github.com/lakshitsachdeva/opencv-rps.git


Run the script:

python main.py

The program will open the default webcam and start detecting gestures. Press q to exit.

Gesture Details

Rock
All fingers curled except the thumb.
Thumb extended sideways.

Paper
All fingers extended.

Scissors
Index and middle fingers extended.
Ring and pinky fingers curled.

How It Works
Landmark Detection: Uses MediaPipe to detect hand landmarks and calculates their positions in the video frame.

Gesture Classification:
Based on the relative positions of key landmarks, gestures are classified as Rock, Paper, or Scissors.
Includes a persistence check to avoid duplicate gesture detection.
Real-Time Visualization: Draws landmarks and connections on the video feed to provide visual feedback.

Customization

You can add more gestures by modifying the gesture detection logic inside the try block:

if condition_for_new_gesture:
    detected_gesture = "New Gesture"

Example:
To add a "Thumbs Up" gesture:
if cordss[4][1] < cordss[3][1] and cordss[8][1] > cordss[5][1]:
    detected_gesture = "Thumbs Up"

    
Known Issues
The system may misclassify gestures if the hand is not clearly visible.
Lighting conditions and camera resolution can affect accuracy.

Contributions
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

Contact

For questions or feedback, please contact:
Name: Lakshit Sachdeva 
Email: lakshitsachdeva14@gmail.com
GitHub: lakshitsachdeva

