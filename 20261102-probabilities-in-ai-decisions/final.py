def diagnose(symptoms):
  if 'fever' in symptoms:
    return {'probability': 0.7, 'diagnosis': 'flu'}
  elif 'headache' in symptoms:
    return {'probability': 0.4, 'diagnosis': 'tension headache'}
  else:
    return {'probability': 0.3, 'diagnosis': 'unknown condition'}

symptoms = ['fever', 'headache']
result = diagnose(symptoms)
print(f'Probability of {result['diagnosis']}: {result['probability']}')
