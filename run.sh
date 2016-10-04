docker-machine start ecoquartier
eval "$(docker-machine env ecoquartier)"
docker-compose run -e DJANGO_SETTINGS_MODULE=ecoquartier.settings -w /src web bash