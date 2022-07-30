<template>
<label>
      {{label}}
      <input :type="type" v-model="inputValue">
  </label>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    label: String
  },
  computed:{
      inputValue:{
            get(){
                return this.modelValue
            },
            set(value){
                this.$emit('update:modelValue', value)
            }
        }
  },
    data(){
     return {
            
        }
     }
}
</script>