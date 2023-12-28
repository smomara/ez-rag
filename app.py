from flask import Flask, request, jsonify, redirect, render_template
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

global_query_engine = None
global_index = None

@app.route('/upload', methods=['POST'])
def upload_document():
    global global_query_engine
    global global_index

    file = request.files['file']
    if file:
        file_path = os.path.join('data', file.filename)
        file.save(file_path)

        document = SimpleDirectoryReader("data").load_data()

        global_index = VectorStoreIndex.from_documents(document)
        global_query_engine = global_index.as_query_engine()
    
        return redirect('/')
    else:
        return 'No file uploaded', 400
    
@app.route('/query', methods=['POST'])
def query_prompt():
    global global_query_engine

    if global_query_engine is None:
        return 'Query engine not available. Upload a document first.', 400

    data = request.get_json()
    prompt = data.get('prompt', '')

    response = global_query_engine.query(prompt)
    print(response)
    print(type(str(response)))
    print(str(response))

    return jsonify({'response': str(response)}), 200

@app.route('/clear', methods=['GET'])
def clear_data():
    global global_query_engine
    global global_index

    global_query_engine = None
    global_index = None

    data_directory = 'data'
    for file_name in os.listdir(data_directory):
        file_path = os.path.join(data_directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    return 'Data cleared', 200

@app.route('/files', methods=['GET'])
def get_files():
    data_directory = 'data'
    files = [file_name for file_name in os.listdir(data_directory) if os.path.isfile(os.path.join(data_directory, file_name))]
    return jsonify({'files': files}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)