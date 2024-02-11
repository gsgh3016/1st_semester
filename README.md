# 1st_semester

## 개요
- 부산대학교 전자공학과 졸업과제 소스 코드입니다.
- 프로젝트 기간: 2022년 1학기 (2022.01 ~ 2022.06)
- 주요 내용: Music Genre Classification과 Music Recommendation 시스템 개발

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
- **GTZAN Dataset**: 10개 장르별로 30초 길이의 100곡, 총 1000곡의 음원 사용
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

분석할 음원 파일을 Data 디렉토리(`graduation_final.ipynb` 실행 시 자동 생성)에 저장합니다.

    * 주의: 현재 시스템은 한 번에 1개의 음원 파일만 처리합니다. 추후 여러 파일을 동시에 처리할 수 있는 기능으로 업데이트될 예정입니다.
