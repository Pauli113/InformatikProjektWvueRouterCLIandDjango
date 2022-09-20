<template>
  <SideBar/>
</template>

<script>

import SideBar from "./components/sidebar/SideBar.vue";


export default {
  name: 'App',
  components: {
    SideBar
},

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding-left: 200px;
  width:100%

}


</style>
