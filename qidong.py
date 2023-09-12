import interpreter
import openai
openai.api_key = "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"
interpreter.model = "gpt-3.5-turbo"
interpreter.chat("Plot AAPL and META's normalized stock prices") # Executes a single command
interpreter.chat() # Starts an interactive chat