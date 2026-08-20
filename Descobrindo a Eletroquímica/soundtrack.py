import pygame
import sys, os


class SoundTrack:

    def __init__(self):
        # Inicializa o mixer com configurações padrão
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

        # Configuração inicial de volume (50% para ambos)
        self.master_volume = 0.5
        self.music_volume = 0.5
        self.sfx_volume = 0.5

        # Canais de áudio
        self.music_channel = pygame.mixer.music  # Canal de música
        self.sfx_channel = pygame.mixer.Channel(0)  # Canal de efeitos sonoros

        # Aplica os volumes iniciais
        self.music_channel.set_volume(self.music_volume * self.master_volume)
        self.sfx_channel.set_volume(self.sfx_volume * self.master_volume)

        # Arquivos de áudio
        self.soundtrack = None
        self.sounds = {}  # Dicionário para armazenar sons carregados
    # __init__()

    def load_music(self, soundtrack):
        """Carrega o arquivo de música de fundo"""
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
            self.music_channel.load(self.soundtrack)
        else:
            print(f"{soundtrack} not found... ignoring", file=sys.stderr)
    # load_music()

    def play_music(self, loops=-1):
        """Toca a música de fundo com o volume atual"""
        if self.soundtrack:
            self.music_channel.play(loops=loops)
    # play_music()

    def load_sound(self, key, sound_file):
        """Carrega um efeito sonoro e armazena com uma chave"""
        if os.path.isfile(sound_file):
            self.sounds[key] = pygame.mixer.Sound(sound_file)
        else:
            print(f"{sound_file} not found... ignoring", file=sys.stderr)
    # load_sound()

    def play_sound(self, key):
        """Toca um efeito sonoro com o volume atual"""
        if key in self.sounds:
            sound = self.sounds[key]
            sound.set_volume(self.sfx_volume * self.master_volume)
            self.sfx_channel.play(sound)
        else:
            print(f"Sound {key} not loaded... ignoring", file=sys.stderr)
    # play_sound()

    def adjust_volume(self, target, change):
        """
        Ajusta o volume gradualmente
        :param target: 'music' ou 'sfx' ou 'master'
        :param change: valor entre -0.1 e 0.1 para ajuste gradual
        """
        if target == 'music':
            self.music_volume = max(0.0, min(1.0, self.music_volume + change))
            self.music_channel.set_volume(self.music_volume * self.master_volume)
        elif target == 'sfx':
            self.sfx_volume = max(0.0, min(1.0, self.sfx_volume + change))
            self.sfx_channel.set_volume(self.sfx_volume * self.master_volume)
        elif target == 'master':
            self.master_volume = max(0.0, min(1.0, self.master_volume + change))
            # Atualiza ambos os volumes
            self.music_channel.set_volume(self.music_volume * self.master_volume)
            self.sfx_channel.set_volume(self.sfx_volume * self.master_volume)
    # adjust_volume()

    def get_volumes(self):
        """Retorna os volumes atuais"""
        return {
            'master': self.master_volume,
            'music': self.music_volume,
            'sfx': self.sfx_volume
        }
    # get_volumes()

    def stop_sound(self, key):
        if key in self.sounds:
            self.sfx_channel.stop()
        else:
            print(f"Sound {key} not loaded... ignoring", file=sys.stderr)
    # stop_sound()

    def stop_music(self):
        if self.soundtrack:
            self.music_channel.stop()
    # stop_music()
# SoundTrack
