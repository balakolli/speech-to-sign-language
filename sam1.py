import os
import string
from flask import Flask, render_template, request, url_for
from moviepy.editor import concatenate_videoclips, VideoFileClip
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

def load_letter_video(letter):
    # Assuming the letter videos are stored in a folder named 'letters'
    video_path = f"letters/{letter}.mp4"
    return VideoFileClip(video_path)

def combine_letters_to_word(word):
    letter_clips = []
    for letter in word:
        if letter.isalpha():  # Ensure it's a valid letter
            letter_clip = load_letter_video(letter.lower())
            letter_clips.append(letter_clip)
    if letter_clips:
        word_clip = concatenate_videoclips(letter_clips)
        return word_clip
    else:
        return None

def merge_and_get_video(sentence):
    words = sentence.split()
    video_clips = []

    for word in words:
        if os.path.exists(f"ISL_Gifs/{word}.mp4"):
            # If the MP4 video file exists, add it to the list of video clips
            word_clip = VideoFileClip(f"ISL_Gifs/{word}.mp4")
            video_clips.append(word_clip)
        else:
            # If the word video doesn't exist, create it from individual letters
            word_clip = combine_letters_to_word(word)
            if word_clip:
                video_clips.append(word_clip)

    # Merge all word videos into a single video
    if video_clips:
        merged_clip = concatenate_videoclips(video_clips)
        return merged_clip
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        '''recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)'''
        try:
            #text = recognizer.recognize_google(audio)
            text=input("enter text:")
            text = text.lower()  # Get text from the form

            # Merge videos based on the provided text
            merged_clip = merge_and_get_video(text)

            if merged_clip:
                # Resize the video for better display
                resized_clip = merged_clip.resize(height=360)

                # Write the resized video to a file
                video_path = "static/merged_video.mp4"
                resized_clip.write_videofile(video_path, codec="libx264")

                # Generate URL for the static file
                video_url = url_for('static', filename='merged_video.mp4')

                # Render template with video URL
                return render_template('translate.html', video_url=video_url)
            else:
                return "No valid words found in the database."
        except Exception as e:
            print("Error:", e)
            return "An error occurred."

if __name__ == '__main__':
    app.run(debug=True)
