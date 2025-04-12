# Locating a Song in a Playlist Using Linear Search
def linear_search(playlist, song_title):
    for index, song in enumerate(playlist):
        if song.lower() == song_title.lower():
            return index
    return -1

def main():
    playlist = [
        "Bikhra",
        "Jab Tak",
        "Tum Hi Ho",
        "Tera Ban Jaunga",
        "Tu Hain Toh",
        "Apna Bana Le",
        "Ishq Wala Love",
        "Kabira",
        "Raabta",
        "Tum Mile",
        "Dil Diyan Gallan",
        "Pehla Nasha",
        "Tujh Mein Rab Dikhta Hai",
        "Tera Hone Laga Hoon",
        "Tum Se Hi",
        "Finding Her",
        "Tere Chehra",
        "Ishq Hai",
        "Millionaire",
        "Raataan Lambiyan",
        "O Maahi",
        "Jo Tum Mera Ho",
        "Tum Jo Aaye",
        "Song E"
    ]
    song_title = input("Enter the song title to search for: ")

    result = linear_search(playlist, song_title)
    
    if result != -1:
        print(f"'{song_title}' found at index {result}.")
    else:
        print(f"'{song_title}' not found in the playlist.")

if __name__ == "__main__":
    main()