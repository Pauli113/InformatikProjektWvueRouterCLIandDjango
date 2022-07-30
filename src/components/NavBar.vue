<template>
<!--
    <ul>
        <li><a href="index.html">Kurs erstellen</a></li> 
        <li><a href="mycourses.html">Meine Kurse</a></li>  
        <li><login-button/></li>
    </ul>   -->
    <div id="nav">
        
            <router-link to="/">Kurs erstellen</router-link>
        <router-link to="/">Meine Kurse</router-link>
        <GithubButton/>
        
         
        
       
    
        <!--
          <ul>
        <li><a href="index.html">Kurs erstellen</a></li> 
        <li><a href="mycourses.html">Meine Kurse</a></li>  
        <li><GithubButton/></li>
      </ul> 
        -->
        
    </div>
    <router-view/>
</template>

<script>
    import GithubButton from "./GithubButton.vue";
    export default {
        name: 'NavBar',
        components: {
            GithubButton
        }
    }
</script>



<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  width: 100%;
}

li {
  float: left;
}

li a {
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}


</style>