FROM python:buster

RUN pip install selenium
RUN git clone https://github.com/youngsteryuan/PKUAutoSubmit.git /PKUAutoSubmit

COPY entrypoint.sh /entrypoint.sh
COPY entrypoint.py /PKUAutoSubmit/entrypoint.py
COPY msedgedriver.exe /PKUAutoSubmit/chromedriver/bin/msedgedriver.exe

ENTRYPOINT [ "/entrypoint.sh" ]
