# AI Medical Prescription Guidance System

A Retrieval-Augmented Generation (RAG) based healthcare assistant that provides context-aware medical information and prescription guidance through an interactive chatbot interface.

## Overview

The AI Medical Prescription Guidance System is an AI-powered healthcare assistant designed to help users retrieve relevant information about medicines, health conditions, treatments, and first-aid guidance.

The system uses a Retrieval-Augmented Generation (RAG) approach, where relevant information is retrieved from a medical knowledge base and provided to a Large Language Model (LLM) as context before generating a response.

This approach helps the system provide responses based on the available medical information rather than depending entirely on the model's internal knowledge.

The application provides an interactive chatbot interface using Gradio, allowing users to enter healthcare-related questions and receive context-aware responses.

## Key Features

- RAG-based medical information retrieval
- Semantic search over medical data
- Context-aware healthcare responses
- Medicine information retrieval
- First-aid and general healthcare guidance
- Medical document embeddings
- ChromaDB vector database
- LangChain-based RAG pipeline
- Local LLM execution using Ollama
- Automatic Ollama service detection and startup
- Automatic fallback between lightweight language models
- Medical-shop stock information support
- Interactive Gradio chatbot interface

## System Architecture

The system follows a Retrieval-Augmented Generation architecture:

```text
                         User Query
                             |
                             v
                    Gradio Chatbot UI
                             |
                             v
                      Query Processing
                             |
                             v
                    Semantic Retrieval
                             |
                             v
                     ChromaDB Vector DB
                             |
                             v
                Relevant Medical Information
                             |
                             v
                    LangChain RAG Pipeline
                             |
                             v
                       Ollama LLM
                             |
                             v
                    Generated Response
                             |
                             v
                    User / Chatbot UI
```

## How It Works

1. Medical information is stored in the project dataset.
2. The ingestion process reads the medical dataset.
3. Each medicine record is converted into descriptive text containing information such as medicine name, category, dosage form, strength, manufacturer, indication, classification, and stock.
4. The medical information is converted into vector embeddings using the `nomic-embed-text` embedding model.
5. The embeddings are stored in a ChromaDB vector database.
6. When a user submits a query, the system performs semantic similarity search.
7. The most relevant medical information is retrieved from ChromaDB.
8. The retrieved information is passed to the LangChain RAG pipeline.
9. The Ollama language model uses the retrieved context to generate a response.
10. The generated response is displayed through the Gradio chatbot interface.

## RAG Pipeline

The core RAG workflow is:

```text
Medical Dataset
      |
      v
Data Processing
      |
      v
Medical Text Documents
      |
      v
Nomic Embeddings
      |
      v
ChromaDB Vector Database
      |
      v
Semantic Similarity Search
      |
      v
Relevant Medical Context
      |
      v
LangChain RAG Chain
      |
      v
Ollama Language Model
      |
      v
Context-Aware Response
```

The application retrieves the top 5 relevant documents from the vector database using similarity search. 

## Project Structure

```text
Medical-Prescription-Guidance/
│
├── app.py
├── gradio_medical_chatbot.py
├── ingest.py
├── add_stock.py
├── test_db.py
│
├── data/
│   └── Medical datasets and knowledge-base files
│
├── requirements.txt
├── README.md
└── Lab Poject Document.pdf
```

## Runtime Files

### `app.py`

Contains the main RAG pipeline.

Responsibilities:

* Checks whether Ollama is running
* Starts Ollama automatically when required
* Loads the ChromaDB vector database
* Initializes the `nomic-embed-text` embedding model
* Performs similarity-based retrieval
* Loads the language model
* Creates the LangChain RAG chain
* Generates responses to user queries

The application uses Ollama embeddings and ChromaDB for semantic retrieval. 

### `gradio_medical_chatbot.py`

Provides the graphical chatbot interface using Gradio.

It connects the user interface to the RAG chain and displays the generated medical responses. 

The interface includes:

* Chatbot window
* User input box
* Send button
* Typing indicator
* Healthcare tips section
* Custom CSS styling

The application is launched using Gradio's sharing option. 

### `ingest.py`

Processes the medical dataset and creates the ChromaDB vector database.

The script extracts medicine-related fields including:

* Medicine Name
* Category
* Dosage Form
* Strength
* Manufacturer
* Indication
* Classification
* Stock

These records are converted into text and stored as embeddings in ChromaDB. 

### `add_stock.py`

Used for managing or updating stock-related information in the medical knowledge base.

### `test_db.py`

Used to test database retrieval and verify whether relevant information can be retrieved from the knowledge base.

## Technologies Used

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Core programming language             |
| LangChain        | RAG and application pipeline          |
| ChromaDB         | Vector database and similarity search |
| Ollama           | Local embedding and language models   |
| Nomic Embed Text | Medical document embeddings           |
| Gradio           | Interactive chatbot interface         |
| Pandas           | Dataset processing                    |
| Python-dotenv    | Environment configuration             |
| Git              | Version control                       |
| GitHub           | Source code management                |

The project dependencies include LangChain, ChromaDB, sentence-transformers, Streamlit, Pandas, Ollama, and Python-dotenv. 

## Language Models

The application attempts to load lightweight Ollama models automatically.

The preferred model order is:

```text
1. tinyllama
2. phi3:mini
3. llama3.2:1b
4. llama3.1:latest
```

If a model cannot be loaded because of system resource limitations, the application automatically attempts the next model in the list. 

The embedding model used for semantic retrieval is:

```text
nomic-embed-text
```

## Installation

### Prerequisites

Make sure the following are installed:

* Python 3.9 or later
* Git
* pip
* Ollama

### Clone the Repository

```bash
git clone https://github.com/USahu25/Medical-Prescription-Guidance.git
cd Medical-Prescription-Guidance
```

### Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install and Prepare Ollama Models

Install Ollama and make sure it is available in the system PATH.

The application uses Ollama locally and automatically checks whether the Ollama service is running. If it is not running, the application attempts to start it in CPU mode. 

The embedding model required by the project is:

```bash
ollama pull nomic-embed-text
```

A lightweight language model can also be downloaded, for example:

```bash
ollama pull tinyllama
```

## Creating the Knowledge Base

Before running the chatbot for the first time, create the ChromaDB vector database from the medical dataset.

Run:

```bash
python ingest.py
```

The ingestion script reads:

```text
data/medicine_dataset_with_stock.csv
```

and creates the persistent vector database in:

```text
chroma_db/
```

The database contains vector representations of the medical information for semantic retrieval.  

## Running the Application

Run the Gradio chatbot:

```bash
python gradio_medical_chatbot.py
```

The application will launch the Gradio interface and provide a URL that can be opened in a web browser.

The chatbot sends the user's question to the RAG chain and displays the generated response in the conversation interface. 

## Example Interaction

### User Query

```text
What should I do for a minor cut?
```

### System Workflow

```text
User Question
      |
      v
Semantic Search
      |
      v
Relevant Medical Information
      |
      v
LangChain RAG Pipeline
      |
      v
Ollama Language Model
      |
      v
Context-Aware Response
```

The system retrieves relevant information from the medical knowledge base and uses it as context while generating the response.

## Medical Information Retrieval

The medical knowledge base stores structured information about medicines.

Each record may contain:

```text
Medicine Name
Category
Dosage Form
Strength
Manufacturer
Indication
Classification
Stock
```

This information is converted into descriptive text before being embedded and stored in ChromaDB. 

This allows users to ask natural-language questions instead of searching the dataset manually.

## Database and Stock Management

The project includes functionality for medical-shop related information and stock management.

The stock information is included as part of the medical records used during retrieval.

This enables the system to provide relevant stock information when it is available in the retrieved context.

## Advantages

* Provides natural-language access to medical information
* Uses semantic search instead of simple keyword matching
* Grounds responses using retrieved medical information
* Uses a local LLM through Ollama
* Supports lightweight models for systems with limited resources
* Provides an interactive chatbot interface
* Can incorporate medicine stock information
* Allows the medical knowledge base to be updated

## Applications

* Medical information assistance
* First-aid guidance
* Medicine information retrieval
* Medical-shop assistance
* Healthcare education
* Academic research and experimentation with RAG systems
* Knowledge-base driven healthcare chatbots

## Important Safety Disclaimer

This project is intended for educational and informational purposes only.

It is not a replacement for a qualified doctor, pharmacist, or other healthcare professional.

The information generated by the system should not be considered a medical diagnosis or a substitute for professional medical advice.

Users should consult a qualified healthcare professional for:

* Diagnosis
* Prescription decisions
* Dosage information
* Serious or persistent symptoms
* Emergency medical conditions

The system should not be used to independently start, stop, or modify medication.

## Future Enhancements

* Improve medical knowledge-base coverage
* Improve retrieval accuracy
* Add source references to generated responses
* Add stronger medical response validation
* Add multilingual support
* Improve medical-shop inventory management
* Add structured prescription information
* Add medicine interaction checking
* Develop web and mobile deployment
* Add conversation history and personalized retrieval

## Project Documentation

Additional project documentation is available in:

```text
Lab Poject Document.pdf
```

The document contains additional information about the project, implementation, and system design.

## Contributors

**Sahithi**

## Acknowledgements

This project was developed as an academic project to explore:

* Retrieval-Augmented Generation
* Large Language Models
* Semantic Search
* Vector Databases
* LangChain
* Ollama
* AI-assisted healthcare information retrieval

## Repository

GitHub Repository:

[https://github.com/USahu25/Medical-Prescription-Guidance](https://github.com/USahu25/Medical-Prescription-Guidance)
```
