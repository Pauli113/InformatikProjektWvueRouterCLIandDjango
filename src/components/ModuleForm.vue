
<template>
    <form>
        <label>module_code</label>
        <input type="module_code" v-model="module_code" placeholder="UUID">

        <label>module_title</label>
        <input type="module_title" v-model="module_title" placeholder="Algorithmik">

        <label>module_abbrev</label>
        <input type="module_abbrev" v-model="module_abbrev" placeholder="ALG">

        <label>module_type</label>
        <select v-model="module_type">
            <option :value="type.type" v-for="(type) in module_types_list" :key="type.type">{{type.type}}</option>
        </select>

        <label>credit_points</label>
        <input type="credit_points" v-model="credit_points" placeholder="5">

        <label>language</label>
        <select v-model="language">
            <option :value="lang.lang" v-for="(lang) in lang_list" :key="lang.lang">{{lang.lang}}</option>
        </select>
        

        <label>duration_of_module</label>
        <input type="duration_of_module" v-model="duration_of_module" placeholder="1">

        <label>recommended_semester</label>
        <select v-model="recommended_semester">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
        </select>
        
        <label>frequency</label>
        <select v-model="frequency">
            <option :value="season.season" v-for="(season) in seasons_list" :key="season.season">{{season.season}}</option>
        </select>

        
   

             <p>responsibilities</p>
        <table class="table">
            <thead>
                <tr>
                    <th>coordinator</th>
                    <th>lecturers</th>
                </tr>
            </thead>
            <tbody>
                  <tr v-for="(person) in person_list" :key="person.person">
                    <td><input type="checkbox" v-model="coordinators" :value="person.person"/>{{person.person}}</td>
                    <td><input type="checkbox" v-model="lecturers" :value="person.person"/>{{person.person}}</td>
                </tr>
            </tbody>
              
        </table>
               
    
  

        <label>assessment_method</label>
        <select v-model="assessment_method">
            <option :value="assessment.assessment" v-for="(assessment) in assessment_method_list" :key="assessment.assessment">{{assessment.assessment}}</option>
        </select>
       

        <label>workload</label>
        <input type="workload" v-model="workload" placeholder="150">

        <label>lecture</label>
        <input type="lecture" v-model="lecture" placeholder="36">

        <label>seminar</label>
        <input type="seminar" v-model="seminar" placeholder="0">

        <label>practical</label>
        <input type="practical" v-model="practical" placeholder="18">

        <label>excersice</label>
        <input type="excersice" v-model="excersice" placeholder="18">

        <label>self_study</label>
        <input type="self_study" v-model="self_study" placeholder="78">

     
        
        <p>prerequisites</p>
        <table class="table">
            <thead>
                <tr>
                    <th>required</th>
                    <th>recommended</th>
                </tr>
            </thead>
            <tbody>
                  <tr v-for="(course) in course_list" :key="course.course">
                    <td><input type="checkbox" v-model="required_prerequisites" :value="course.course"/>{{course.course}}</td>
                    <td><input type="checkbox" v-model="recommended_prerequisites" :value="course.course"/>{{course.course}}</td>
                </tr>
            </tbody>
              
        </table>       

        

        <label>status</label>
        <select v-model="status">
            <option :value="status.status" v-for="(status) in status_list" :key="status.status">{{status.status}}</option>
        </select>

        <label>location</label>
        <select v-model="location">
            <option :value="location.location" v-for="(location) in location_list" :key="location.location">{{location.location}}</option>
        </select>

        <label>po</label>
        <select v-model="po">
            <option value="1">PO1</option>
            <option value="2">PO2</option>
        </select>

        <label>furtherInformation</label>
        <input type="further_information" v-model="further_information" id="furtherInformation" placeholder="## (de) Angestrebte Lernergebnisse:">


        <button @click.prevent="handleSubmit" >Modul hinzufügen bzw ändern</button>
    </form>
    
    
</template>

<script>
//json file imports
let langs = require('../data/lang.js')
let assessmentMethods = require('../data/assessment.js')
let moduleTypes = require('../data/type.js')
let locations = require('../data/location.js')
let seasons = require('../data/season.js')
let status_file = require('../data/status.js')
let persons = require('../data/person.js')
let courses = require('../data/courses.js')
export default {
    components:{
             
    },
    
    data(){
        return{
            module_code:'',
            module_title:'',
            module_abbrev:'',
            credit_points:'',
            //language list
            language:'',
            lang_list: langs,
            //assessment list
            assessment_method:'',
            assessment_method_list: assessmentMethods,
            //module type list
            module_type:'',
            module_types_list: moduleTypes,
            //location
            location:'',
            location_list: locations,
            //season
            season:'',
            seasons_list: seasons,
            //status
            status:'',
            status_list: status_file,
            duration_of_module:'',
            recommended_semester:'',
            //person
            coordinators: [],
            person_list: persons,
            lecturers:[],
            workload:'',
            lecture:'',
            seminar:'',
            practical:'',
            self_study:'',
            excersice:'',
            //courses
            recommended_prerequisites:[],
            required_prerequisites:[],
            course_list: courses,
            po:'',
            further_information:'',
            frequency:''
        }

    },

    
    methods:{
        handleSubmit(){
            alert("Modul hinzufügt bzw geändert")
            console.log(this.coordinators)
            
        },
        assignValues(){
            
        },
        fillModuleArray(){
            
        }
    }
    
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

input {
    margin: 10px;
    display: block;
    width: 80%;
}

select{
    margin: 10px;
    display: block;
    width: 80.5%;
}

#furtherInformation{
        height: 50px;
}

.table {
    width:81%
}

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}



</style>
