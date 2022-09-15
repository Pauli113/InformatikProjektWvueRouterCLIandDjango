
import requests
import json

ulr = "http://localhost:8000/api/courses/"
p = {'fields': "module_code,module_title,module_abbrev,module_type,credit_points,language,duration_of_module,recommended_semester,frequency,lecturers_list,coordinators_list,assessment_method,workload,seminar,practical,excercise,self_study,required_prerequisites_list,recommended_prerequisites_list,status,location,po,further_information"}
response = requests.get(ulr,params=p)



def main():
  
    from mdutils.mdutils import MdUtils
    from mdutils import Html
    
    print("Daten von API")
    mdFile = MdUtils(file_name='Modulhandbuch', title='Modulhandbuch')
    mdFile.new_paragraph("---")
    module_string = response.text
    module_string = module_string.replace('[','').replace(']','').replace('{','').replace('}','').replace('"','').replace('\\','').replace(',','\n')
    print(module_string)
    mdFile.new_paragraph(module_string)

    
    mdFile.create_md_file()
    print("Eingaben wurden verwendet")
  


if __name__ == "__main__":
    main()