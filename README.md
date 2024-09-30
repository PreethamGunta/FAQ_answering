# FAQ_answering
This Retrieval-Augmented Generation (RAG) application is designed to provide accurate, contextually relevant answers to frequently asked questions (FAQs) for businesses across various industries. By leveraging large language models (LLMs) and a retrieval mechanism, the application enhances the quality of responses by integrating real-time information from specific company databases or knowledge sources.

Businesses automating customer support or internal knowledge management can streamline information retrieval across sectors like finance, healthcare, and e-commerce. The application reduces workload, ensures consistent responses, and scales efficiently by combining LLM-generated language with real-time data retrieval for accurate, relevant answers.

## Watch the Demo Video

[![Watch the video](https://img.youtube.com/vi/oHY1MpOoJeE/maxresdefault.jpg)](https://www.youtube.com/watch?v=oHY1MpOoJeE)


Running the Application on Linux (or Windows with WSL):

1)Navigate to a new folder and clone the repository:

git clone https://github.com/PreethamGunta/FAQ_answering

Add your Gemini API key to the .env file. Then, either update the config.yaml file to point to your document folder or place the documents in the data folder.


2)Build the Docker image:

docker build -t rag .


3)Run the Docker container:

docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env rag


4)Use the RAG service by sending a question with the following curl command:

curl -X POST 'http://0.0.0.0:8000/v1/pw_ai_answer' \
-H 'accept: */*' \
-H 'Content-Type: application/json' \
-d '{
  "prompt": "How do I reset my password?"
}'
