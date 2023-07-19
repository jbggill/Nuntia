from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class BiasAnalyzer:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        self.labels = torch.tensor([0])

    def analyze(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs, labels=self.labels)
        loss, logits = outputs[:2]
        print(outputs)
        output = logits.softmax(dim=-1)[0].tolist()
        print(output)
        return self.labelOutput(output)

    @staticmethod
    def labelOutput(lst):
        lst = [round((l * 100),2) for l in lst]
        output = {
            'left': lst[0],
            'center': lst[1],
            'right': lst[2]
        }
        return output
