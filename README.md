# ecoquartier

## Install

On linux, run the following command

```
git clone https://github.com/ouhouhsami/ecoquartier
cd ecoquartier
docker-compose up
```

On OSX, run the following command

```
git clone https://github.com/ouhouhsami/ecoquartier
cd ecoquartier
docker-machine start ecoquartier
eval "$(docker-machine env ecoquartier)"
docker-machine ip ecoquartier
docker-compose up
```

Due to sync issues between containers, you may also need to migrate and create a superuser. See start_web.sh for more information.


If you want to recover data, fill the db with the appropriate dump

```
eval "$(docker-machine env ecoquartier)"
docker-compose run db /srv/data/backup/restore_db.sh
```

## Help on docker

Create a docker machine

```
docker-machine create --driver virtualbox --virtualbox-memory 8096 ecoquartier
```

List all docker machines

```
docker-machine ls
```

Stop a docker machine

```
docker-machine stop ecoquartier
```

Start a docker machine

```
docker-machine start ecoquartier
```
Set env variable the right way

```
eval "$(docker-machine env ecoquartier)"
```

To get the VM IP address

```
docker-machine ip ecoquartier
```

docker-compose

```
docker-compose build ecoquartier
docker-compose build --no-cache ecoquartier
docker-compose run ecoquartier command
docker-compose up ecoquartier
docker-compose stop
```

## initial step to load the data

docker-compose run web bash
cd /src
export DJANGO_SETTINGS_MODULE=ecoquartier.settings
python manage.py migrate


## PSQL

Shouldn't be needed

createdb ecoquartier
psql ecoquartier

DUMP data

docker-compose exec db bash
and inside container : pg_dump -C -c -O -x -U postgre postgre > test.sql
