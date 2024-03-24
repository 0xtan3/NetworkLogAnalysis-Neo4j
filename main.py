import os
import pandas as pd
from dotenv import load_dotenv
from neomodel import StringProperty,StructuredNode,RelationshipTo,UniqueIdProperty,config

load_dotenv()

dataset_dir = './data'

config.DATABASE_URL=os.getenv("NEO4J_BOLT_URL")
data = pd.read_csv(os.path.join(dataset_dir,'Trojan_Detection.csv'))

