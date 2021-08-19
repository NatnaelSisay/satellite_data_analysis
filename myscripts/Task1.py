import json, ast
from os import stat
import pdal

def read_json(file_name):
  '''
  Read json file and return the string format
  '''

  try:
    file_path = '../pipeline.json'
    print("File Path : ", file_path)
    with open(file_path, 'r') as json_file:
      data = json.loads(json_file.read())
    return data

  except:
    print('File Not found')
    return None

def prepare_pipe(bound, us_state='IA_FullState'):
  data = read_json('pipeline.json')
  data['pipeline'][0]['bounds'] = bound
  data['pipeline'][0]['filename'] = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"+us_state+"/ept.json"
  data['pipeline'][6]['filename'] = 'iowa.laz'
  data['pipeline'][7]['filename'] = 'iowa.tiff'

  print("data LInk : " , data['pipeline'][0]['filename'])
  return data

def run_pipe(bound, us_state):
  print("Run pipe")
  result = prepare_pipe(bound, us_state)
  pipeline = pdal.Pipeline(json.dumps(result))
  pipe_result  = pipeline.execute()
  print(pipe_result)

bound = str(([-10425171.940, -10423171.940], [5164494.710, 5166494.710]))
state = 'IA_FullState'

# data = read_json('pipeline.json')
# print(data)
# result = prepare_pipe(bound)
# print(result)

run_pipe(bound, state)


# open_file = open('../pipeline.json', 'r')
# print(open_file.read())

