# Azure Environment of DevSecNinja

Welcome! This project contains an API that returns a resource name based on a naming convention.

## Instructions

To run the Python script based on FastAPI locally, run the following:

```` bash
python -m venv ./venv
./venv/bin/python -m pip install -r ./requirements.txt
source ./venv/bin/activate && uvicorn main:app --reload
````

After running this once, you can run the `Run app locally` task. To view the automatically generated API documentation based on OpenAPI (formerly Swagger), go to: `http://127.0.0.1:8000/docs`

## CI / CD Status - develop

### Linter (develop)

[![GitHub Super-Linter](https://github.com/DevSecNinja/NamingConventionApi/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)
