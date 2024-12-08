# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

import re
from transformers import pipeline
from .recommendation import recommend_stocks
from .models import TextGenerationModel, StockAnalyzer
from .services import model_service

generator = pipeline("text-generation", model="gpt2")  # gpt2 used to generate the text 

def generate_text(prompt, max_length=150):
    try:
        generated = generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=generator.tokenizer.eos_token_id
        )
        return generated[0]['generated_text']
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return prompt

def process_question(question):
    analyzer = model_service.stock_analyzer
    
    tickers = re.findall(r'\b[A-Z]{1,5}\b', question)
    
    if 'price' in question.lower():
        responses = []
        for ticker in tickers:
            stock_info = StockAnalyzer.get_stock_info(ticker)
            if stock_info:
                responses.append(f"The current price of {ticker} is {stock_info['current_price']}")
        return " ".join(responses) if responses else "Could not find stock price information."
        
    elif 'analyze' in question.lower() or 'analysis' in question.lower():
        responses = []
        for ticker in tickers:
            analysis = analyzer.analyze_stock(ticker)
            responses.append(analysis)
        return " ".join(responses) if responses else "Could not perform analysis."
        
    elif 'recommend' in question.lower() or 'tell' in question.lower():
        try:
            print("Getting recommendations...")
            recommendations = recommend_stocks(tickers)  # Remove model parameter
            if recommendations:
                recommendations_text = ', '.join(recommendations)
                prompt = f"Based on my analysis, I recommend considering {recommendations_text}. Here's why: "
                return generate_text(prompt)
            else:
                return f"After analyzing {', '.join(tickers)}, my model suggests holding off on investment at this time."
        except Exception as e:
            print(f"Error in recommendations: {str(e)}")
            return "Sorry, the recommendation model is not available at this time."
    elif "help" in question.lower():
        return "I can help you with stock prices, analysis, and recommendations. Please specify what you'd like to know."
    else:
        return generate_text(question)