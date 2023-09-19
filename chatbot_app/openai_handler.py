import openai


class OpenAIHandler:

    def generate_embeddings(self, input_json_object):
        """generate the embeddings of whole json object in a single go for now"""
