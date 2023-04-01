# publive
 Projects for publive. https://thepublive.com/
 
 This is a news article summarizer tool. 
 Examples of goog articles are present in **input/** directory. 
 
 A good news article would contain certain keywords in it (to help the summarizer):
 **Title, Description, followed by sections**. 
 Each section has a **section heading**, and a **section body**.
 
 
 To get the summary of the article:
 python3 request.py -a=../input/sample_input_1


 ## Sidenote:
 ## Experiment with prompt design
 To experiment with the prompt design:
 * modify the prompt string in publive/openai/prompts.txt
 * python3 get_prompt_string.py -f=/Users/sidkumar/Desktop/publive/openai/promts.txt
 
 paste the output(generated) string in the openai/request.py, prompt_str variable.
 
 ### Note:
 make sure not to modify the {article_str} part of the prompt.
 Only modify the **header** section, or the **instructions** section of the prompt. 
