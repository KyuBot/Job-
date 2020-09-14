<template>
  <div class="login-container">
    <div class="login-form-box">
      <div class="login-button-box">
        <div id="login-btn"></div>
        <div class="login-toggle-btn login-toggle" @click="onLogin">Login</div>
        <div class="login-toggle-btn signup-toggle" @click="onSignup">Signup</div>
      </div>
      <div class="login-logo-img" @click="goHome">
        <img src="@/assets/images/resume.png" alt="">
      </div>
      <p class='login-logo-text' @click="goHome">MY RESUME</p>
      <form id="login" class="login-input-group">
        <input v-model="loginMail" type="email" class="login-input-field" placeholder="Email" required>
        <input v-model="loginPassword" type="password" class="login-input-field" placeholder="Password" required>
        <div class="login-submit-btn" @click="goLogin">Login</div>
      </form>
      <form id="signup" class="login-input-group">
        <div class="signup-email">
          <input v-model="signUpMail" type="email" class="login-input-field login-input-email" placeholder="Email" required>
          <span @click="onModal">인증받기</span>
        </div>
        <div class='signup-name'>
          <input v-model="signUpFirst" type="text" class="login-input-field login-input-first" placeholder="First Name" required>
          <input v-model="signUpLast" type="text" class="login-input-field login-input-last" placeholder="Last Name" required>
        </div>
        <input v-model="signUpPassword" type="password" class="login-input-field" placeholder="Password" required>
        <input v-model="signUpPasswordConfirm" type="password" class="login-input-field" placeholder="Password Confirm" required>
        <div class="login-submit-btn">Signup</div>
      </form>
    </div>

    <MailValidationModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
import MailValidationModal from '../components/MailValidationModal.vue'
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'Login',
  data() {
    return {
      showModal: false,
      loginMail: '',
      loginPassword: '',
      signUpMail: '',
      signUpFirst: '',
      signUpLast: '',
      signUpPassword: '',
      signUpPasswordConfirm: '',
    }
  },
  components: {
    MailValidationModal,
  },
  mounted() {
    this.setIsLogin(true)
  },
  methods: {
    ...mapMutations(['setIsLogin', 'setMailInput']),
    onLogin() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box')

      LOGIN.style.left = "50px";
      SIGNUP.style.left = "450px";
      BTN.style.left = "0";
      FORM.style.height = "480px";
    },
    onSignup() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box')

      LOGIN.style.left = "-400px";
      SIGNUP.style.left = "50px";
      BTN.style.left = "50%";
      FORM.style.height = "590px";
    },
    goHome() {
      this.$router.push('/')
    },
    onModal() {
      this.showModal = true;
      this.setMailInput(this.signUpMail)
    },
    goLogin() {
      const loginData = {
        email: this.loginMail,
        password: this.loginPassword
      }

      axios.post(SERVER_URL + 'rest-auth/login/', loginData)
        .then(res => {
          console.log(res.data)
          // this.$cookies.set('auth-token', res.data.key)
          // this.isLoggedIn = true
          // this.sendUserInfo()
          // this.goKids()
          // this.$router.go()

          
        })
        .catch((err) =>
          console.log(err.data))
    },
  },
  beforeDestroy() { 
    this.setIsLogin(false)
  }
}
</script>

<style>
.login-form-box {
  width: 380px;
  height: 480px;
  position: relative;
  margin: 3.5% auto;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border: 1px solid rgba(0,0,0,0);
  border-radius: 10px;
  padding: 5px;
  overflow: hidden;
  transition: .5s;
}

.login-form-box .login-logo-img {
  width: 100px;
  height: 100px;
  background-color: #80c3ff;
  margin: 0 auto;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.login-form-box .login-logo-img img {
  width: 70%;
  height: 70%;
}

.login-form-box .login-logo-text {
  margin: 0 auto;
  width: 130px;
  text-align: center;
  font-size: 20px;
  font-weight: 900;
  margin-bottom: 50px;
  cursor: pointer;
}

.login-button-box {
  width: 230px;
  margin: 35px auto;
  position: relative;
  display: flex;
  justify-content: space-between;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border-radius: 30px;
}

.login-toggle-btn {
  width: 50%;
  padding: 10px 0;
  text-align: center;
  cursor: pointer;
  background: transparent;
  border: 0;
  outline: none;
  position: relative;
}

#login-btn {
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 100%;
  background: linear-gradient(to right, #0088ff, #b9deff);
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
  border-radius: 30px;
  transition: .5s;
}

.login-input-group {
  position: absolute;
  top: 280px;
  width: 280px;
  transition: .5s;
}

.login-input-field {
  width: 94%;
  height: 40px;
  line-height: 40px;
  padding-left: 6%;
  margin: 5px 0;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
  border: 1px solid rgba(0,0,0,0.01);
  border-radius: 20px;
  outline: none;
  background: transparent;
}

.login-submit-btn {
  height: 40px;
  line-height: 40px;
  cursor: pointer;
  display: block;
  margin: auto;
  margin-top: 30px;
  background: linear-gradient(to right, #0075db, #a3d4ff);
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
            -6px -6px 10px -1px rgba(255,255,255,0.7);
  border: 0;
  outline: none;
  border-radius: 30px;
  text-align: center;
  color: rgba(255,255,255,0.9);
}

#login {
  left: 50px;
}

#signup {
  left: 450px;
}

.signup-email {
  position: relative;
}

.signup-email span {
  position: absolute;
  top: 50%;
  right: 2%;
  transform: translate(0, -50%);
  font-size: 12px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
            -6px -6px 10px -1px rgba(255,255,255,0.7);
  padding: 5px 10px;
  border-radius: 30px;
  color: rgba(0,0,0,0.5);
  transition: .5s;
  cursor: pointer;
}

.signup-email span:hover {
  background: #0088ff;
  color: #fff;
  font-weight: 700;
}

.login-input-email {
  width: 70%;
  padding-right: 24%;
}

.signup-name {
  width: 100%;
  display: flex;
}

.login-input-last {
  width: 70%;
  margin-left: 10px;
}
</style>