import json

job_list=[]
def modify_jsonl(data):
  modified_data = []
  for item in data:
    item["flag"] = False
    item["status"] = "Not Applied"
    item["resume"] = "NULL"
    item["summary"] = "NULL"
    modified_data.append(item)
  return modified_data

def read_jsonl_and_modify(filename):
  data = []
  with open(filename, 'r') as f:
    for line in f:
      try:
        data.append(json.loads(line))
      except json.JSONDecodeError:
        print(f"Error: Could not parse line: {line}")

  return modify_jsonl(data)

data = read_jsonl_and_modify("job-description.jsonl")  