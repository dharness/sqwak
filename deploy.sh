export REACT_APP_API_URL=localhost
(cd ./frontend/app; npm run build)
rm -rf ./nginx/www
mkdir ./nginx/www
cp -r ./frontend/app/build/ ./nginx/www/

scp ./docker-compose.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.yml
scp ./docker-compose.prod.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.prod.yml
scp ./docker-compose.override.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.override.yml
