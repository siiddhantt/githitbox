#!/bin/bash

# GitHitBox Deployment Script

echo "🚀 Deploying GitHitBox..."

git pull origin master

docker-compose down
docker-compose build --no-cache
docker-compose up -d

echo "✅ GitHitBox deployed successfully!"
echo "🌐 Service running at: http://localhost:8000"
echo "📊 Health check: http://localhost:8000/health"
echo "🔍 Logs: docker-compose logs -f githitbox"

docker-compose ps
