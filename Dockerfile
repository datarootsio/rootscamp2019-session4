FROM python:3.6.8
MAINTAINER Monkey To Complain To "complaints@here.rtfm"

COPY . /app
WORKDIR /app

EXPOSE 8080

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api_connexxion_fancypansy.py"]