FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
# local image 
RUN mkdir /app && cd /app && mkdir pwh_docker
COPY ./ /app/phw_docker 
# git image
# RUN mkdir /app && cd /app && git clone https://github.com/jchorley/phw_docker.git 
# RUN cd /app/phw_docker && git pull
WORKDIR /app/phw_docker
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]