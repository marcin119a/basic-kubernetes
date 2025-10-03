# Kubernetes ML Project - Real Estate Price Prediction

Projekt zawiera aplikację do predykcji cen nieruchomości opartą na uczenia maszynowego, wdrożoną w Kubernetes z wykorzystaniem FastAPI i MLflow.

## 🏗️ Architektura

Projekt składa się z następujących komponentów:

- **FastAPI Application** - API do predykcji cen nieruchomości
- **MLflow** - narzędzie do zarządzania eksperymentami ML
- **Random Forest Model** - model do predykcji cen
- **Kubernetes Deployment** - orkiestracja kontenerów

## 📁 Struktura projektu

```
kubernetes-basic/
├── data/
│   └── adresowo_warszawa_wroclaw.csv    # Dane treningowe
├── main.py                              # FastAPI aplikacja
├── train.py                             # Szkolenie modelu ML
├── models.py                            # Definicje modeli Pydantic
├── Dockerfile                           # Konfiguracja kontenera
├── deployment.yaml                      # Kubernetes Deployment
├── flask-pod.yaml                       # Konfiguracja FastAPI Pod
├── flask-service.yaml                   # FastAPI Service
├── mlflow-pod.yaml                      # Konfiguracja MLflow Pod
└── mlflow-service.yaml                  # MLflow Service
```

## 🚀 Funkcjonalności

### API Endpoints

#### POST `/predict/`
Predykcja ceny nieruchomości na podstawie podanych parametrów.

**Request Body:**
```json
{
    "area_m2": 75.5,
    "rooms": 3,
    "photos": 8,
    "locality": "Mokotów",
    "street": "Marszałkowska",
    "property_type": "apartment",
    "city": "Warszawa",
    "price": 450000.0
}
```

**Response:**
```json
{
    "predicted_price": 425000.0
}
```

### Model ML

Model wykorzystuje **Random Forest Regressor** z następującymi cechami:
- `rooms` - liczba pokoi
- `area_m2` - powierzchnia w m²
- `photos` - liczba zdjęć
- `locality` - lokalizacja
- `street` - ulica
- `property_type` - typ nieruchomości
- `city` - miasto

## 🛠️ Instalacja i uruchomienie

### Wymagania
- Docker
- Kubernetes (minikube)
- kubectl

### 1. Przygotowanie środowiska

```bash
# Uruchomienie minikube
minikube start

# Konfiguracja Docker dla minikube
eval $(minikube docker-env)
```

### 2. Budowanie i wdrażanie

```bash
# Budowanie obrazu Docker
docker build -t marcin119a/fastapi-k8s-demo:latest .

# Wdrożenie aplikacji
kubectl apply -f deployment.yaml
kubectl apply -f flask-service.yaml

# Wdrożenie MLflow
kubectl apply -f mlflow-pod.yaml
kubectl apply -f mlflow-service.yaml
```

### 3. Sprawdzenie statusu

```bash
# Sprawdzenie podów
kubectl get pods

# Sprawdzenie serwisów
kubectl get svc

# Sprawdzenie deploymentów
kubectl get deployments
```

### 4. Dostęp do aplikacji

```bash
# Uzyskanie adresu FastAPI
minikube service fastapi-service --url

# Uzyskanie adresu MLflow
minikube service mlflow-service --url
```

## 🧪 Testowanie API

```bash
# Przykład wywołania API
curl -X POST "http://<SERVICE_URL>/predict/" \
     -H "Content-Type: application/json" \
     -d '{
       "area_m2": 75.5,
       "rooms": 3,
       "photos": 8,
       "locality": "Mokotów",
       "street": "Marszałkowska",
       "property_type": "apartment",
       "city": "Warszawa",
       "price": 450000.0
     }'
```

## 📊 MLflow

MLflow jest dostępne pod adresem uzyskanym przez `minikube service mlflow-service --url` i umożliwia:
- Śledzenie eksperymentów ML
- Zarządzanie modelami
- Monitoring metryk

## 🔧 Konfiguracja Kubernetes

### Deployment
- **Repliki:** 3
- **Port:** 8000
- **Obraz:** marcin119a/fastapi-k8s-demo:latest

### Services
- **FastAPI Service:** NodePort na porcie 80 → 8000
- **MLflow Service:** NodePort na porcie 80 → 5000

### Persistent Storage
FastAPI Pod wykorzystuje PersistentVolumeClaim (`fastapi-pvc`) do przechowywania danych.

## 🚨 Rozwiązywanie problemów

### Sprawdzenie logów
```bash
kubectl logs <pod-name>
```

### Restart deploymentu
```bash
kubectl rollout restart deployment/fastapi-deployment
```

### Usunięcie zasobów
```bash
kubectl delete deployment fastapi-deployment
kubectl delete service fastapi-service
kubectl delete service mlflow-service
```

## 📈 Monitoring

- **FastAPI:** Dostępne pod adresem serwisu
- **MLflow UI:** Dostępne przez przeglądarkę
- **Kubernetes Dashboard:** `minikube dashboard`

## 👥 Autorzy

Projekt stworzony w ramach nauki Kubernetes i Machine Learning.

## 📝 Licencja

Projekt edukacyjny - użyj zgodnie z własnymi potrzebami.
