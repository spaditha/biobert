
## ---- Data prep

def prep_factoid(data: dict, test_file: bool = False) -> dict:
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

## ---- Data prep

def prep_list_test(data: dict, test_file: bool = False) -> dict:
   paragraphs = []
   for j, question in enumerate(data['questions']):
       if question['type'] == 'list':
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

  ## -- Read test file
  
  import json

with open('BioASQ-task9bPhaseB-testset4.txt') as f:
    data = json.load(f)

prepped_data = prep_list_test(data)
#prepped_data_yesno = prep_yesno(data)
#print(prepped_data)

with open('list.json', 'w') as fn:
    # indent for formatting
    # ensure_ascii to exclude \u char from being written
    json.dump(prepped_data, fn)#, indent=2)#, ensure_ascii=False)
    
## -- BioASQ code    
    
!git clone https://github.com/dmis-lab/bioasq-biobert.git
  
!gdown --id 1AR6CLa17oMjdnYtV1xF3w9GygSrElmxK
!gdown --id 1rXFQRcV69QHAxghQ3NeAlhkg6ykpflVK
!gdown --id 17fX1-oChZ5rxu-e-JuaZl2I96q1dGJO4
!gdown --id 1GQUvBbXvlI_PeUPsZTqh7xQDZMOXh7ko

!tar -xzf BERT-pubmed-1000000-SQuAD2.tar.gz
!tar -xzf BERT-pubmed-1000000-SQuAD.tar.gz

!pip install tensorflow==1.15

!python bioasq-biobert/run_list.py --num_train_epochs=100.0 --do_predict=True --vocab_file=vocab.txt --bert_config_file=bert_config.json --init_checkpoint=model.ckpt-14470 --max_seq_length=384 --doc_stride=128 --do_lower_case=False --train_batch_size=10 --predict_batch_size=10 --train_file=prepped_list_training9b.json --predict_file=list.json --output_dir=t9btestlist

!python /content/bioasq-biobert/biocodes/transform_n2b_list.py --nbest_path=/content/t9btestlist/nbest_predictions.json --output_path=/content
