FROM python:3.10.9

#Set working directory
WORKDIR /src

#Copy requirements
COPY requirements.txt requirements.txt
COPY ./src ./src


#install dependancy
RUN pip install -r requirements.txt
RUN pip install ./bark
RUN pip uninstall -y torch torchvision torchaudio
RUN pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu118

