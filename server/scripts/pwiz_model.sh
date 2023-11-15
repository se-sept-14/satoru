#!/bin/bash
python -m pwiz --host=18.136.102.74 --port=3306 --user=root -P --engine=mysql recommender_system > ../models/db_models.py