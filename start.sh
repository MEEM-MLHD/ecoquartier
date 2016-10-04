docker-machine start ecoquartier
eval "$(docker-machine env ecoquartier)"
export URL='http://'$(docker-machine ip ecoquartier)
python -mwebbrowser $URL
docker-compose up