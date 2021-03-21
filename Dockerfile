FROM python
WORKDIR /usr/src/app
COPY  ywai.py .
RUN python ywai.py