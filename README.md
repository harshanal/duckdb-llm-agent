# Local LLM with DuckDB Integration

This project is based on a demonstration by Jeffrey Morgan, founder of [Ollama](https://ollama.com/), presented at the [Small Data SF](https://www.smalldatasf.com/) event. 

Watch the original talk on YouTube: [Running Small LLMs Locally – Jeffrey Morgan at Small Data SF](https://www.youtube.com/watch?v=P-55pV6ss3k)

## Features

- **Local LLM Execution**: Run LLMs directly on your machine without relying on external APIs.
- **Database Integration**: Query and retrieve data from a DuckDB database to provide context to the LLM.
- **Interactive Console**: Engage in a conversational interface where the LLM can process user queries and fetch relevant data from the database.

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Ollama**: Install Ollama to run LLMs locally. Download it from the [Ollama website](https://ollama.com/download).
- **DuckDB**: The Python package for DuckDB will be installed via the requirements file.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/harshanal/duckdb-llm-agent.git
   cd duckdb-llm-agent
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the DuckDB Database**:

   Run the script `create_duckdb.py` to generate the `ducks.duckdb` file with a sample table and data:

   ```bash
   python create_duckdb.py
   ```

5. **Run the Qwen Model Using Ollama**:

   Make sure Ollama is installed and running. Then, start the `qwen2.5-coder` model by running:

   ```bash
   ollama run qwen2.5-coder
   ```

   This will download the model (if not already downloaded) and make it available for the script to use.

6. **Run the Application**:

   ```bash
   python tools_demo.py
   ```

## Usage

Once the application is running, you can enter queries related to the `ducks` table. For example:

```
>>> How many ducks are in the database?
```

The LLM will interpret the query, generate the appropriate SQL command, execute it against the DuckDB database, and return the result.

### Example Output

```
>>> how many ducks are in the database
>>> tool_call: {'name': 'query', 'args': {'query': 'SELECT COUNT(*) AS duck_count FROM ducks'}, 'id': 'b54fdd6b-8b0a-41ae-89c2-ebe740760566', 'type': 'tool_call'}
>>> tool_output: 10
There are 10 ducks in the database.

>>> what color is Darth's shirt?
>>> tool_call: {'name': 'query', 'args': {'query': "SELECT color FROM ducks WHERE firstName = 'Darth';"}, 'id': '31a1e41e-1399-4fe3-9dc5-29addf523686', 'type': 'tool_call'}
>>> tool_output: black
Darth's shirt is black.

>>> what is the combined age of all the male ducks?
>>> tool_call: {'name': 'query', 'args': {'query': "SELECT SUM(age) FROM ducks WHERE gender = 'male';"}, 'id': '74d225c8-a24e-440e-95e3-d1a52d99c7f6', 'type': 'tool_call'}
>>> tool_output: 212
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

