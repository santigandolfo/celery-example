#!/bin/sh
celery -A worker.worker_app worker --loglevel=INFO
