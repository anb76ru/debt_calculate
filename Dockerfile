FROM python:latest
ARG BRANCH=main
ENV GITHUB_TOKEN=123
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

RUN git config --global http.postBuffer 524288000
RUN git config --global core.compression 0
RUN git config --global http.version HTTP/1.1
RUN git clone --branch ${BRANCH} https://github.com/anb76ru/debt_calculate.git
WORKDIR /anb76ru/debt_calculate

ENTRYPOINT yes | buildozer android debug
CMD dpl releases --token ${GITHUB_TOKEN} --file "bin/DebtCalculate-${BRANCH}-arm64-v8a-debug.apk" --tag_name ${BRANCH}