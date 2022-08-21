<!--


<template>
    <div class="moduleForm">
    <form @submit.prevent="handleSubmit()">
            <CostumInput 
            v-for="(input,i) in inputs"
            :key="i"
            v-model="input.value" 
            :label="input.label"
            :type="input.type"
            />
            <button>Modul hinzufügen bzw ändern</button>
    </form> 
    </div> 
</template>  

<script>

import CostumInput from './CustomInput.vue'
import moduleInputs from '../variables'

export default {
  watch: {
  },
  name: 'HelloWorld',
  props: {
  },
  components:{
      CostumInput
  },
  data(){
      return {
            inputs: [
                {
                    label: 'module_code',
                    value: '',
                    type: 'module_code'
                },
                {
                    label: 'module_title',
                    value: '',
                    type: 'module_title'
                },
                {
                    label: 'module_abbrev',
                    value: '',
                    type: 'module_abbrev'
                },
                {
                    label: 'module_type',
                    value: '',
                    type: 'module_type'
                },
                {
                    label: 'credit_points',
                    value: '',
                    type: 'credit_points'
                },
                {
                    label: 'language',
                    value: '',
                    type: 'language'
                },
                {
                    label: 'duration_of_module',
                    value: '',
                    type: 'duration_of_module'
                },
                {
                    label: 'recommended_semester',
                    value: '',
                    type: 'recommended_semester'
                },
                {
                    label: 'coordinator',
                    value: '',
                    type: 'coordinator'
                },
                {
                    label: 'lecturers',
                    value: '',
                    type: 'lecturers'
                },
                {
                    label: 'assessment-methods',
                    value: '',
                    type: 'assessment-methods'
                },
                {
                    label: 'workload',
                    value: '',
                    type: 'workload'
                },
                {
                    label: 'lecture',
                    value: '',
                    type: 'lecture'
                },
                {
                    label: 'seminar',
                    value: '',
                    type: 'seminar'
                },
                {
                    label: 'practical',
                    value: '',
                    type: 'practical'
                },
                {
                    label: 'exercise',
                    value: '',
                    type: 'exercise'
                },
                {
                    label: 'self_study',
                    value: '',
                    type: 'self_study'
                },
                {
                    label: 'recommended-prerequisites',
                    value: '',
                    type: 'recommended-prerequisites'
                },
                {
                    label: 'status',
                    value: '',
                    type: 'status'
                },
                {
                    label: 'location',
                    value:'',
                    type:'location'
                },
                {
                    label: 'po',
                    value: '',
                    type: 'po'
                },
                {
                    label: 'furtherInformation',
                    value:'',
                    type:'furtherInformation'
                }

            ]
      }
  },
  methods:{
      handleSubmit(){

            for(let i=0;i<this.inputs.length;i++)
            {
                console.log(this.inputs[i].value)
                moduleInputs.push(this.inputs[i].label,this.inputs[i].value)

            }
            console.log(moduleInputs)
            this.moduleToString()


               alert("Modul hinzufügt bzw geändert")

        },
        moduleToString(){
           const jsonString = JSON.stringify(moduleInputs)

            console.log("Json:")
            console.log(jsonString)
            return jsonString
        }
  }
}
</script>
-->

<template>
    <form>
        <label>module_code</label>
        <input type="module_code" v-model="module_code">

        <label>module_title</label>
        <input type="module_title" v-model="module_title">

        <label>module_abbrev</label>
        <input type="module_abbrev" v-model="module_abbrev">

        <label>module_type</label>
        <select v-model="module_type">
            <option :value="type.type" v-for="(type) in module_types_list" :key="type.type">{{type.type}}</option>
        </select>

        <label>credit_points</label>
        <input type="credit_points" v-model="credit_points">

        <label>language</label>
        <select v-model="language">
            <option :value="lang.lang" v-for="(lang) in lang_list" :key="lang.lang">{{lang.lang}}</option>
        </select>
        

        <label>duration_of_module</label>
        <input type="duration_of_module" v-model="duration_of_module">

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
        <label>coordinator</label>
        <select v-model="coordinator">
            <option :value="person.person" v-for="(person) in person_list" :key="person.person">{{person.person}}</option>
        </select>

        <label>lecturers</label>
        <select v-model="lecturers">
            <option :value="person.person" v-for="(person) in person_list" :key="person.person">{{person.person}}</option>
        </select>

        
        <label>assessment_method</label>
        <select v-model="assessment_method">
            <option :value="assessment.assessment" v-for="(assessment) in assessment_method_list" :key="assessment.assessment">{{assessment.assessment}}</option>
        </select>
       

        <label>workload</label>
        <input type="workload" v-model="workload">

        <label>lecture</label>
        <input type="lecture" v-model="lecture">

        <label>seminar</label>
        <input type="seminar" v-model="seminar">

        <label>practical</label>
        <input type="practical" v-model="practical">

        <label>self_study</label>
        <input type="self_study" v-model="self_study">

        <label>recommended_prerequisites</label>
        <input type="recommended_prerequisites" v-model="recommended_prerequisites">

        <label>required_prerequisites</label>
        <input type="required_prerequisites" v-model="required_prerequisites">

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
        <input type="further_information" v-model="further_information" id="furtherInformation">


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
            coordinator: '',
            person_list: persons,
            lecturers:'',
            workload:'',
            lecture:'',
            seminar:'',
            practical:'',
            self_study:'',
            recommended_prerequisites:'',
            required_prerequisites:'',
            po:'',
            further_information:''
        }

    },
    methods:{
        handleSubmit(){
            alert("Modul hinzufügt bzw geändert")
            //const fs = require('fs')

            //const lang = fs.readFileSync('./data/lang.yaml', {encoding: 'utf-8'});
            //console.log(lang);
            

            
        },
        assignValues(){
            
        },
        fillModuleArray(){
            
        }
    },

      beforeCreate(){
            /*const lang = this.loadLang()
            for(let i = 0; i<lang.length;i++){
                this.lang_list.push(e)
            }*/
        },
        mounted(){},
        updated(){
            //todo
            //parse yaml and fill array
            //this.loadLang()
        }

    
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

input {
    margin: 10px;
    display: block;
    border-radius: 7px;
    width: 100%;
}

select{
     margin: 10px;
    display: block;
    border-radius: 7px;
    width: 100%;
}

#furtherInformation{
        height: 50px;
}


</style>
