FROM python

WORKDIR /opt/build

ADD requirements.txt .

RUN pip install -r requirements.txt


#RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

