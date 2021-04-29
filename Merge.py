pwd

%cd '/content/sample_data'

f1data = f2data = "" 
 
with open('BioASQform_BioASQ-answer_factoid_testset4.json') as f1: 
  f1data = f1.read() 
with open('BioASQform_BioASQ-answer_yesno_testset4.json') as f2: 
  f2data = f2.read() 
  
  f1data += "\n"
f1data += f2data
with open ('Merge.json', 'a') as f3: 
  f3.write(f1data)

  
  def prep_list(data: dict, test_file: bool = False) -> dict:
   paragraphs = []
   for j, question in enumerate(data['questions']):

       if question['type'] == 'list':
           q_text = question['body'].replace(r'\u', '')
           id_base = question['id']
           #id = question['id']
           ideal = question['ideal_answer']
           exact = question['exact_answer']
           if test_file:
               exact = exact[0]
           for i, snippet in enumerate(question['snippets']):
               id = id_base + f'_{i+1:03}'
               context = snippet['text'].replace(r'\u', '')
               answer_start = -1
               is_impossible = False
               if not test_file:
                   for ans in set(ideal+exact):
                       ans = ans.replace(r'\u', '')
                       idx_found = context.lower().find(ans.lower())
                       if idx_found >= 0:
                           answer_start = idx_found
                           exact_answer = ans
                   if answer_start == -1:
                       is_impossible = True
                       continue
                   answers = [{
                       'text': exact_answer,
                       'answer_start': answer_start
                   }]
               else:
                   if len(id) != 28:
                       id = id + f'_{i+1:03}'
                   answers = []
               sample = {
                   'qas': [{
                       'id': id,
                       'question': q_text,
                       'answers': answers
                   }],
                   'context': context
               }
               paragraphs.append(sample)
   prepped_dict = {
       'data': [{
           'paragraphs': paragraphs
       }]
   }
   return prepped_dict
  
  def prep_list_test(data: dict, test_file: bool = False) -> dict:
   paragraphs = []
   for j, question in enumerate(data['questions']):
       if question['type'] == 'factoid':
           q_text = question['body'].replace(r'\u', '')
           id_base = question['id']
           #id = question['id']
           #ideal = question['ideal_answer']
          # exact = question['exact_answer']
           if test_file:
               exact = exact[0]
           for i, snippet in enumerate(question['snippets']):
               id = id_base + f'_{i+1:03}'
               context = snippet['text'].replace(r'\u', '')
              # answer_start = -1
               #is_impossible = False
               # if not test_file:
               #     for ans in set(ideal+exact):
               #         ans = ans.replace(r'\u', '')
               #         idx_found = context.lower().find(ans.lower())
               #         if idx_found >= 0:
               #             answer_start = idx_found
               #             exact_answer = ans
               #     if answer_start == -1:
               #         is_impossible = True
               #         continue
               #     answers = [{
               #         'text': exact_answer,
               #         'answer_start': answer_start
               #     }]
               # else:
               #     if len(id) != 28:
               #         id = id + f'_{i+1:03}'
               #     answers = []
               sample = {
                   'qas': [{
                       'id': id,
                       'question': q_text,
                       #'answers': answers
                   }],
                   'context': context
               }
               paragraphs.append(sample)
   prepped_dict = {
       'data': [{
           'paragraphs': paragraphs
       }]
   }
   return prepped_dict
  
  import json

with open('BioASQ-task9bPhaseB-testset4') as f:
    data = json.load(f)

prepped_data = prep_list_test(data)
#prepped_data_yesno = prep_yesno(data)
#print(prepped_data)

with open('list.json', 'w') as fn:
    # indent for formatting
    # ensure_ascii to exclude \u char from being written
    json.dump(prepped_data, fn)#, indent=2)#, ensure_ascii=False)
