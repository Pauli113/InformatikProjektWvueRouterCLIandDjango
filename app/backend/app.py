import requests
import json

ulr = "http://localhost:8000/api/courses/"

response = requests.get(ulr)
#print(response.text)
module_string = response.text
#print(module_string)
#list_string = response.text.split(",")
#module_list = module_string.split("}")
#list_string = str(module_list)

def main():
    #import markdown
    #output = markdown.markdown(module_string)
    from mdutils.mdutils import MdUtils
    from mdutils import Html

    
    #f = open('module_book.md','w')
    #f.write(output)
    #f.close()
    print("Daten von API")
    splitted_string = module_string.split(',')
   #print("splitted string")
    #print(splitted_string)
    for item in splitted_string:
        res_string = item.replace('[','')

    
        print(res_string)
  

    mdFile = MdUtils(file_name='Modulhandbuch', title='Modulhandbuch')
    mdFile.new_paragraph(module_string)
    mdFile.create_md_file()
    print("Eingaben wurden verwendet")
  


if __name__ == "__main__":
    main()