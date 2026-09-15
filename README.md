# tecweb-2026-2-projeto1B

docker run --rm --name pg-docker \
  -e POSTGRES_PASSWORD=escolhaumasenha \
  -d \
  -p 5432:5432 \
  -v "$HOME/docker/volumes/postgres:/var/lib/postgresql/data" \
  postgres
