<template>
    <div class="loncom_content">
        首页
    </div>
</template>


<script>

export default {
    created () {
        if(JSON.stringify(sessionStorage.loginInfo) == undefined){
            this.$message.warning("请登录系统");
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
        

    },
    components:{}
}
</script>




