FROM python:latest
WORKDIR /anb76ru
# COPY ./debt_calculate ./debt_calculate
RUN git clone https://github.com/anb76ru/debt_calculate.git
RUN cd debt_calculate
RUN git checkout anb76ru/mobile_app
