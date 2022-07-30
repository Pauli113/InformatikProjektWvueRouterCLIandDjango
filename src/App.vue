<template>
  <div id="nav">
    <router-link to="/input">Kurs erstellen</router-link>
    <router-link to="/myCourses">Meine Kurse</router-link>
  </div>
    <router-view/>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
//import InputPage from './components/InputPage.vue'

export default {
  name: 'App',
  components: {
    
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
