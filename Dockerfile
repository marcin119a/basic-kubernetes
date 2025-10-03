FROM python:3.11-slim

WORKDIR /app

# skopiuj kod
COPY main.py .
COPY train.py .

# instalacja zależności
RUN pip install fastapi uvicorn pandas scikit-learn

# wytrenuj model w trakcie builda (tworzy model.pkl)
RUN python train.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
