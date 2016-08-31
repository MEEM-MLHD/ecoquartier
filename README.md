# <project_name>

## Install

On linux, run the following command

```
$ git clone https://github.com/ouhouhsami/<project_name>
$ cd <project_name>
$ docker-compose up
```

Due to sync issues between containers, you may also need to migrate and create a superuser. See start_web.sh for more information.


If you want to recover data, fill the db with the appropriate dump

```
$ eval "$(docker-machine env <project_name>)"
$ docker-compose run db /srv/data/backup/restore_db.sh
```

## Help on docker

Create a docker machine

```
$ docker-machine create --driver virtualbox --virtualbox-memory 8096 <project_name>
```

List all docker machines

```
$ docker-machine ls
```

Stop a docker machine

```
$ docker-machine stop <project_name>
```

Start a docker machine

```
$ docker-machine start <project_name>
```
Set env variable the right way

```
$ eval "$(docker-machine env <project_name>)"
```

To get the VM IP address

```
$ docker-machine ip <project_name>
```

docker-compose

```
$ docker-compose build <project_name>
$ docker-compose build --no-cache <project_name>
$ docker-compose run <project_name> command
$ docker-compose up <project_name>
$ docker-compose stop
```

## PSQL

createdb ecoquartier
psql ecoquartier

