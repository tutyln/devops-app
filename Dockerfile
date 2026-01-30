# 1️⃣ Hangi ortamdan başlıyoruz?
FROM python:3.11-slim

# 2️⃣ Container içinde çalışma dizini
WORKDIR /app

# 3️⃣ Bağımlılık dosyasını kopyala
COPY requirements.txt .

# 4️⃣ Python paketlerini kur
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Uygulama kodunu kopyala
COPY app.py .

# 6️⃣ Container ayağa kalkınca çalışacak komut
CMD ["python", "app.py"]
