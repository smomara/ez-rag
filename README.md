# ez-rag: Easy Resource Querying

ez-rag is a project that simplifies the process of updating doucments to be used as sources for LLM queries. The primary use case I am exploring is creating a homework helper that leverages RAG with LLMs to answer questions based on the content of uploaded PDF or text files, such as textbooks. Feel free to tinker with it however you want.

This project is very much rudimentary and needs a lot of refactoring for actual usability.

## Getting Started
To use ez-rag, follow these steps:
```bash
# Clone the repository
git clone https://github.com/smomara/ez-rag.git
# Enter the repository
cd ./ez-rag
# Create a .env file
touch .env
# Add your OpenAI API key
cat "OPENAI_API_KEY=your_openai_api_key > .env # replace with your actual OpenAI API key
# Create the data folder
mkdir data
# Run the application
python app.py
```
This will start the application, which will be accesible at http://localhost:5000

## Usage
1. Upload a document
- Visit the locally hosted site and upload a PDF or text file of the textbook or document that you want to use as a source
2. Ask questions
- After uploading the document, submit question or prompts
3. Explore results
- Review the AI-generated responses and extract valuable information from the document

You can upload multiple files as source data. The source data will automatically be cleared when the you leave the site, but you can also clear the source data with the "Clear Data" button.