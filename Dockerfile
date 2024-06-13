FROM python:3.11.5
ARG BRANCH=main
ENV GITHUB_TOKEN=123

RUN echo "===Устанавливаем зависимости==="

RUN apt-get update && apt install -y \ 
    ruby-dev \
    default-jre \
    cmake \ 
    openjdk-17-jdk \
    git \
    zlib1g-dev

WORKDIR /anb76ru
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/.local/bin
RUN pip install buildozer==1.5.0
RUN pip install cython

RUN gem install \
    dpl --pre \
    bundler
RUN gem install uri
RUN gem install net-http

RUN echo "===Выкачиваем ветку ${BRANCH} репозитория==="

RUN git clone --branch ${BRANCH} https://github.com/anb76ru/debt_calculate.git
WORKDIR /anb76ru/debt_calculate

RUN echo "===Запуск компиляции приложения==="

RUN yes | buildozer android debug

ENTRYPOINT dpl releases --token ${GITHUB_TOKEN} --file 'bin/DebtCalculate-${BRANCH}-arm64-v8a-debug.apk' --tag_name ${BRANCH}