#!/bin/bash

for i in {1..9}
do
	cd lab0${i}/distribute
	docker-compose build
	docker-compose up -d
	cd ../..
done
