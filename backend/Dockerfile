FROM python:3.10.9
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --upgrade pip -r requirements.txt
COPY . /backend
ENV PORT=3333
EXPOSE 3333
