def parse_review_inference(inference):
  data = {}

  data['toxicity'] = float(inference['toxicity'])
  data['severe_toxicity'] = float(inference['severe_toxicity'])
  data['obscene'] = float(inference['obscene'])
  data['threat'] = float(inference['threat'])
  data['insult'] = float(inference['insult'])
  data['identity_attack'] = float(inference['identity_attack'])

  return data
