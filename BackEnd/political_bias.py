from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def BERT(text):

    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

    model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

    labels = torch.tensor([0])
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs, labels=labels)
    loss, logits = outputs[:2]
    print(logits.tolist())
    return percentages(logits.tolist()[0])


def percentages(lst):
    print(lst)
    lst = [val + 5 for val in lst]
    total = sum(lst)
    normalized = [val / total for val in lst]

    # Convert to percentages
    percentages = [val * 100 for val in normalized]
    labels = ['left','center','right']
    output = ""
    for label, percentage in zip(labels, percentages):
        output += f"{label}\n{percentage:.2f}%\n"
    output = {
        'left':percentages[0],
        'center':percentages[1],
        'right':percentages[2]
    } 
    return output
