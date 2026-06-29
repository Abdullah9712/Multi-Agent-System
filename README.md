# Multi-Agent-System

A modular **Python-based Multi-Agent System** that automates the complete research workflow using specialized AI agents. The system accepts a user query, performs web research, cleans and structures the collected information, and generates a professional PDF report.

This project demonstrates the concept of **Multi-Agent Systems (MAS)**, where multiple AI agents collaborate to accomplish a complex task while maintaining clear separation of responsibilities. Each agent performs a dedicated task and passes its output to the next stage of the workflow.


## Features

* Automated web research based on user queries
* Modular multi-agent architecture
* Intelligent data cleaning and formatting
* Professional PDF report generation
* PowerPoint export support
* JSON-based communication between agents
* Web searching and webpage fetching
* Execution logging for debugging
* Secure API key management using `.env`
* Easily extendable architecture for adding new agents


# System Architecture

```text
                    User Input
                        │
                        ▼
                Research Agent
                        │
                        ▼
                Raw Research Data
                        │
                        ▼
                Cleaning Agent
                        │
                        ▼
               Structured JSON Data
                        │
                        ▼
               Formatting Agent
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
        PDF Report          PowerPoint (Optional)
```

# Project Structure

```text
Multi-Agent-System/
│
├── agents/
│   ├── research_agent.py
│   ├── cleaning_agent.py
│   └── formatting_agent.py
│
├── data/
│   ├── input/
│   ├── raw/
│   └── cleaned/
│
├── logs/
│   └── system.log
│
├── output/
│   └── research_report.pdf
│
├── utils/
│   ├── api_client.py
│   ├── export_pdf.py
│   ├── export_ppt.py
│   ├── file_handler.py
│   ├── helpers.py
│   ├── web_search.py
│   └── webpage_fetcher.py
│
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

# Getting Started

## Prerequisites

Before running the project, ensure you have:

* Python **3.10** or above
* pip
* Git
* Gemini API Key


## Clone the Repository

```bash
git clone https://github.com/Abdullah9712/Multi-Agent-System.git

cd Multi-Agent-System
```


## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```


## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a file named **`.env`** in the project root.

Example:

```env
GEMINI_API_KEY=your_api_key_here
MODEL=gemini-2.5-flash
```

> **Important:** Never upload your `.env` file to GitHub. The `.gitignore` file already excludes it from version control.


# Running the Project

Start the application using:

```bash
python main.py
```

When prompted, enter any research topic.

Example:

```text
Enter your topic:

Artificial Intelligence
```

The system will automatically:

1. Perform web research
2. Collect relevant sources
3. Clean and organize the information
4. Generate a professional PDF report
5. Save intermediate JSON files


# Agents

## Research Agent

Responsible for:

* Receiving the user's query
* Searching the web
* Fetching webpage content
* Collecting source references
* Saving raw research data


## Cleaning Agent

Responsible for:

* Removing duplicate information
* Organizing content
* Creating structured JSON output
* Preparing data for formatting


## Formatting Agent

Responsible for:

* Formatting the cleaned data
* Creating a professional PDF report
* Exporting PowerPoint presentations (optional)


# Data Flow

```text
User Input
     │
     ▼
Research Agent
     │
     ▼
data/raw/
     │
     ▼
Cleaning Agent
     │
     ▼
data/cleaned/
     │
     ▼
Formatting Agent
     │
     ▼
output/research_report.pdf
```


# Technologies Used

* Python
* Gemini API
* ReportLab
* python-dotenv
* DuckDuckGo Search
* JSON
* Markdown

---

# Generated Output

The project automatically generates:

* Raw research data
* Cleaned JSON data
* System logs
* Professional PDF report
* PowerPoint presentation (if enabled)



# Security

Sensitive files are excluded using `.gitignore`, including:

* `.env`
* Virtual environments
* Logs
* Generated reports
* Cache files
* Temporary files

This helps keep API keys and other credentials secure.


# Future Improvements

* Web interface using Flask/FastAPI
* Streamlit dashboard
* Parallel execution of agents
* Memory-enabled agents
* Retrieval-Augmented Generation (RAG)
* Vector database integration
* Docker support
* Cloud deployment
* REST API integration



# Contributing

Contributions are welcome!

If you'd like to contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Please ensure your code is well-documented and tested before submitting.


# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more details.



# Author

**Abdullah**

Artificial Intelligence Student

GitHub: **https://github.com/Abdullah9712**

Repository:

**https://github.com/Abdullah9712/Multi-Agent-System**



## Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It helps support the project and encourages future development.
