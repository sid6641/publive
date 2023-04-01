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
 
 Summary: 
* According to Warren Buffett, stock market efficiency is a myth and stocks often trade at unreasonable prices. 
* He encourages investors to focus on businesses rather than stocks and cautions that it is not easy to find good businesses. 
* Berkshire Hathaway has earned massive dividends from two companies with total investments equalling $47 billion or 10 per cent of its net worth.  
* Buffett advises investors to ignore operating earnings which can be manipulated easily by managers and emphasises the power of compounding for success in investing. 
* He also stresses that there is no guarantee of anything, so even high returns may be wiped out by declines in investment due to leverage risks



 Article: https://30stades.com/art-culture/how-pritikana-goswami-revived-bengal-nakshi-kantha-embroidery-poverty-to-empowerment
 
 Summary: 
* Pritikana Goswami received the Padma Shri award in 2023 for reviving Bengal's long-lost Nakshi Kantha craft through her artworks. 
* The Sanskrit word Kontha, which implies scraps or rags, is whence the word "Kantha" originates and was referenced as warm clothing in Panini's book "Ashtadhyayi". 
* In 1989, Pritikana was asked to create a group of women to work at a new Kantha stitching centre and replicate an intricate type of embroidery mostly done in Bangladesh called Nakshi Kantha - which she did successfully over three months.  
* Types of stitches used include Cross-stitch, backstitch, Kane stitch, Herringbone stitch, Satin stitch and running stitch among others; with various border types including Beki par (wavy or bent border), Biche par (scorpion border), Barfi par (diamond border) etc. 
* Mahua Lahiri has taken forward her mother’s legacy by participating as a speaker in seminars and using social media sites like Facebook and Instagram as marketing tools; while also sourcing Kantha from women trained by her mother for buyers abroad
