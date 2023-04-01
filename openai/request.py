# things that can be expreimented upon:
# 1. prompt design: can we make the promt so there are better summaries
# 2. number of responses. Right now, I'm just taking the best repsonse from chatGPT, but there are other options for the same article as well.

import os
import argparse
import openai
from pathlib import Path

openai.api_key = "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"

parser = argparse.ArgumentParser(description = 'input news article to summarise')
parser.add_argument('-a','--article_file', type = str, help='inputs news article to summarise')



def main():
  args = parser.parse_args()
  article_str = Path(args.article_file).read_text()
  prompt_str = 'Act like you\'re an expert journalist.\nyour task is to summarize news articles in the following format:\n    The input will contain three sections: "Title", "Description", and "Body".\n    The "Title" section will contain the title of the news article.\n    The "Description" section will contain a short description of the article.\n    The "Body" section will contain multiple sections, each with its own "Section heading" and "Section body"\n    "Section body" will contain a few paragraphs of text related to the "Section heading.\n\nRead this input format and summarize the news article into 5 to 10 easily understandable points. The summary should be in simple language, avoiding technical jargon. The prompt should be able to handle articles from a variety of sources, including newspapers, online news websites, and blogs.\n\n\nARTICLE STARTS\n\n{article_str}\n\nARTICLE ENDS\n\n\nInstructions:\nSummarize this article in 5 to 10 easily digestable and attention grabbing points. \nDo not skip any section completely. \nMake the output in points.\n'
  
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_str,
    temperature=0.6,
    max_tokens=500,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
  )

  article_summary = response.choices[0].text

  print(article_summary)
  print(response.choices[0].finish_reason)


main()