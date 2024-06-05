import cv2
import os
import random
import pygame
import keyboard
from deepface import DeepFace

pygame.init()

def play_song_based_on_emotion(dominant_emotion):
    if dominant_emotion == "happy":
        happy_songs = [
            r'Python-project-OpenCV-\happy_songs\Aye_Khuda_[Full_Song]_Paathshaala(256k).mp3'
            # Additional songs
        ]
        selected_song = random.choice(happy_songs)
        
    elif dominant_emotion == "sad":
        sad_songs = [
            r'Python-project-OpenCV-\sad_songs\Ava_Max_-_Into_Your_Arms__NO_RAP__%5BLyrics_Vietsub%5D_%7E_TikTok_Hits_%7E(256k).mp3'
            # Additional songs 
        ]
        selected_song = random.choice(sad_songs)

    elif dominant_emotion == "neutral":
        neutral_songs = [
            r'Python-project-OpenCV-\neutral_songs\_AGAR_TUM_SAATH_HO__Full_VIDEO_song___Tamasha___Ranbir_Kapoor%2C_Deepika_Padukone___T-Series(256k).mp3'
            # Additional songs 
        ]
        selected_song = random.choice(neutral_songs)

    elif dominant_emotion == "angry":
        angry_songs = [
            r'Python-project-OpenCV-\Angry_songs\Apna_Time_Aayega___Gully_Boy___Ranveer_Singh___Alia_Bhatt___DIVINE___Dub_Sharma___Zoya_Akhtar(256k).mp3'
            # Additional 
        ]
        selected_song = random.choice(angry_songs)

    elif dominant_emotion == "surprise":
        surprise_songs = [
            r'Python-project-OpenCV-\surprise_songs\_Lungi_Dance_Chennai_Express__New_Video_Feat._Honey_Singh%2C_Shahrukh_Khan%2C_Deepika(256k).mp3'
            # Additional songs 
        ]
        selected_song = random.choice(surprise_songs)

    elif dominant_emotion == "fear":
        fear_songs = [
            r'Python-project-OpenCV-\Fear_songs\Ajnabi_Hawaayein_[Full_Song]_Shaapit_By_Shreya_Ghoshal(256k).mp3'
            # Additional songs
        ]
        selected_song = random.choice(fear_songs)
        
    elif dominant_emotion == "disgust":
        disgust_songs = [
            r'Python-project-OpenCV-\disgust_songs\BHAAG_DK_BOSE_I_DELHI_BELLY_I_RAM_SAMPATH(256k).mp3'
            # Additional songs
        ]
        selected_song = random.choice(disgust_songs)

    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

    print("Press 'q' to stop the music and exit.")
    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed('q'):
            pygame.mixer.music.stop()
            break

def capture_and_analyze_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        return

    directory = 'images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, 'photo.jpg')
    cv2.imwrite(file_path, frame)

    img = cv2.imread(file_path)
    if img is None:
        print(f"Error: Failed to read the image file {file_path}.")
        return

    try:
        analysis = DeepFace.analyze(img, actions=['emotion'])
        dominant_emotion = analysis[0]['dominant_emotion']
        print("Detected emotion:", dominant_emotion)
        play_song_based_on_emotion(dominant_emotion)
    except Exception as e:
        print(f"Error: {e}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_analyze_emotion()
