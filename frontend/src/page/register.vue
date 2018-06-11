<template>
<div class="seafood">
    <div class="register_con">
		<div class="l_con fl">
			<a class="reg_logo"><img src="/static/images/logo02.png"></a>
			<div class="reg_slogan">足不出户  ·  新鲜每一天</div>
			<div class="reg_banner"></div>
		</div>

		<div class="r_con fr">
			<div class="reg_title clearfix">
				<h1>用户注册</h1>
                <router-link to="/login">登录</router-link>
			</div>
			<div class="reg_form clearfix">
				<el-form :model="form_info" :rules="form_rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                    <el-form-item label="用户名:" prop="username">
                        <el-input v-model="form_info.username" placeholder="请输入用户名"></el-input>
                    </el-form-item>
                    <el-form-item label="密码:" prop="password">
                        <el-input v-model="form_info.password" placeholder="请输入密码" type="password"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码:" prop="cpassword">
                        <el-input v-model="form_info.cpassword" placeholder="请再次输入密码" type="password"  @keyup.native="keyLogin($event,'ruleForm')"></el-input>
                    </el-form-item>
                    <el-form-item label="邮箱:">
                        <el-input v-model="form_info.email" placeholder="请输入邮箱"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="submitForm('ruleForm')" size="small" @keydown="keyLogin($event,'ruleForm')">立即注册</el-button>
                        <el-button @click="resetForm('ruleForm')" size="small">重置</el-button>
                    </el-form-item>
				</el-form>
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
		<p>CopyRight © 2016 四川天天生鲜信息技术有限公司 All Rights Reserved</p>
		<p>电话：028-****888    蜀ICP备*******8号</p>
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
            cpassword:'',
            email:'',

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
            cpassword:[
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
            this.$api.post('/user/register', this.form_info, r => {
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
