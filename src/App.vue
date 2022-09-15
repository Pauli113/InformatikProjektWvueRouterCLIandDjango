<template>
  <SideBar/>
</template>

<script>

//import GithubButton from "./components/GithubButton.vue";
import SideBar from "./components/sidebar/SideBar.vue";
import { sidebarWidth } from '@/components/sidebar/state'


export default {
  name: 'App',
  components: {
    SideBar
},
setup() {
    return { sidebarWidth }
  }
}
</script>

<style>
#app {
  /*text-align:center;*/
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding-left: 200px;
  width:100%

}


</style>
