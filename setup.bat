python -m venv venv
call venv\Scripts\activate.bat

# assuming you have a local build of the Parlant
pip install ..\parlant\dist\parlant-1.7.0rc22-py3-none-any.whl
# or if you want to install parlant
pip install parlant

# export OPENAI_API_KEY=your-api-key

pip install parlant-client

pip install poetry
cd basic-client
poetry install
cd ..

cd tool-service
poetry install
cd ..
