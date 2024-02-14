# 1st_semester

## 개요
- 부산대학교 전자공학과 졸업과제 소스 코드입니다.
- 프로젝트 기간: 2022년 1학기 (2022.01 ~ 2022.06)
- 주요 내용: Music Genre Classification과 Music Recommendation 시스템 개발
- 본 프로젝트는 [Andrada Olteanu의 코드](https://www.kaggle.com/code/andradaolteanu/work-w-audio-data-visualise-classify-recommend/notebook)를 바탕으로 작성된 코드입니다.

## 데이터 및 모델
### 모델
- **Music Genre Classification**
    - XGBoost
    - LightGBM
    - CatBoost
- **Music Recommendation**
    - Cosine Similarity
    - Euclidean Distance
    - K-Nearest Neighbor (Manhattan 기반)
    - Singular Value Decomposition

### 데이터
- [**GTZAN Dataset**](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification): 10개 장르별로 30초 길이의 100곡, 총 1000곡의 음원 사용
- **전처리 기법**:
    - Chroma STFT
    - RMS
    - Spectral Centroid
    - Spectral Bandwidth
    - Rolloff
    - Zero Crossing Rate
    - Harmony Mean
    - Tempo
    - Mel-frequency cepstral coefficients (MFCC)

## 개발 환경
- **OS**: macOS Sonoma 14.2.1
- **IDE**: Visual Studio Code (VSCode)
- **가상환경**: Python `venv` 모듈 사용 권장

## 실행 방법

### 가상환경 설정

프로젝트의 종속성을 격리시키고 관리하기 위해 Python `venv` 모듈을 사용하여 가상 환경을 설정하는 것이 좋습니다.

```bash
python3 -m venv venv
source venv/bin/activate  # macOS 또는 Linux
```

Windows에서는 다음 명령어를 사용합니다.

```bash
.\venv\Scripts\activate
```

### 종속성 설치

가상 환경이 활성화된 상태에서, 다음 명령어로 필요한 Python 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

### 데이터 준비

GTZAN: [https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)

#### GTZAN 데이터셋을 다운 받을 경우

- 프로젝트 디렉토리에 GTZAN 데이터셋 파일 압축을 푸세요.

#### GTZAN 데이터셋을 다운 받지 않은 경우

- 데이터셋을 다운로드하기 위해서는 Kaggle 계정이 필요합니다. Kaggle 계정을 생성하고 API 키와 사용자 이름을 `.env` 파일에 입력하고 저장하세요.(`.env_sample` 참고)


#### 분석할 음원 파일 준비

- 분석할 음원 파일을 `Data` 디렉토리에 저장합니다. `graduation_final.ipynb` 실행 시 `Data` 디렉토리가 자동으로 생성됩니다.

- **주의**: 현재 시스템은 한 번에 **1개의 음원 파일만 처리**합니다. 추후 여러 파일을 동시에 처리할 수 있는 기능으로 업데이트될 예정입니다.

## 참고 자료 및 기록

- 참고 코드: [링크](https://www.kaggle.com/code/andradaolteanu/work-w-audio-data-visualise-classify-recommend/notebook)
- 2022.01 ~ 2022.06: 참고 코드에 사용자 음원에 대해 장르 구분 및 유사 음원 추천(결과는 `docs/final_presentation.pdf` 참고.).
- 2023.03 ~ 2024.02: 장르 구분 모델 / 유사 음원 추천 종류 다각화.
