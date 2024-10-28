This folder contains all of the deep learning functionality of the program.

Additionally, it contains the way in which finance data is downloaded and used for training and prediction of stocks.

The main.py program is what runs all of the other files. To download certain stocks to use for training, include the given stock in the tickers list.
Once that us done, run the main.py file to train the model on that stock data.

The llm.py file contains a simple LLM from HuggingFace where a user can prompt the model and return what the model generates. Simply change the prompt and run the llm.py file.
Do note that this will later be exchanged for the OpenAI API to include more advance LLMs.