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
    <form @submit.prevent="handleSubmit()">
        <label>module_code</label>
        <input type="module_code" v-model="module_code">

        <label>module_title</label>
        <input type="module_title" v-model="module_title">

        <label>module_abbrev</label>
        <input type="module_abbrev" v-model="module_abbrev">

        <label>module_type</label>
        <select v-model="module_type">
            <option value="mandatory">mandatory</option>
             <option value="voluntary">voluntary</option>
        </select>

        <label>credit_points</label>
        <input type="credit_points" v-model="credit_points">

        <label>language</label>
        <select v-model="language">
            <option value="de">Deutsch</option>
            <option value="eng">Englisch</option>
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
            <option value="season.ws">season.ws</option>
            <option value="season.ss">season.ss</option>
        </select>

        <p>responsibilities</p>
        <label>coordinator</label>
        <select v-model="coordinator">
            <option v-for="(item,index) in person_list" :value="index" v-bind:key="index">
            {{item}}
            </option>
        </select>
        <label>lecturers</label>
        <select v-model="lectures">
            <option v-for="(item,index) in person_list" :value="index" v-bind:key="index">
            {{item}}
            </option>
        </select>

         

        <label>assessment_method</label>
        <input type="assessment_method" v-model="assessment_method">

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
            <option value="1">active</option>
            <option value="2">inactive</option>
        </select>

        <label>location</label>
        <select v-model="location">
            <option value="location.cgn_deutz">location.cgn_deutz</option>
            <option value="location.cgn_kalk">location.cgn_kalk</option>
            <option value="location.cgn_muelheim">location.cgn_muelheim</option>
            <option value="location.cgn_cgn_suedstadt">location.cgn_suedstadt</option>
            <option value="location.gm">location.gm</option>
            <option value="location.lvk">location.lvk</option>
        </select>

        <label>po</label>
        <select v-model="po">
            <option value="1">PO1</option>
            <option value="2">PO2</option>
        </select>

        <label>furtherInformation</label>
        <input type="further_information" v-model="further_information" id="furtherInformation">


        <button>Modul hinzufügen bzw ändern</button>
    </form>
    {{module_code}}
    {{}}
    
    
</template>

<script>
export default {
    components:{
                
    },
    data(){
        return{
            module_code:'',
            module_title:'',
            module_abbrev:'',
            module_type:'',
            credit_points:'',
            language:'',
            duration_of_module:'',
            recommended_semester:'',
            frequency:'',
            coordinator: '',
            person_list:{
                "all":"all",
                "nn":"nn",
                "tbb":"tbb",
                "sbe":"sbe",
                "bbe":"bbe",
                "mboe":"mboe",
                "hkl":"hkl",
                "sku":"sku"
            },
            lecturers:'',
            assessment_method:'',
            workload:'',
            lecture:'',
            seminar:'',
            practical:'',
            self_study:'',
            recommended_prerequisites:'',
            required_prerequisites:'',
            status:'',
            location:'',
            po:'',
            further_information:'',
            assessment:''
        }

    },
    methods:{
        handleSubmit(){
            alert("Modul hinzufügt bzw geändert")
        },
        assignValues(){
            
        },
        fillModuleArray(){
            
        }
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
