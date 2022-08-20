<template>
  <div id="nav">
    <router-link to="/input">Kurs erstellen</router-link>
    <router-link to="/myCourses">Meine Kurse</router-link>
    <GithubButton/>
  </div>
    <router-view/>
</template>

<script>

import GithubButton from "./components/GithubButton.vue";


export default {
  name: 'App',
  components: {
    GithubButton
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
  
}


#app nav {
    margin: 30px;
    width:100%;
    float: left;
    display:block;
}
</style>
