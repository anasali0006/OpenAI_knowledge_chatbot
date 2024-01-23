from openai.embeddings_utils import get_embedding
import openai


class OpenAIHandler:
    EMBEDDING_MODEL = "text-embedding-ada-002"

    with open("../openai_key.txt") as file:
        OPENAI_KEY = file.readline()

    openai.api_key = OPENAI_KEY

    @classmethod
    def generate_single_embedding(cls, input_text):
        """generate the embeddings of a single piece of text"""
        try:
            embedding = get_embedding(
                input_text,
                engine=OpenAIHandler.EMBEDDING_MODEL
            )
        except Exception as exp:
            raise Exception(exp)

        return embedding
