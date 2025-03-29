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
>>> how many ducks are there in the database
>>> tool_call: {'name': 'query', 'args': {'query': 'SELECT COUNT(*) FROM ducks;'}, 'id': 'd011f318-ee30-4046-b37e-06c668171d52', 'type': 'tool_call'}
>>> tool_output: 3
There are 3 ducks in the database.

>>> What is the combined age of the ducks in the database?
>>> tool_call: {'name': 'query', 'args': {'query': 'SELECT SUM(age) AS total_age FROM ducks'}, 'id': 'c3de759d-be97-4012-b85e-db694698e36e', 'type': 'tool_call'}
>>> tool_output: 10
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

