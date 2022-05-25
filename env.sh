#!/usr/bin/env bash

ENV=$1

if [ ! ${ENV} ]; then
  ENV=local
fi

export CAPITAL_DC_A_ENV=${ENV} # 当前环境 可选 local product dev test product_china

# 生产环境:
# source env.sh product
# python app.py
