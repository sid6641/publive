from pathlib import Path
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', type = str, help='input prompt for chatGPT summarizer')


def main():
  args = parser.parse_args()
  article_str = Path(args.file).read_text()
  print(repr(article_str))


main()