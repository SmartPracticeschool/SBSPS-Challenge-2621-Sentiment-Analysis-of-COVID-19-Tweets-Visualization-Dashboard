import preprocessor as p
import numpy as np 
import pandas as pd
import re as re
import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_59ce70433d0c4b4d95817a77b9042741 = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='OHfo7peHW5YcrP1k2sp-BWA8c5HUs53HUEiUS4sqYYmT',
    ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.eu-geo.objectstorage.service.networklayer.com')


body = client_59ce70433d0c4b4d95817a77b9042741.get_object(Bucket='megha1-donotdelete-pr-k9tzkndbrlckzs',Key='data_2020-03-01.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

def preprocess_tweet(row):
    text = row['Tweet Content']
    text = p.clean(text)
    return text
    
parse_dt = pd.read_csv(body)
parse_dt=parse_dt[1:]

p.set_options(p.OPT.URL, p.OPT.MENTION)
parse_dt['Tweet Content']=parse_dt.apply(preprocess_tweet, axis=1)
print(parse_dt)
ls=[]
for row in parse_dt['Tweet Content']:
    for ext in re.findall(r"#(\w+)", row):
        ls.append(ext)
