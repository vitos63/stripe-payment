#!/bin/sh
cd backend
alembic upgrade head
cd ..
python -m backend.database.create_mock_products
exec uvicorn backend.main:app --host 0.0.0.0 --port 8000