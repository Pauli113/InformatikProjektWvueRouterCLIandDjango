
<template>
    <form @submit.prevent="handleSubmit">
        <label>module_code</label>
        <input type="module_code" v-model="course.module_code" placeholder="UUID">

        <label>module_title</label>
        <input type="module_title" v-model="course.module_title" placeholder="Algorithmik">

        <label>module_abbrev</label>
        <input type="module_abbrev" v-model="course.module_abbrev" placeholder="ALG">

        <label>module_type</label>
        <select v-model="course.module_type">
            <option :value="type.type" v-for="(type) in module_types_list" :key="type.type">{{type.type}}</option>
        </select>

        <label>credit_points</label>
        <input type="credit_points" v-model="course.credit_points" placeholder="5">

        <label>language</label>
        <select v-model="course.language">
            <option :value="lang.lang" v-for="(lang) in lang_list" :key="lang.lang">{{lang.lang}}</option>
        </select>
        

        <label>duration_of_module</label>
        <input type="duration_of_module" v-model="course.duration_of_module" placeholder="1">

        <label>recommended_semester</label>
        <select v-model="course.recommended_semester">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
        </select>
        
        <label>frequency</label>
        <select v-model="course.frequency">
            <option :value="season.season" v-for="(season) in seasons_list" :key="season.season">{{season.season}}</option>
        </select>

        
   

             <p>responsibilities</p>
        <table class="table">
            <thead>
                <tr>
                    <th>coordinators</th>
                    <th>lecturers</th>
                </tr>
            </thead>
            <tbody>
                  <tr v-for="(person) in person_list" :key="person.person">
                    <td><input type="checkbox" v-model="course.coordinators_list" :value="person.person"/>{{person.person}}</td>
                    <td><input type="checkbox" v-model="course.lecturers_list" :value="person.person"/>{{person.person}}</td>
                    
                </tr>
            </tbody>
              
        </table>
      

        <label>assessment_method</label>
        <select v-model="course.assessment_method">
            <option :value="assessment.assessment" v-for="(assessment) in assessment_method_list" :key="assessment.assessment">{{assessment.assessment}}</option>
        </select>
       

        <label>workload</label>
        <input type="workload" v-model="course.workload" placeholder="150">

        <label>lecture</label>
        <input type="lecture" v-model="course.lecture" placeholder="36">

        <label>seminar</label>
        <input type="seminar" v-model="course.seminar" placeholder="0">

        <label>practical</label>
        <input type="practical" v-model="course.practical" placeholder="18">

        <label>excersice</label>
        <input type="excersice" v-model="course.excersice" placeholder="18">

        <label>self_study</label>
        <input type="self_study" v-model="course.self_study" placeholder="78">

     
       
        <p>prerequisites (zur Mehrfachauswahl "command" oder "strg" Taste halten)</p>
        <p>required </p>
        <select name="courses" id="required_prerequisites" v-model="course.required_prerequisites_list" multiple class="multi">
            <option v-for="(course) in course_list" :key="course.course">{{course.course}}</option>
        </select>

        <p>recommended</p>
        <select name="courses" id="required_prerequisites" v-model="course.recommended_prerequisites_list" multiple class="multi">
            <option v-for="(course) in course_list" :key="course.course">{{course.course}}</option>
        </select>

        <label>status</label>
        <select v-model="course.status">
            <option :value="status.status" v-for="(status) in status_list" :key="status.status">{{status.status}}</option>
        </select>

        <label>location</label>
        <select v-model="course.location">
            <option :value="location.location" v-for="(location) in location_list" :key="location.location">{{location.location}}</option>
        </select>

        <label>po</label>
        <select v-model="course.po" multiple>
            <option :value="po.po" v-for="(po) in po_list" :key="po.po">{{po.po}}</option>
        </select>
        <!--nedd to add submit prevent when enter is pressed-->
        <label>furtherInformation (Shift enter für Zeilen umbrüche)</label>
        <br/>
        <textarea v-model="course.further_information" id="furtherInformation" placeholder="Für Überschriften ein ## und ein Leerzeichen vor den Text hängen, bei Aufzählungen ein * und ein Leerzeichen" @keydown="inputHandler"></textarea>
        <br>
        <button >Modul hinzufügen bzw ändern</button>
    </form>
    
    
</template>

<script>
import axios from 'axios';


let langs = require('../data/lang.js')
let assessmentMethods = require('../data/assessment.js')
let moduleTypes = require('../data/type.js')
let locations = require('../data/location.js')
let seasons = require('../data/season.js')
let status_file = require('../data/status.js')
let persons = require('../data/person.js')
let courses = require('../data/courses.js')
let pos = require('../data/po.js')
export default {
    
    data(){
        return{

            assessment_method_list: assessmentMethods,
            lang_list: langs,
            module_types_list: moduleTypes,
            location_list: locations,
            status_list: status_file,
            person_list: persons,
            course_list: courses,
            seasons_list: seasons,
            po_list: pos,
            course:{
            module_code:'',
            module_title:'',
            module_abbrev:'',
            credit_points:'',
            language:'',
            assessment_method:'',
            module_type:'',
            location:'',
            season:'',
            //status
            status:'',
            duration_of_module:'',
            recommended_semester:'',
            //person
            coordinators_list: [],
            lecturers_list:[],
            //courses
            required_prerequisites_list:[],
            recommended_prerequisites_list:[],
            //pos
            po:[],
            //integers
            workload:'',
            lecture:'',
            seminar:'',
            practical:'',
            self_study:'',
            excersice:'',
            further_information:'',
            frequency:'',
            linebreak:''
        }
    }

    },

    
    methods:{
        inputHandler(e) {
      if (e.keyCode === 13 && !e.shiftKey) {
        e.preventDefault();
        this.handleSubmit();
      }
    },
       handleSubmit(){
        //todo submit only fires when button is clicked
        console.log(this.course)
        this.createCourse()
       },
       async createCourse(){
        this.course.recommended_prerequisites_list.forEach((item,i,self) => self[i] = ' module.'+item)
        this.course.recommended_prerequisites = JSON.stringify(this.course.recommended_prerequisites_list)
        this.course.required_prerequisites_list.forEach((item,i,self) => self[i] = '- module.'+item)
        this.course.required_prerequisites = JSON.stringify(this.course.required_prerequisites_list)
        this.course.lecturers_list.forEach((item,i,self) => self[i] = 'person.'+item)
        this.course.lecturers = JSON.stringify(this.course.lecturers_list)
        this.course.coordinators_list.forEach((item,i,self) => self[i] = 'person.'+item)
        this.course.coordinators = JSON.stringify(this.course.coordinators_list)
        this.further_information = this.further_information + '---'
        this.course.status = 'status.' + this.course.status
        this.course.location = 'location.' + this.course.location
        this.course.module_abbrev = this.course.module_abbrev.toUpperCase()
        this.course.module_type = 'module_type.' + this.course.module_type
        this.course.language = 'lang.' + this.course.language
        this.course.frequency = 'season.' + this.course.frequency
        this.course.assessment_method + 'assessment-methods.' + this.course.assessment_method
        this.course.linebreak = '---'
        for (let i = 0; i < this.course.po.length;i++){
            if((i+1) == (this.course.po.length)){
                this.course.po[i] = this.course.po[i].replace(',','')
            }
        }
        this.course.po_list = JSON.stringify(this.course.po)
        axios.post("http://127.0.0.1:8000/api/courses/",this.course)
        .then(res => (this.courses.push(res.data)))
        .catch(err => console.log(err))
        console.log(this.courses)
        alert("Kurs wurde erstellt " + this.course.module_code)
       }
    }
}
</script>

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

.multi{
    height:900px;
}

#furtherInformation{
        height: 200px;
        width: 81%;
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
