#!/bin/bash

N=$1
text=$2

for ((i = 1; i <= N; i++)); do
    curl -w "Time: %{time_total}s\n" -o /dev/null -s " localhost:8000/message/" -d '{"alias": "test", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque aliquam turpis nec purus ullamcorper, nec pretium sapien viverra. Ut malesuada nisi ac venenatis ultrices. Duis fringilla rhoncus lectus a congue. Duis ac sapien lorem. Donec luctus scelerisque massa eget pellentesque. Aenean sit amet suscipit odio. Donec feugiat, arcu gravida aliquam tristique, velit nisi interdum ante, sed bibendum lorem est nec dui. Praesent malesuada porttitor odio, et dictum ex faucibus vitae. Nam et diam quis felis ullamcorper rutrum non elementum tellus. Morbi sed semper ligula. Donec dictum purus id leo viverra, vel tempor metus dictum. Suspendisse scelerisque aliquam elit et finibus. Nulla dapibus et leo non ultrices. Fusce sed bibendum tellus. Nunc scelerisque tellus non urna mattis consectetur"}' -H 'content-type: application/json'
    echo "1"
done