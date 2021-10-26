FROM python:buster

RUN pip install selenium
RUN git clone https://github.com/youngsteryuan/PKUAutoSubmit.git/PKUAutoSubmit

COPY entrypoint.sh /entrypoint.sh
COPY entrypoint.py /PKUAutoSubmit/entrypoint.py
COPY chromedriver.exe /PKUAutoSubmit/chromedriver/bin/chromedriver.exe

ENTRYPOINT [ "/entrypoint.sh" ]
