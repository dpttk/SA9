
echo "Starting Docker Compose for pipes ..."

docker compose up -d
if [ $? -ne 0 ]; then
    echo "Error: Failed to start Docker Compose services."
    exit 1
fi

sleep 40
while true; do
    sleep 3
    RUNNING_CONTAINERS=$(docker ps -q --filter "status=running")
    TOTAL_CONTAINERS=$(docker compose ps -q | wc -l)
    RUNNING_COUNT=$(echo "$RUNNING_CONTAINERS" | wc -l)
    
    if [ "$RUNNING_COUNT" -eq "$TOTAL_CONTAINERS" ]; then
        echo "All containers are running."
        break
    fi
    sleep 2
done

sleep 5

echo "Docker Compose services started."

bash ../spam.sh 100 > /dev/null &
docker stats --no-stream >> docker_resource_usage.txt

sleep 5

for ((i = 1; i <= 15; i++)); do
    echo "Running spam.sh..."
    START_TIME=$(date +%s%4N)
    bash ../spam.sh 100 > /dev/null 
    END_TIME=$(date +%s%4N)
    TIME_TAKEN=$((END_TIME - START_TIME))
    echo " " >> docker_resource_usage.txt
    echo "spam.sh completed in $TIME_TAKEN." >> docker_resource_usage.txt
done

IS_RUNNING=$(docker ps -q --filter "id=$CONTAINER_ID")
if [ -n "$IS_RUNNING" ]; then
    echo "Docker container is still running."
else
    echo "Docker container is no longer running."
fi
docker compose down
# Cleanup and output results
echo "Process completed. Docker resource usage and script execution time recorded."
