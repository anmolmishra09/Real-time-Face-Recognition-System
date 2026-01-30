.

👁️ Drishti – The Ultimate Eye

Real-Time Face Recognition System

Drishti is a real-time face recognition–based surveillance and access monitoring system designed for campuses and secure environments. It detects, recognizes, and logs individuals entering or exiting a premises using computer vision and cloud services.

📁 Project Structure
Drishti-The-Ultimate-Eye-main/
│── AWS/                    # AWS integration files and scripts
│── Drishti-The-Ultimate-Eye/ # Core face recognition logic
│── dashhboard/             # Web dashboard for monitoring
│── test_open_cv/           # OpenCV testing scripts
│── README.md               # Project documentation

🚀 Features

Real-time face detection and recognition

Automatic entry/exit logging

Identification of authorized vs unauthorized users

Dashboard for monitoring records

Cloud integration using AWS

OpenCV-based face processing

🛠️ Tech Stack

Python

OpenCV

AWS (Rekognition / S3 / Lambda – if configured)

Flask / Dashboard UI

NumPy

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/Drishti-The-Ultimate-Eye.git
cd Drishti-The-Ultimate-Eye-main


Install dependencies

pip install -r requirements.txt


Run face recognition module

python Drishti-The-Ultimate-Eye/main.py


Run dashboard

cd dashhboard
python app.py

📸 How It Works

Camera captures live video

Faces are detected using OpenCV

Facial embeddings are matched with stored data

Entry/exit is logged

Records are displayed on dashboard

🗺️ Roadmap
Phase 1

Authenticate entry/exit at campus gates

Identify student, staff, or outsider

Store records in the system

Phase 2

Improve recognition accuracy

Add cloud backup and alerts

👨‍💻 Authors

Anmol Mishra Computer Science & Engineering Student Aspiring Software Developer
