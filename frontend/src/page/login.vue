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
                        <form>
                            <input type="text" name="username" class="name_input" placeholder="请输入用户名">
                            <div class="user_error"></div>
                            <input type="password" name="pwd" class="pass_input" placeholder="请输入密码">
                            <div class="pwd_error"></div>
                            <div class="more_input clearfix">
                                <input type="checkbox" name="">
                                <label>记住用户名</label>
                                <a href="#">忘记密码</a>
                            </div>
                            <input type="submit" name="" value="登录" class="input_submit">
                        </form>
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
        
  	}
  },
  methods:{
      
  }
}
</script>