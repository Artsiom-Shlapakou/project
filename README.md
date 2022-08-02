## Run

```sh
docker-compose up -d --build
docker ps (find out id web-api container docker )
docker exec -it <id_container>  python manage.py createsuperuser
```