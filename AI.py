import google.generativeai as genai


class GoogleGPT:
    """
    A class for interacting with the Google Gemini API using the google-generativeai library.
    """

    def __init__(self, api_key):
        """
        Initializes the GoogleGPT class with your API key.

        Args:
          api_key (str): Your Google API key.
        """
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel("gemini-pro")

    def send_message(self, prompt):
        """
        Sends a message (prompt) to the Gemini model and returns the generated response.

        Args:
          prompt (str): The message you want to send to the model.

        Returns:
          str: The generated response from the model.
        """
        try:
            response = self._model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

    def stream_responses(self, prompt):
        """
        Sends a message (prompt) to the Gemini model and yields responses as they are generated.

        Args:
          prompt (str): The message you want to send to the model.

        Yields:
          str: Each generated response from the model.
        """
        for response in self._model.generate_content(prompt, stream=True):
            try:
                yield response.text
            except Exception as e:
                print(f"{type(e).__name__}: {e}")


# Example usage:
if __name__ == "__main__":
    api_key = ""
    # Replace with your API key

    gpt = GoogleGPT(api_key)

    prompt = "Help me write a letter to my professor"
    response = gpt.send_message(prompt)
    print(response.to)

    # # Stream generated responses (useful for longer prompts)
    # for response in gpt.stream_responses("Write a short story about a robot who falls in love with a human."):
    #     print(f"Generated Text: {response}")
    #     # Implement logic to stop streaming if desired
    # response = gpt.generate_content("What is the meaning of life?", stream=True)
