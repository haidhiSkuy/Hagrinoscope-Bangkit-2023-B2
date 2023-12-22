# Hagrinoscope Bangkit 2023 Capstone Project

The project has two different models:
* Fruit maturity classifier: this model can classify 10 different maturity levels from different four fruits.
* Soil types classifier: this model can classify five different types of soils

The models can be downloaded from this [URL](https://drive.google.com/file/d/1CvyAopRxwlCu4i0bQ2k7_lvX3-G5owUj/view?usp=sharing)

 
## Application and API Architecture
<img src="https://github.com/haidhiSkuy/Hagrinoscope-Bangkit-2023-B2/assets/118953030/3a0c45a8-8dac-4812-a4b8-4bb165612e6d" alt="drawing" style="width:700px;"/>


## Docker Image Usage
```console 
root@ubuntu:~$ docker build -t hagrinoscope/ml .
root@ubuntu:~$ docker container create --name api --publish 8080:80 hagrinoscope/ml
root@ubuntu:~$ docker container start api
```

## API Test with Python 
```python 
multiple_files = [
    ('files', ('banana.jpg', open('banana.jpg', 'rb'), "multipart/form-data")),
    ('files', ('yellow.jpg', open('yellow.jpg', 'rb'), "multipart/form-data"))
]

endpoint = "http://0.0.0.0:8080/predict/"

r = requests.post(endpoint, files=multiple_files)
recommendation = r.json()
```
