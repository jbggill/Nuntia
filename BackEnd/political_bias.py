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
    lst = [val + 5 for val in lst]
    total = sum(lst)
    normalized = [val / total for val in lst]

    # Convert to percentages
    percentages = [val * 100 for val in normalized]
    labels = ['left','center','right']
    output = ""
    for label, percentage in zip(labels, percentages):
        output += f"{label}\n{percentage:.2f}%\n"
    return output



text = "Actor Michael Imperioli thanked the Supreme Court on Saturday for \"allowing\" him to discriminate after they held that a graphic designer who creates wedding websites does not have to create them for same-sex marriages.&nbsp; He also decided to \"forbid bigots and homophobes\" from watching his work.&nbsp; \"I've decided to forbid bigots and homophobes from watching The Sopranos, The White Lotus, Goodfellas or any movie or tv show I’ve been in. Thank you Supreme Court for allowing me to discriminate and exclude those who I don’t agree with and am opposed to. USA ! USA!\" he wrote.&nbsp; \"Hate and ignorance is not a legitimate point of view,\" he wrote on Instagram. \"America is becoming dumber by the minute.\"  SUPREME COURT RULES AGAINST BIDEN STUDENT LOAN DEBT HANDOUT In a 6-3 decision issued Friday, the Supreme Court ruled in favor of artist Lorie Smith, who sued the state over its anti-discrimination law that prohibited businesses providing sales or other accommodations to the public from denying service based on a customer's sexual orientation. Justice Neil Gorsuch authored the majority opinion, which said that, \"In this case, Colorado seeks to force an individual to speak in ways that align with its views but defy her conscience about a matter of major significance."


print(percentages(BERT(text)))