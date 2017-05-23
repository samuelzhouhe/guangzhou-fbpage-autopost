#Inspired by the tutorial here: http://nodotcom.org/python-facebook-tutorial.html
import facebook
import config
import datetime


def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "539503376218930",  # Der Guangzhouer
    "access_token" :   config.ACCESS_TOKEN() # Step 3
    }

  api = get_api(cfg)
  timeStamp = str(datetime.datetime.now())[0:19]
  msg = "Good evening, Cantonese people!" + timeStamp
  print(msg)
  status = api.put_wall_post(msg)
  print(status)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

if __name__ == "__main__":
  main()