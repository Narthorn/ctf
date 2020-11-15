#!/bin/bash
for i in {1..1000}; do curl https://www.challengecybersec.fr/9bcb53d26eab7e9e08cc9ffae4396b48/blog/post/$i 2>&- | grep message-digest | sed "s#.*proof\">\(.*\)<.*#\1#"; done | tr -d "\n" | md5sum
