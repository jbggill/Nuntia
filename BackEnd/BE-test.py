import political_bias
import article_processor
contents = article_processor.getContents('https://www.foxnews.com/media/democratic-strategist-scolds-biden-not-recognizing-seventh-grandchild-humanity')
bias = political_bias.BERT(contents[:len(contents)//2])
print(bias)