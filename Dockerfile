FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask requests urllib3

# Copy application files
COPY html/proxy.py html/solar_dashboard.html ./

EXPOSE 5000

# Use gunicorn for production, fall back to Flask dev server
RUN pip install --no-cache-dir gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "30", "proxy:app"]
