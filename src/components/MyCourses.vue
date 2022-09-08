<template>
  <h1>Meine Kurse</h1>
  <input placeholder="Kurs suchen" type="text" v-model="query">
  <button v-on:click="getCourses">Meine Kurse suchen</button>
  
 <div v-for="course in courses" :key="course">
    <p>{{course}}</p>
  </div>
  
  <!--
<table>
  <thead>
    <tr>
      <td>Kurse</td>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(course,index) in courses" :key="index">
    </tr>

  </tbody>
 </table>
  -->
 
</template>

<script>
import axios from 'axios';

  export default{
  
    data(){
      return {
        courses:[],
        query:''
      }
    },
    beforeCreate() {
        axios.get("http://localhost:8000/api/courses/")
        .then(res => (this.courses.push(res.data)))
        .catch(err => console.log(err))
        console.log(this.courses)
    },
    getCourses(){
      return this.courses.filter((course)=>
        course.toLowerCase().includes(this.query.value.toLowerCase())
      )
    }



   
  }
</script>