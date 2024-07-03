from dotenv import load_dotenv
import os
load_dotenv()
secreat_key=os.getenv('keyval')
print(f"secreat key :{secreat_key}")