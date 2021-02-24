FROM python:3.9.1

#avoid to create __pycache__
ENV PYTHONDONTWRITEBYTECODE 1
#pass through package
ENV PYTHONPATH /home/$git_repo_name/package:$PYTHONPATH

RUN mkdir -p /home/$git_repo_name

COPY requirements.txt /home

RUN pip install --upgrade pip &&\
    pip install -r /home/requirements.txt &&\
    rm /home/requirements.txt

WORKDIR /home/$git_repo_name

CMD [ "/bin/bash" ]