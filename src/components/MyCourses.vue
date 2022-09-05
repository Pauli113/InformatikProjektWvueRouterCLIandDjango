<template>
  <h1>Meine Kurse</h1>
  <button v-on:click="getCourses">Meine Kurse sehen</button>
  <div v-for="course in courses" :key="course">
    <p>{{course}}</p>
  </div>
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
        .then(res => (this.courses.push(res.data)))
        .catch(err => console.log(err))
        console.log(this.courses)
      }
    }
  }
</script>