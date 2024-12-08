# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

# script to test the chat box functionality

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from text_generator import process_question

def test_process_question():
    question_with_ticker = "What is the current price of AAPL?"
    question_without_ticker = "Tell me more about stocks in general."

    print("Test process_question with ticker:")
    print(process_question(question_with_ticker))  # Expected to return AAPL stock info

    print("\nTest process_question without ticker:")
    print(process_question(question_without_ticker))  # Expected to ask for a valid ticker symbol

# Run the test
if __name__ == "__main__":
    test_process_question()
