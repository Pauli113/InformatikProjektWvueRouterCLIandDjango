<template>
    <h1>Modulhandbucheditor</h1> 
    <NavBar/>
    <ModuleForm/>
</template>

<script>

import ModuleForm from './ModuleForm.vue'
import NavBar from './NavBar.vue'



export default {
  name: 'InputPage',
  components: {
    ModuleForm,
    NavBar
  }
}

</script>