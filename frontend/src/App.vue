<template>
  <div id="app">
    <div id="nav" v-show="!isLogin">
      <div class="logo-box" @click="goHome">MY RESUME</div>
      <div class="menu-bar-box">
        <div class="menu-bar">이력서</div>
        <div class="menu-bar">취업달력</div>
        <div class="menu-bar">교육</div>
        <div class="menu-bar">검색</div>
      </div>
      <div class="user-box">
        <div class="user-bar" @click="goLogin">로그인</div>
        <div class="user-bar">회원가입</div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import "../public/css/common.css";
import { mapState } from 'vuex';
export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods: {
    goHome() {
      this.$router.push('/')
    },
    goLogin() {
      this.$router.push('/login')
    }
  },
  computed: {
    ...mapState(['isLogin']),
  }
}
</script>

<style>
  #nav {
    height: 7vh;
    min-height: 30px;
    background-color: #eff0f5;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
                -6px -6px 10px -1px rgba(255,255,255,0.7);
    border: 1px solid rgba(0,0,0,0);
    z-index: 5000;
    display: flex;
  }

  #nav .logo-box {
    /* background-color: aqua; */
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Black Han Sans', sans-serif;
    font-weight: 900;
    font-size: 25px;
    letter-spacing: -1px;
    cursor: pointer;
    margin-left: 2%;
    color: #0F4C81;
  }

  #nav .menu-bar-box {
    width: 68%;
    /* background-color: bisque; */
    display: flex;
    align-items: center;
  }

  #nav .user-box {
    width: 20%;
    /* background-color: blueviolet; */
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .menu-bar-box .menu-bar {
    width: 70px;
    height: 60%;
    /* background-color: cadetblue; */
    margin: 0 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    border-radius: 20px;
    color: rgba(0,0,0,0.8);
    cursor: pointer;
  }

  .menu-bar-box .menu-bar:hover {
    box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
    border: 1px solid rgba(0,0,0,0.01);
    font-weight: 900;
  }

  .user-box .user-bar {
    width: 70px;
    height: 60%;
    /* background-color: cadetblue; */
    margin-right:30px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    border-radius: 20px;
    color: rgba(0,0,0,0.8);
    cursor: pointer;
  }

  .user-box .user-bar:hover {
    box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
    border: 1px solid rgba(0,0,0,0.01);
    font-weight: 900;
  }
</style>
