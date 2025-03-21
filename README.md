<a name="readme-top"></a>

<div align="center">
  <br/>
  <h3><b>RAGAPP - Retrieval Augmented Generation API</b></h3>
  <br/>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show Your Support](#support)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 RAGAPP <a name="about-project"></a>

**RAGAPP** is a REST API built with FastAPI, Python, and LangChain that leverages Retrieval Augmented Generation (RAG) to answer user queries using embeddings and contextual data. The application combines various data sources, including text embeddings stored with pgVector, to deliver context-aware responses.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>

<details>
  <summary>Database</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://www.pgvector.org/">pgVector</a></li>
  </ul>
</details>

<details>
  <summary>Libraries</summary>
  <ul>
    <li><a href="https://docs.langchain.com/">LangChain</a></li>
    <li><a href="https://pydantic-docs.helpmanual.io/">Pydantic</a></li>
    <li><a href="https://www.sqlalchemy.org/">SQLAlchemy/SQLModel</a></li>
  </ul>
</details>

### Key Features <a name="key-features"></a>

- **Contextualized Query Reformulation:** Uses chat history to generate standalone questions.
- **RAG Chains:** Combines retrieval and LLM chains for enhanced question answering.
- **pgVector Integration:** Stores and retrieves text embeddings from a PostgreSQL database using pgVector.
- **Modular Design:** Easily extend functionality with services and dependency injection.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

- [Live API Documentation](http://localhost:8000/docs) <!-- Update with actual URL if hosted -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites <a name="prerequisites"></a>

Ensure that you have the following installed:

- Python 3.13
- [PostgreSQL](https://www.postgresql.org/) with pgVector extension enabled
- Virtual environment tool (e.g., venv)

### Setup <a name="setup"></a>

Clone this repository to your desired folder:

```sh
cd path/to/your-folder
git clone https://github.com/your-username/RAGAPP.git
```

### Install <a name="install"></a>

1. Create and activate your virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file at the root of the project with the following variables:

```env
# Database configuration
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>

# OpenAI API key for LangChain integration
OPENAI_API_KEY=your_openai_api_key

# Other configuration variables
FIRECRAWL_API_KEY=''
TRELLO_API_KEY = ''
TRELLO_TOKEN =''
# ...
```

### Usage <a name="usage"></a>

To run the project locally, use the following command:

```sh
fastapi dev src/dev
```

Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Ambrose Kibet**

- GitHub: [ambrose-kibet](https://github.com/ambrose-kibet)
- Twitter: [@ambrose_kibet](https://twitter.com/ambrose_kibet)
- LinkedIn: [Ambrose Kibet](https://linkedin.com/in/ambrose-kibet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] **Unit and E2E Tests**
- [ ] **Advanced Query Optimization**
- [ ] **Enhanced Retrieval Mechanisms**
- [ ] **Custom Authentication and Authorization**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/your-username/RAGAPP/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show Your Support <a name="support"></a>

If you like this project, please give it a star ⭐️.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
