# --- Étape 1 : choisir l'image de base Python ---
FROM python:3.11-slim

# --- Étape 2 : définir le répertoire de travail ---
WORKDIR /app

# --- Étape 3 : copier les fichiers nécessaires ---
COPY requirements.txt ./
COPY app.py ./
COPY data/ ./data/

# --- Étape 4 : installer les dépendances ---
RUN pip install --no-cache-dir -r requirements.txt

# --- Étape 5 : exposer le port de Streamlit ---
EXPOSE 8501

# --- Étape 6 : commande par défaut pour lancer Streamlit ---
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
