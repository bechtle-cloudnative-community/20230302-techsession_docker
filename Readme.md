# TechSession Docker - 03.02.2023
Welcome !

## Simple API for uploading Image

```
docker build -t myimage01:latest .
docker run -dp 80:8000 --name apidocker -v apivolume:/data myimage01
```

### Simple Compose-Stack

Build compose stack local:
```
docker-compose up -d
```
