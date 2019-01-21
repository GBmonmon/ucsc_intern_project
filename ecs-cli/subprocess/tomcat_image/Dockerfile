FROM tomcat:8
RUN apt-get update -y && apt-get install -y python3-pip && \
    pip3 install package_name

RUN mkdir /code 
ADD . /code
WORKDIR /code
#RUN pip3 install -r /code/subprocess/requirements.txt
RUN apt install vim -y
RUN pip3 install mysql-connector-python

