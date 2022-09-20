<template>
  <h1>Alle Kurse</h1>

  
  <pre>{{courses[0]}}</pre>
 
</template>

<script>
import axios from 'axios';

  export default{
  created () {
  },
  
    data(){
      return {
        courses:[]
      }
    },
    beforeCreate() {
        axios.get("http://localhost:8000/api/courses/")
        .then(res => (this.courses.push(res.data)))
        .catch(err => console.log(err))
        console.log(this.courses)
    }
   
  }
</script>