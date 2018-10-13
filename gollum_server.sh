#!/usr/bin/env bash

cd docs;

gollum --live-preview --allow-uploads page &

sleep 2; 

atom . ../
open http://127.0.0.1:4567/
