<template>
    <div class="loncom_index">
        zutai
    </div>
</template>

<script>

export default {
  created () {
    
        if(JSON.stringify(sessionStorage.loginInfo) == undefined){
            this.$message.warning("请登录");
            this.$router.push({path:'/login'});
            return;
        }


  },
  mounted() {
   
  },
  data() {
    return {
        
    }
  },
  methods:{
    
  }
  
}
</script>

