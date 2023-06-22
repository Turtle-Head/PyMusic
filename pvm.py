# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:35:52 2023
Py_Visual_lMusic
-Console based Python built player for MP3 music
-=--=-
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
        print("2. Play")
        print("3. Rewind")
        print("4. Stop")
        print("5. Next")
        print("6. Exit")

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
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.open_directory()
            elif choice == "2":
                self.play_audio()
            elif choice == "3":
                self.rewind_audio()
            elif choice == "4":
                self.stop_audio()
            elif choice == "5":
                self.next_audio()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

        pygame.mixer.quit()


def main():
    audio_player = AudioPlayer()
    audio_player.run()


if __name__ == "__main__":
    main()
