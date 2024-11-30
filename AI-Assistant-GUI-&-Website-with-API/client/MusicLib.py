import webbrowser

songloc = "C:\\Users\\lenovo\\Music\\"

songs = {
    "one love": f"{songloc}One Love_320(PagalWorld.com.se).mp3",
    "choo lo" : f"{songloc}Choo Lo.mp3"
}

def playSong(song):
    webbrowser.open(songs[song])

if __name__ == "__main__":
    song = input("Enter Song Name: ")
    playSong(song.lower())