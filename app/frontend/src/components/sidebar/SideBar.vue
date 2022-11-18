
<template>
  <div class="sidebar">
   <h3>
    Editor
   </h3>


  <router-link to="/input" class="links">Editor</router-link>
  <router-link to="/allCourses" class="links">Alle Kurse</router-link>

  
  </div>
  <router-view/>
</template>

<script>

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

  width: 180px;

}
.sidebar h1 {
  height: 2.5em;
}

.links {
  color: white;
  margin-top: 20px;
}



</style>