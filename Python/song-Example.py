playlist=[]
for i in range(10):
    song_name=input(f"Enter the song name {i}:")
    playlist.append(song_name)
print(f"The list of songs are:{playlist}")
print(playlist[::-1])
