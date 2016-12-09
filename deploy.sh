export REACT_APP_API_URL=sqwak.kingofthestack.com
(cd ./frontend/app; npm run build)
rm -rf ./nginx/www
mkdir ./nginx/www
cp -r ./frontend/app/build/ ./nginx/www/

scp ./docker-compose.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.yml
scp ./docker-compose.prod.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.prod.yml
scp ./docker-compose.override.yml root@sqwak.kingofthestack.com:/usr/src/app/docker-compose.override.yml

docker-compose build nginx
docker push sqwak/nginx

ssh root@sqwak.kingofthestack.com "cd /usr/src/app && docker pull sqwak/nginx && docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d"
