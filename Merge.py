pwd

%cd '/content/sample_data'

f1data = f2data = f3data = f4data = "" 
 
with open('BioASQform_BioASQ-answer_factoid.json') as f1: 
  f1data = f1.read() 
with open('BioASQform_BioASQ-answer_yesno.json') as f2: 
  f2data = f2.read() 
with open('BioASQform_BioASQ-answer_list.json') as f3: 
  f3data = f3.read() 
with open('BioASQform_BioASQ-answer_summary.json') as f4: 
  f4data = f4.read() 
  
f1data += "\n"
f1data += f2data
f1data += "\n"
f1data += f3data
f1data += "\n"
f1data += f4data
with open ('BioASQform_BioASQ-answer_all.json', 'a') as f5: 
  f5.write(f1data)

  
 
