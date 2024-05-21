# LLM-RAG-Chroma-Prompt :speech_balloon:
This repository belongs to the trial project given by Gaditek for the Test Purposes. Syed Umaid has written this code in a way to run it through dual functionality (Local Database with llama and Chroma) Seperately

# Project Title

Objective is to create a simple Q/A bot by using RAG technique in an LLM like OpenAI Llama or Mistral. Create a simple Q/A bot that will answer user's
questions from a given knowledge. To store the knowledge use Vector Database and embeddings. Use LLM to answer user questions in natural language.


## Getting Started
Developers have divided the Tasks into three main Sections 

### Prerequisites

You need to have an OpenAI key for the purpose of generating embeddings. While running the code, in order to save the Key for Public Disposal. First Create the Environment. Then Save the Key There.

```
nano .env
OPEN_AI_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Installing

A step by step series of examples that tell you how to get a development-env running

Make the Virtual Environment with Version of Python=3.9. Run the "requirements.txt" file in the Virtual Environment

```
pip install -r requirements.txt
```



## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### Prompting/Coding style For the Exact Similar Output in Trial Examination Questionarre

From llama_index.core we have used the Prompt Library in order to design the Prompt in the Desired Format.
The "qa_template" used is producing the outputs in the required format as requested in the paper sample.


```
    template = (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question and each question should start with the word User: and each answer should start with code word Bot: {query_str}\n"
    )

```

## Data Ingestion of Content

The two PDF's are used for guiding the developed Chatbot. The PDF's are available in the "Data folder"

## Built With

* [OpenAI](http://www.dropwizard.io/1.0.2/docs/) - To Generate the Embeddings
* [LLAMA](https://docs.llamaindex.ai/en/stable/) - For RAG and Local Storage Functions

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Syed Umaid Ahmed** - *Initial work* - [Researcher](https://github.com/SyedUmaidAhmed)


## License

This project is licensed under the Free License - To Test and Reproduce the Results

