def musica(a=False):
    from pygame import mixer
    
    if a:
        mixer.init()
        mixer.music.load('./T3C5_Squad_8_Beatriz_Marcus_Steffany_projeto_final/music.mp3')
        mixer.music.play(loops=2)
    else:
        mixer.music.stop()