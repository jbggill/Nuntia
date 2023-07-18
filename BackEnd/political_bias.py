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
        print(logits.tolist()[0])
        return self.percentages(logits.tolist()[0])

    @staticmethod
    def percentages(lst):
        lst = [val + 5 for val in lst]
        total = sum(lst)
        normalized = [val / total for val in lst]

        # Convert to percentages
        percentages = [val * 100 for val in normalized]
        labels = ['left', 'center', 'right']
        output = {
            'left': percentages[0],
            'center': percentages[1],
            'right': percentages[2]
        }
        return output
