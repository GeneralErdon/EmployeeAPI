FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN alembic upgrade head
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000