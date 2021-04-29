pwd

%cd '/content/sample_data'

f1data = f2data = "" 
 
with open('BioASQform_BioASQ-answer_factoid_testset4.json') as f1: 
  f1data = f1.read() 
with open('BioASQform_BioASQ-answer_yesno_testset4.json') as f2: 
  f2data = f2.read() 
with open('BioASQform_BioASQ-answer_list_testset4.json') as f2: 
  f2data = f2.read() 
  
  f1data += "\n"
f1data += f2data
with open ('Merge.json', 'a') as f3: 
  f3.write(f1data)

  
 
