
import requests

ulr = "http://localhost:8000/api/courses/"
response = requests.get(ulr)

def main():
  
    from mdutils.mdutils import MdUtils
    
    print("Daten von API")
    module_string = response.text
    module_string = module_string.replace('[','').replace(']','').replace('{','').replace('}','').replace('"','').replace('\\','').replace(',','\n').replace('po:','## po:').replace('further_information:','')
    print(module_string)
    choice = input("Sollen die Kurse hinzugefügt werden? J/N")
    if choice == 'J':
        mdFile = MdUtils(file_name='Modulhandbuch', title='Modulhandbuch')
        mdFile.new_paragraph("---")
        mdFile.new_paragraph(module_string)
        mdFile.create_md_file()
        print("Eingaben wurden verwendet") 
    elif choice == 'N':
        print("Eingaben wurden nicht verwendet. Falls ein Kurs gelöscht werden soll, benutzen Sie bitte das API-Admin Interface und führen Sie den Code erneut aus")



if __name__ == "__main__":
    main()