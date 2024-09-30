from dotenv import load_dotenv
from pathway.udfs import DiskCache, ExponentialBackoffRetryStrategy
from pathway.xpacks.llm import embedders, llms, parsers, splitters
from pathway.xpacks.llm.question_answering import BaseRAGQuestionAnswerer
from pathway.xpacks.llm.vector_store import VectorStoreServer
import os
import logging
import click
import pathway as pw
import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

load_dotenv()

def data_sources(source_configs) -> list[pw.Table]:
    sources = []
    for source_config in source_configs:
        for filename in os.listdir(source_config['config']['path']):
            file_path = os.path.join(source_config['config']['path'], filename)
            source = pw.io.fs.read(
                file_path,
                format="binary",
                with_metadata=True,
            )
        sources.append(source)

    return sources

@click.command()
@click.option("--config_file", default="config.yaml", help="Config file to be used.")
def run(config_file: str = "config.yaml"):
    with open(config_file) as config_f:
        configuration = yaml.safe_load(config_f)

    LLM_MODEL = configuration["llm_config"]["model"]

    embedding_model = "avsolatorio/GIST-small-Embedding-v0"

    embedder = embedders.SentenceTransformerEmbedder(
        embedding_model,
        call_kwargs={"show_progress_bar": False}
    )

    chat = llms.LiteLLMChat(
        model=LLM_MODEL,
        retry_strategy=ExponentialBackoffRetryStrategy(max_retries=6),
        cache_strategy=DiskCache(),
    )

    host_config = configuration["host_config"]
    host, port = host_config["host"], host_config["port"]

    doc_store = VectorStoreServer(
        *data_sources(configuration["sources"]),
        embedder=embedder,
        splitter=splitters.TokenCountSplitter(max_tokens=400),
        parser=parsers.ParseUnstructured(),
    )

    rag_app = BaseRAGQuestionAnswerer(llm=chat, indexer=doc_store)

    rag_app.build_server(host=host, port=port)

    rag_app.run_server(with_cache=True, terminate_on_error=False)

if __name__ == "__main__":
    run()