python -m venv venv
call venv\Scripts\activate.bat

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
