<template>
    <div class="seafood">
        <div class="login_top clearfix">
            <a href="index.html" class="login_logo"><img src="static/images/logo02.png"></a>	
        </div>

        <div class="login_form_bg">
            <div class="login_form_wrap clearfix">
                <div class="login_banner fl"></div>
                <div class="slogan fl">日夜兼程 · 急速送达</div>
                <div class="login_form fr">
                    <div class="login_title clearfix">
                        <h1>用户登录</h1>
                        <router-link to="/register">立即注册</router-link>
                    </div>
                    <div class="form_input">
                        <el-form :model="form_info" :rules="form_rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                            <el-input v-model="form_info.username" placeholder="请输入用户名" class="info_input"></el-input>
                            <el-input v-model="form_info.password" placeholder="请输入密码" class="info_input" type="password"></el-input>
                            <div class="more_input clearfix">
                                <input type="checkbox" name="">
                                <label>记住用户名</label>
                                <a href="#">忘记密码</a>
                            </div>
                            <el-button type="primary" @click="submitForm('ruleForm')" @keydown="keyLogin($event,'ruleForm')" style="width: 100%;"> 登录 </el-button>
                        </el-form>
                        
                    </div>
                </div>
            </div>
        </div>

        <div class="footer no-mp">
            <div class="foot_link">
                <a href="#">关于我们</a>
                <span>|</span>
                <a href="#">联系我们</a>
                <span>|</span>
                <a href="#">招聘人才</a>
                <span>|</span>
                <a href="#">友情链接</a>		
            </div>
            <p>CopyRight © 2016 北京天天生鲜信息技术有限公司 All Rights Reserved</p>
            <p>电话：010-****888    京ICP备*******8号</p>
        </div>
    </div>
</template>

<script>
export default {
  
 data(){
  
  	return {
        form_info:{
            username:'',
            password:'',

        },
        form_rules:{
            username:[
                { required: true, message: '请输入用户名', trigger: 'blur' },
                { min: 2, max: 8, message: '长度在 2 到 8 个字符', trigger: 'blur' }
            ],
            password:[
                { required: true, message: '请输入密码', trigger: 'blur' },
                { min: 6, max: 18, message: '长度在 6 到 18 位', trigger: 'blur' }
            ],
        },
  	}
  },
  methods:{
      keyLogin:function(ev,ruleForm){
        if(ev.keyCode == 13){
          this.submitForm(ruleForm);
        }
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$api.post('/user/login', this.form_info, r => {
                console.log(r)
                if(r.success){
                    this.$message.success(r.msg);
                }else{
                    this.$message.error(r.msg);
                }
            })
            
          } 
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
  }
}
</script>