# FAQ_answering
Answer user queries with information from a faq.csv file with a lot of question and answers data.

## Watch the Demo Video

[![Watch the video](https://img.youtube.com/vi/oHY1MpOoJeE/maxresdefault.jpg)](https://www.youtube.com/watch?v=oHY1MpOoJeE)


How to run this application for linux (or windows with wsl):

Step 1:
go to any freshly created folder and clone this git repository with "git clone https://github.com/PreethamGunta/FAQ_answering"

Step 2:
put the gemini api key into the .env file
modify the path in config.yaml to the folder with the documents or put the documents in the data folder.

step 3:
build the docker image with "docker build -t rag ."

step 4:
Run the docker container with "docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env rag"

step 5:
Run the RAG service by asking questions by "curl -X 'POST' 'http://0.0.0.0:8000/v1/pw_ai_answer' -H 'accept: */*' -H 'Content-Type: application/json' -d '{
  "prompt": "How to Reset my password?"
}'"
