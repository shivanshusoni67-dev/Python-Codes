import time
import sys 


def print_lyrics():
    lyrics = [ 
        "BADE BADNAAM HUE " ,
        "BADE MASHOOR HUE " ,
        "APNO SE DUR HUE " ,
        "DUR HUYE " ,
        "DUR HUYE " ,
        "DIL KE MURDER BHI HUYE " ,
        "BADE TORTURE BHI HUYE " , 
        "GAMO SE CHUR HUYE " ,
        "CHUR HUYE " ,
        "CHUR HUYE " ,
    ]
    delays = [
        1.2 , 1.2 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0
    ]

    print(" 🎵 NOW PLAYING - 2025 MEIN KYA KYA HUA ? ")
    time.sleep(1.2)

    for i , line in enumerate (lyrics):
        for char in line :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8) 
print_lyrics()
