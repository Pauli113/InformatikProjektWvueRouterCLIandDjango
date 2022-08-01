<template>
  <div id="nav">
    <router-link to="/input">Kurs erstellen</router-link>
    <router-link to="/myCourses">Meine Kurse</router-link>
    <GithubButton/>
  </div>
    <router-view/>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
//import InputPage from './components/InputPage.vue'
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
  margin-top: 60px;
}

#nav {
  width: 100%;
  overflow: auto;
}
</style>
