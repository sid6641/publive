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


 ### Sample outputs for the news articles:
 Article: https://www.newsdrum.in/personal-finance/warren-buffetts-letter-to-shareholders-key-takeaways-for-investors
 Output:
 Summary: 
* According to Warren Buffett, stock market efficiency is a myth and stocks often trade at unreasonable prices. 
* He encourages investors to focus on businesses rather than stocks and cautions that it is not easy to find good businesses. 
* Berkshire Hathaway has earned massive dividends from two companies with total investments equalling $47 billion or 10 per cent of its net worth.  
* Buffett advises investors to ignore operating earnings which can be manipulated easily by managers and emphasises the power of compounding for success in investing. 
* He also stresses that there is no guarantee of anything, so even high returns may be wiped out by declines in investment due to leverage risks



 Article: https://30stades.com/art-culture/how-pritikana-goswami-revived-bengal-nakshi-kantha-embroidery-poverty-to-empowerment
 Summary: 
* The article focuses on the current state of US-China trade relations and the potential consequences of President Trump's recent tariffs. 
* It highlights some of the key issues at stake, including rising tensions between the two countries over intellectual property theft, currency manipulation and market access. 
* It argues that while tariffs may be a short-term solution to protect American jobs, they could have long term negative effects on both economies if not handled properly by both sides. 
* The article also looks at how China is responding to these new tariffs with retaliatory measures such as increasing taxes on certain goods imported from the US and potentially restricting access to its markets for certain companies or products in retaliation against US actions.  
* In addition, it discusses how other countries are being impacted by this situation due to their economic ties with either country, with many economists predicting a global economic slowdown as a result of this ongoing trade war between two major world powers . 
* Finally, it outlines how businesses can prepare themselves for potential changes in international trade resulting from this dispute through diversifying their supply chains and exploring alternative sources of production outside China or the US depending on what best suits their needs in light of changing circumstances..
