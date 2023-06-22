# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:46:49 2023
-Creating a Musical World one song at a time
@author: James Fehr
"""

import os
import pygame

class AudioPlayer:
    def __init__(self):
        self.directory = ""
        self.audio_files = []
        self.current_index = -1

        # Initialize Pygame mixer
        pygame.mixer.init()

    def display_menu(self):
        print("\n--- Audio Player Menu ---")
        print("1. Open Directory")
        print("2. Display MP3 Files")
        print("3. Play")
        print("4. Rewind")
        print("5. Stop")
        print("6. Next")
        print("7. Exit")

    def open_directory(self):
        self.directory = input("Enter the directory path containing the MP3 files: ")
        if os.path.isdir(self.directory):
            self.audio_files = [
                os.path.join(self.directory, filename)
                for filename in os.listdir(self.directory)
                if filename.endswith('.mp3')
            ]
            if self.audio_files:
                print(f"Found {len(self.audio_files)} MP3 files.")
                self.current_index = 0
            else:
                print("The selected directory does not contain any MP3 files.")
        else:
            print("Invalid directory path.")

    def display_mp3_files(self):
        if self.audio_files:
            print("\n--- MP3 Files ---")
            for index, file in enumerate(self.audio_files):
                print(f"{index+1}. {os.path.basename(file)}")
        else:
            print("No MP3 files available.")

    def play_audio(self):
        if self.audio_files:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(self.audio_files[self.current_index])
                pygame.mixer.music.play()

    def rewind_audio(self):
        if self.audio_files and pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()

    def stop_audio(self):
        if self.audio_files:
            pygame.mixer.music.stop()

    def next_audio(self):
        if self.audio_files:
            pygame.mixer.music.stop()
            self.current_index = (self.current_index + 1) % len(self.audio_files)
            pygame.mixer.music.load(self.audio_files[self.current_index])
            pygame.mixer.music.play()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                self.open_directory()
            elif choice == "2":
                self.display_mp3_files()
            elif choice == "3":
                self.play_audio()
            elif choice == "4":
                self.rewind_audio()
            elif choice == "5":
                self.stop_audio()
            elif choice == "6":
                self.next_audio()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

        pygame.mixer.quit()


def main():
    audio_player = AudioPlayer()
    audio_player.run()


if __name__ == "__main__":
    main()
