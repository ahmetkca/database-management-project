docker-compose down && docker-compose kill
docker-compose down --rmi all
docker volume rm database-management-project_frontend_volume
docker volume rm database-management-project_backend_volume
docker-compose up -d --build
