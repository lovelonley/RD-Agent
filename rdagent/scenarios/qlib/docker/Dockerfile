FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

# For GPU support, please choose the proper tag from https://hub.docker.com/r/pytorch/pytorch/tags

RUN apt-get clean && apt-get update && apt-get install -y \  
    curl \  
    vim \  
    git \  
    build-essential \
    coreutils \
    && rm -rf /var/lib/apt/lists/* 

# Copy local qlib source to avoid remote git clone failures
COPY ./qlib /workspace/qlib

WORKDIR /workspace/qlib

# No need to reset here as we already did it locally
# RUN git fetch && git reset 2fb9380b342556ddb50a4b24e4fe8655d548b2b8 --hard

RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade cython
RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -e .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple catboost
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xgboost
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tables
