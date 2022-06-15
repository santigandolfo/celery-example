#!/bin/sh
watchmedo auto-restart -d . -p '*.py' -R -- celery -A worker.queue worker --loglevel=INFO
