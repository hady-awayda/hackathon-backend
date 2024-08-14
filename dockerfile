# Build stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY config/requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .

# Final stage
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app .

ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
