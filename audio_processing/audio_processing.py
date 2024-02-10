import tensorflow as tf
import numpy as np


class values:
    def __init__(self, file_path):
        self.y, self.sr = self.load_audio()
        self.midi_notes = []
        self.params = {
            "chroma_stft": self.chroma_stft(),
            "rms": self.rms(),
            "spectral_centroid": self.spectral_centroid(),
            "spectral_bandwidth": self.spectral_bandwidth(), 
            "rolloff": self.rolloff(),
            "zero_crossing_rate": self.zero_crossing_rate(),
            "harmony": self.harmony(),
            "tempo": self.tempo(),
            "mfccs": self.mfccs()
        }
        """
        오디오 처리하기 전, 파일을 불러오고 겹치는 연산하기(tensorflow 활용)
        """
        
    def load_audio(self):
        file_contents = tf.io.read_file(self.file_path)
        y, sample_rate = tf.audio.decode_wav(file_contents)
        return y, sample_rate
        
    def chroma_stft():
        pass
    
    def rms():
        pass
    
    def spectral_centroid():
        """
        spectral_centroid 구하는 함수.
        spectral_bandwidth와 구하는 과정이 많이 겹치면 함수를 하나로 합칠 것.
        """
        pass
    
    def spectral_bandwidth():
        """
        spectral_bandwidth 구하는 함수.
        """
        pass
    
    def rolloff():
        pass
    
    def zero_crossing_rate():
        pass
    
    def harmony():
        pass
    
    def tempo():
        pass
    
    def mfccs():
        """
        mfcc 값들을 구하는 함수.
        mfcc1 ~ mfcc20까지 값을 구해야 함.
        """
        pass
    
    def compute(self):
        self.chroma_stft()
        self.rms()
        self.spectral_centroid()
        self.spectral_bandwidth()
        self.rolloff()
        self.zero_crossing_rate()
        self.harmony()
        self.tempo()
        self.mfccs()
    
    def params(self):
        return self.params