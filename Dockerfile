FROM python:3-slim
EXPOSE 5000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]