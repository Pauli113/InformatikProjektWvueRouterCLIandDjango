import re
import requests
import json

ulr = "http://localhost:8000/api/courses/"

response = requests.get(ulr)



def main():
    #import markdown
    #output = markdown.markdown(module_string)
    from mdutils.mdutils import MdUtils
    from mdutils import Html
    
    print("Daten von API")
    mdFile = MdUtils(file_name='Modulhandbuch', title='Modulhandbuch')
    mdFile.new_paragraph("---")
    module_string = response.text
    module_string = module_string.replace('[','').replace(']','').replace('{','').replace('}','').replace('"','')
    print(module_string)
    mdFile.new_paragraph(module_string)

    
    mdFile.create_md_file()
    print("Eingaben wurden verwendet")
  


if __name__ == "__main__":
    main()