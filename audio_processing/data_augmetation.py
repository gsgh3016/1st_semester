import audio_processing as ap
import numpy as np
import logging

def data_augmentation(y, sr):
    audio_specs = ap.values()
    audio_specs.compute()
    values = audio_specs.params()
    
    augmented_data = {
        'chroma_stft_mean': np.mean(values['chroma_stft']),
        'chroma_stft_var': np.var(values['chroma_stft']),
        """
        밑에도 일괄 적용
        """
        
        'rms_mean': np.mean(ap.rms(y=y), axis=1).astype(np.float64),
        'rms_var': np.var(ap.rms(y=y), axis=1).astype(np.float64),
        'spectral_centroid_mean': np.mean(ap.spectral_centroid(y=y, sr=sr), axis=1).astype(np.float64),
        'spectral_centroid_var': np.var(ap.spectral_centroid(y=y, sr=sr), axis=1).astype(np.float64),
        'spectral_bandwidth_mean': np.mean(ap.spectral_bandwidth(y=y, sr=sr), axis=1).astype(np.float64),
        'spectral_bandwidth_var': np.var(ap.spectral_bandwidth(y=y, sr=sr), axis=1).astype(np.float64),
        'rolloff_mean': np.mean(ap.spectral_rolloff(y=y, sr=sr), axis=1).astype(np.float64),
        'rolloff_var': np.var(ap.spectral_rolloff(y=y, sr=sr), axis=1).astype(np.float64),
        'zero_crossing_rate_mean': np.mean(ap.zero_crossing_rate(y), axis=1).astype(np.float64),
        'zero_crossing_rate_var': np.var(ap.zero_crossing_rate(y), axis=1).astype(np.float64),
        'harmony_mean': np.mean(ap.harmonic(y), axis=0).astype(np.float64),
        'harmony_var': np.var(ap.harmonic(y), axis=0).astype(np.float64),
        'tempo': ap.tempo(y=y, sr=sr)[0].astype(np.float64),
        'mfcc1_mean': np.mean(ap.mfcc(y=y, sr=sr, n_mfcc=20)[0], axis=0).astype(np.float64),
        'mfcc1_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[0], axis=0).astype(np.float64),
        'mfcc2_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[1], axis=0).astype(np.float64),
        'mfcc2_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[1], axis=0).astype(np.float64),
        'mfcc3_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[2], axis=0).astype(np.float64),
        'mfcc3_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[2], axis=0).astype(np.float64),
        'mfcc4_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[3], axis=0).astype(np.float64),
        'mfcc4_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[3], axis=0).astype(np.float64),
        'mfcc5_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[4], axis=0).astype(np.float64),
        'mfcc5_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[4], axis=0).astype(np.float64),
        'mfcc6_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[5], axis=0).astype(np.float64),
        'mfcc6_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[5], axis=0).astype(np.float64),
        'mfcc7_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[6], axis=0).astype(np.float64),
        'mfcc7_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[6], axis=0).astype(np.float64),
        'mfcc8_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[7], axis=0).astype(np.float64),
        'mfcc8_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[7], axis=0).astype(np.float64),
        'mfcc9_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[8], axis=0).astype(np.float64),
        'mfcc9_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[8], axis=0).astype(np.float64),
        'mfcc10_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[9], axis=0).astype(np.float64),
        'mfcc10_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[9], axis=0).astype(np.float64),
        'mfcc11_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[10], axis=0).astype(np.float64),
        'mfcc11_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[10], axis=0).astype(np.float64),
        'mfcc12_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[11], axis=0).astype(np.float64),
        'mfcc12_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[11], axis=0).astype(np.float64),
        'mfcc13_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[12], axis=0).astype(np.float64),
        'mfcc13_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[12], axis=0).astype(np.float64),
        'mfcc14_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[13], axis=0).astype(np.float64),
        'mfcc14_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[13], axis=0).astype(np.float64),
        'mfcc15_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[14], axis=0).astype(np.float64),
        'mfcc15_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[14], axis=0).astype(np.float64),
        'mfcc16_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[15], axis=0).astype(np.float64),
        'mfcc16_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[15], axis=0).astype(np.float64),
        'mfcc17_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[16], axis=0).astype(np.float64),
        'mfcc17_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[16], axis=0).astype(np.float64),
        'mfcc18_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[17], axis=0).astype(np.float64),
        'mfcc18_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[17], axis=0).astype(np.float64),
        'mfcc19_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[18], axis=0).astype(np.float64),
        'mfcc19_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[18], axis=0).astype(np.float64),
        'mfcc20_mean': np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[19], axis=0).astype(np.float64),
        'mfcc20_var': np.var(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)[19], axis=0).astype(np.float64),
    }
    for i in augmented_data.keys():
        if isinstance(augmented_data[i], np.ndarray):
            augmented_data[i] = np.float64(augmented_data[i].item())    # np.ndarray를 np.float64로 맞춰주기
    return augmented_data

def process_audio(row):
    source_audio_location = "Data/genres_original"
    genre = row["label"]
    filename = row["filename"]
    file_path = f"{source_audio_location}/{genre}/{filename}"

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        y, sr = librosa.load(file_path)
    except Exception as e:
        logger.error(f"Error loading audio file {file_path}: {e}")
        return []  # Return an empty list in case of error

    augmentations = [
        librosa.effects.pitch_shift(y=y, sr=sr, n_steps=4),
        librosa.effects.time_stretch(y, rate=1.5),
        y + 0.005 * np.random.randn(len(y)),
        librosa.effects.preemphasis(y)
    ]
    
    features_list = []
    for augmented_y in augmentations:
        augmented_features = data_augmentation(augmented_y, sr)  # Assuming this function returns a dict
        features_list.append(augmented_features)
    
    return features_list
