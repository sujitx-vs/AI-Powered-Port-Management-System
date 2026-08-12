import ollama


class LLMService:

    def __init__(self):

        self.model = "qwen2.5:7b"

        print(f"Loaded LLM: {self.model}")

    def generate(self, prompt):

        stream = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
        )

        full_response = ""

        for chunk in stream:

            content = chunk["message"]["content"]

            print(content, end="", flush=True)

            full_response += content

        print()

        return full_response

    def generate_stream(self, prompt):

        stream = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
        )

        for chunk in stream:
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content