#!/bin/bash

for i in {1..9}
do
	cd lab0$i/distribute
	docker-compose down
	cd ../..
done
