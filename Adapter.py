class Converter:
    def format(self):
        pass
    def bitrate(self):
        pass
    def frequency(self):    #частота
        pass

class Music_original(Converter):
    def format(self):
        return "wav"
    def bitrate(self):
        return "128 kbps"
    def frequency(self):
        return "96000 Khz"

class Music_convert:
    def format(self):
        pass
    def bitrate(self):
        pass
    def frequency(self):
        pass

class Music_after(Music_convert):
    __progress = None

    def __init__(self, progress):
        self.__progress = progress

    def format(self):
        return "mp3"
    def bitrate(self):
        return self.__progress.bitrate()
    def frequency(self):
        return "48000 Khz"

#Client
class Play_in_converter:
    __converter = None

    def __init__(self, converter):
        self.__converter = converter

    def play(self):
        if self.__converter.format() > "mp3":
            print("Player not active")
        else:
            if self.__converter.bitrate() == "128 kbps" and self.__converter.frequency() == "48000 Khz":
                print('Music play in '+self.__converter.format()+' format, bitrate - '+self.__converter.bitrate()+', frequency - '+self.__converter.frequency())

def main():
    music_original = Music_original()
    music_after = Music_after(music_original)
    Mp3 = Play_in_converter(music_after)
    Mp3.play()
if __name__ == "__main__":
    main()