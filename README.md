# 💬 Speech to Sign Language Translator

## 📝 Description

This project is a web-based application that translates **spoken words into Indian Sign Language (ISL)** gestures. It uses a combination of **speech recognition**, **NLP**, and **video retrieval** to visually represent spoken language.  
The primary goal is to **bridge the communication gap between hearing and deaf communities** by providing an accessible translation tool.

---

## 🚀 Features

- 🎙️ **Speech-to-Text Conversion**  
  Captures audio from the user's microphone and converts it into text using speech recognition.

- 🧠 **Sign Language Translation**  
  Maps recognized words to pre-recorded ISL video clips.

- 🔤 **Word-to-Letter Fallback**  
  If a word-level video is unavailable, the system spells it using individual letter videos.

- 🖥️ **User-Friendly Web Interface**  
  Simple, clean, and easy to use.

---

## 🛠️ Technologies Used

### 🔧 Backend:
- **Python** – Core programming language
- **Flask** – Web framework for handling routes and rendering templates
- **speech_recognition** – For converting speech to text
- **moviepy** – For video processing and concatenation
- **Natural Language Processing (NLP)** – Used for tokenizing sentences into individual words
  - Python built-in string methods, or optional libraries like `nltk`
- **Computer Vision (CV)** – Implemented through logic for video retrieval based on processed words

### 🎨 Frontend:
- **HTML/CSS** – For structuring and styling the web interface

---

## 🧠 NLP and Computer Vision

### 🗣️ Natural Language Processing (NLP)
The system uses **NLP for tokenization**, breaking down recognized sentences into individual words. This enables the application to search for each word’s corresponding ISL video.

### 👁️ Computer Vision (Simplified)
The project applies a simplified form of CV:
- Based on recognized words, it retrieves corresponding video clips from a dataset of pre-recorded ISL gestures.
- If a specific word video is missing, individual letter videos are used to spell the word.

While not using deep learning-based vision models, the logic simulates computer vision behavior through data mapping.

---
## ⚙️ Setup and Installation

### 1. Clone the repository:
```bash
git clone [Your-GitHub-Repo-URL]
cd [Your-Project-Folder]



