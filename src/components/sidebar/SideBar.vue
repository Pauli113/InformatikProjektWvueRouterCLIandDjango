

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
   <h3>
    Editor
   </h3>


  <router-link to="/input">Editor</router-link>
  <router-link to="/myCourses">Meine Kurse</router-link>
  <router-link to="/login">Login</router-link>


  
  </div>
  <router-view/>
</template>

<script>
import {  sidebarWidth } from './state'

export default {
  props: {},
  setup() {
    return {  sidebarWidth }
  }
}
</script>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;

}
.sidebar h1 {
  height: 2.5em;
}

</style>