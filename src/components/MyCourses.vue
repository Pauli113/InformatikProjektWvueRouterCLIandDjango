<template>
  <h1>Meine Kurse</h1>
  <button v-on:click="getCourses">Meine Kurse sehen</button>
</template>

<script>
import axios from 'axios';

  export default{
  
    data(){
      return {
        courses:[]
      }
    },

    methods:{
      getCourses(){
        axios.get("http://localhost:8000/api/courses/")
        .then(res => (console.log(res.data)))
        .catch(err => console.log(err))
        console.log(this.courses)
      }
    }
  }
</script>