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
        <p v-if="!isLoginValid" class='signup-err-msg'>이메일 또는 비밀번호를 확인하세요.</p>
        <input v-model="loginMail" type="email" class="login-input-field" placeholder="Email" required @keydown.enter="goLogin">
        <input v-model="loginPassword" type="password" class="login-input-field" placeholder="Password" required @keydown.enter="goLogin">
        <div v-show="!isLoginBtn" class="login-submit-btn">Login</div>
        <div v-show="isLoginBtn" class="login-submit-btn on-login-btn" @click="goLogin">Login</div>
      </form>
      <form id="signup" class="login-input-group">
        <p v-if='!passwordSchema.validate(signUpPassword) && (signUpPassword.length>0)' class='signup-err-msg'>비밀번호는 영문, 숫자 포함 8자리 이상이어야 합니다.</p>
        <p v-if='(passwordSchema.validate(signUpPassword)) && (signUpPassword != signUpPasswordConfirm)' class='signup-err-msg'>비밀번호가 일치하지 않습니다.</p>
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
        <div v-show="!isSignBtn" class="login-submit-btn">Signup</div>
        <div v-show="isSignBtn" class="login-submit-btn on-login-btn" @click="setSignup">Signup</div>
      </form>
    </div>

    <MailValidationModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import MailValidationModal from '../components/MailValidationModal.vue'
import PasswordValidator from 'password-validator'
import '../components/css/login.css'
import axios from 'axios';
import Swal from 'sweetalert2'

const SERVER_URL = 'http://j3b104.p.ssafy.io/api/'

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
      isLoginValid: true,
      isSignBtn: false,
      isLoginBtn: false,
      isPasswordValid: false,
      passwordSchema: new PasswordValidator(),
    }
  },
  components: {
    MailValidationModal,
  },
  computed: {
    ...mapState(['mailValid', 'loginPath']),
  },
  created() {
    this.passwordSchema
      .is().min(8)
      .is().max(100)
      .has().digits()
      .has().letters();
  },
  mounted() {
    this.setIsLogin(true)
    if (this.loginPath === 'login') {
      this.onLogin()
    } else {
      this.onSignup()
    }
  },
  watch: {
    signUpMail() {
      this.checkSingupForm()
    },
    signUpFirst() {
      this.checkSingupForm()
    },
    signUpLast() {
      this.checkSingupForm()
    },
    signUpPassword() {
      this.checkPassword()
      this.checkSingupForm()
    },
    signUpPasswordConfirm() {
      this.checkPassword()
      this.checkSingupForm()
    },
    mailValid() {
      this.checkSingupForm()
    },
    loginMail() {
      this.checkLoginForm()
    },
    loginPassword() {
      this.checkLoginForm()
    }
  },
  methods: {
    ...mapMutations(['setIsLogin', 'setMailInput', 'setMailCode', 'setIsLoggedIn', 'setToken']),
    onLogin() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box');
      const LOGIN_TOGGLE = document.querySelector('.login-toggle');
      const SIGNUP_TOGGLE = document.querySelector('.signup-toggle');

      LOGIN.style.left = "50px";
      SIGNUP.style.left = "450px";
      BTN.style.left = "0";
      FORM.style.height = "480px";
      LOGIN_TOGGLE.style.color = 'rgba(0,0,0,0.8)'
      SIGNUP_TOGGLE.style.color = 'rgba(0,0,0,0.3)'
    },
    onSignup() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box');
      const LOGIN_TOGGLE = document.querySelector('.login-toggle');
      const SIGNUP_TOGGLE = document.querySelector('.signup-toggle');

      LOGIN.style.left = "-400px";
      SIGNUP.style.left = "50px";
      BTN.style.left = "50%";
      FORM.style.height = "590px";
      LOGIN_TOGGLE.style.color = 'rgba(0,0,0,0.3)'
      SIGNUP_TOGGLE.style.color = 'rgba(0,0,0,0.8)'
    },
    goHome() {
      this.$router.push('/')
    },
    goLogin() {
      const loginData = {
        email: this.loginMail,
        password: this.loginPassword
      }

      axios.post(SERVER_URL + 'rest-auth/login/', loginData)
        .then(res => {
          console.log(res.data)
          this.isLoginValid = true
          this.$cookies.set('auth-token', res.data.key)
          this.setToken(res.data.key)
          this.setIsLoggedIn(true)
          this.$router.push('/')
        })
        .catch(() => this.isLoginValid = false)
    },
    onModal() {
      this.showModal = true;
      this.setMailInput(this.signUpMail)
      axios.post(SERVER_URL + `accounts/${this.signUpMail}/`)
        .then(res => {
          console.log(res.data.result)
          this.setMailCode(res.data.result)
        })
        .catch((err) =>
          console.log(err.data))
    },
    checkSingupForm() {
      if(this.signUpMail && this.signUpFirst && this.signUpLast && this.signUpPassword && 
      this.signUpPasswordConfirm && this.mailValid && this.isPasswordValid) {
        this.isSignBtn = true
      } else {
        this.isSignBtn = false
      }
    },
    checkLoginForm() {
      if(this.loginMail && this.loginPassword) {
        this.isLoginBtn = true
      } else {
        this.isLoginBtn = false
      }
    },
    checkPassword() {
      if((this.signUpPassword == this.signUpPasswordConfirm) && this.passwordSchema.validate(this.signUpPassword)) {
        this.isPasswordValid = true
      } else {
        this.isPasswordValid = false
      }
    },
    setSignup() {
      const signupData = {
        email: this.signUpMail,
        password1: this.signUpPassword,
        password2: this.signUpPasswordConfirm,
        first_name: this.signUpFirst,
        last_name: this.signUpLast
      }
      axios.post(SERVER_URL + 'rest-auth/signup/', signupData)
        .then(res => {
          console.log(res.data)
          this.$cookies.set('auth-token', res.data.key)
          this.setToken(res.data.key)
          this.setIsLoggedIn(true)
          Swal.fire({
            icon: 'success',
            title: '환영합니다',
            confirmButtonText: '확인'
          }).then((result) => {
            if (result.value) {
              this.$router.push('/resume')
            }
          })
        })
        .catch((err) => console.log(err))
    }
  },
  beforeDestroy() { 
    this.setIsLogin(false)
  }
}
</script>