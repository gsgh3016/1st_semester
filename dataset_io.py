import os
from multiprocessing import Pool
import librosa



def find_wav_files(directory):
    wav_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                wav_files.append(os.path.join(root, file))
    return wav_files

def load_audio(file_path) -> tuple:
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

if __name__ == '__main__':
    root_dir = 'Data/genres_original'
    wav_files = find_wav_files(root_dir)

    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(load_audio, wav_files)

    print(f"Loaded {len(results)} files.")