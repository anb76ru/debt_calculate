команды для деплоя apk в гитхаб
docker run --rm -it python:latest bash
git clone https://github.com/anb76ru/debt_calculate.git
git checkout anb76ru/mobile_app
apt-get update
apt-get install ruby-dev
gem install dpl --pre
export GITHUB_TOKEN=
gem install bundler
docker cp DebtCalculate-0.0.1-arm64-v8a-debug.apk 5ca482122ec2:/debt_calculate/bin

mkdir anb76ru
mv debt_calculate/ anb76ru/
cd anb76ru/debt_calculate
dpl releases --token $GITHUB_TOKEN --file "bin/DebtCalculate-0.0.1-arm64-v8a-debug.apk" --tag_name "v.0.0.1"


docker run --rm -e GITHUB_TOKEN='123' debt_calculate:0.0.2
docker build --no-cache --build-arg="BRANCH=rc-0.0.2" -t debt_calculate:0.0.2 .