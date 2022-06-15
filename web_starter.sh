#!/bin/sh
uvicorn "web_service.web_service_app:app" --host=0.0.0.0 --port=8000 --reload
