# Separate build image
FROM python:3.11-slim-buster as compile-image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Final image
FROM python:3.11-slim-buster
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /usr/src/app/
COPY ./bot/ /usr/src/app/bot/
ENTRYPOINT ["python", "-m", "bot"]