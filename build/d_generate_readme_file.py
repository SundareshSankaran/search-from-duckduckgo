import os
import json
from py_sas_studio_custom_steps import CustomStep

cs=CustomStep(type="code", displayName="Search from DuckDuckGo")

trigger_name="ddgs"

description="This custom step searches the internet using the DuckDuckGo search engine for websites or news related to a search term provided by the user, and outputs results to a SAS dataset."

cs.generate_readme(readme_file=os.path.join(os.getcwd(),"..","README.md"), description=description, trigger_name=trigger_name)

