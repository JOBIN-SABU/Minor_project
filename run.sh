#!/bin/bash

echo "Starting Backend..."
cd Backend
python3 -m uvicorn api:app --reload &

sleep 3

echo "Starting React Frontend..."
cd ../Frontend
npm start