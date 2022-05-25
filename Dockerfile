FROM python:slim

ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN:zh
ENV LC_ALL zh_CN.UTF-8
ENV CAPITAL_DC_A_ENV product
ARG project_dir=/projects/
WORKDIR $project_dir
ENV PYTHONPATH $project_dir

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./product.sh & chmod +x ./product_china.sh

EXPOSE 11002
ENTRYPOINT ["/bin/bash", "-c ./product_china.sh"]