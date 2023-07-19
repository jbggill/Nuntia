import requests
from bs4 import BeautifulSoup
import torch
from transformers import BertModel, BertTokenizer

def get_article_text(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  article_text = soup.find("div", class_="article-body")
  if article_text is None:
    print("The article text could not be found.")
    return None
  else:
    return article_text.text

def get_subjectivity(article_text):
  tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
  model = BertModel.from_pretrained("bert-base-uncased")

  inputs = tokenizer(article_text, return_tensors="pt")
  outputs = model(**inputs)
  
  # The subjectivity score is the output of the second last layer of the model.
  subjectivity = outputs[0][0][0]
  return subjectivity

def main():
  url = "https://www.bbc.com/news/world-us-canada-62190649"
  article_text = get_article_text(url)
  subjectivity = get_subjectivity(article_text)
  print(subjectivity)

if __name__ == "__main__":
  main()
