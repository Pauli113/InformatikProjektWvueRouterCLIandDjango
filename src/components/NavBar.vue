<template>
    <div id="nav">
        
        <router-link to="/">Kurs erstellen</router-link>
        <router-link to="/">Meine Kurse</router-link>
        <GithubButton/>
        
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
</style>



<style>



</style>