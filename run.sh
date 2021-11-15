docker-compose down && docker-compose kill
docker volume rm database-management-project_frontend_volume
docker volume rm database-management-project_backend_volume
docker rmi database-management-project_backend
docker rmi database-management-project_frontend
docker-compose up -d --build
