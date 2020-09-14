<template>
  <transition name="modal">
    <div class="mail-modal-mask" @click.self="$emit('close')">
      <i class="fas fa-times" @click.self="$emit('close')"></i>
      <div class="mail-modal-wrap">
        <div class="mail-modal-content">
          <div class='mail-modal-header'>계정을 <br> 인증하세요.</div>
          <div class='mail-modal-footer'>{{ email }}으로 <br>전송된 인증번호를 입력하세요.</div>
          <input v-model="validInput" class='mail-valid-input' type="text">
          <div v-if="!isSubmit" class='mail-valid-btn'>제출</div>
          <div v-if="isSubmit" class='mail-valid-btn mail-modal-submit'>제출</div>
          <div class='mail-valid-btn mail-modal-re'>다시보내기</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex';
// import Swal from 'sweetalert2'

export default {
  name: 'MailValidationModal',
  data() {
    return {
      email: "default@ssafy.com",
      validInput: '',
      isSubmit: false,
    }
  },
  watch: {
    validInput() {
      this.onSubmit()
    },
  },
  computed: {
    ...mapState(['signUpInput']),
  },
  created() {
    this.email = this.signUpInput
  },
  methods: {
    onSubmit() {
      if (this.validInput) {
        this.isSubmit = true
      } else {
        this.isSubmit = false
      }
    }
  }
}
</script>

<style scoped>
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

}

.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

}

.mail-modal-mask {
  position: fixed;
  z-index: 99999;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.mail-modal-mask .fa-times {
  position: absolute;
  top: 3vh;
  right: 3vh;
  cursor: pointer;
  color: #eff0f5;
  font-size: 5vh;
}

.modal-enter .mail-modal-wrapper,
.modal-leave-active .mail-modal-wrapper {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.mail-modal-wrap {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  padding: 1vh;
  transition: 0.3s ease;
  background-color: #eff0f5;
  border-radius: 1vw;
  width: 88%
}

@media (min-width: 450px) {
  .mail-modal-wrap {
  max-width: 50vh;
  width: 100%;
  margin: 0 auto;
  }
}

.mail-modal-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px;
}


.mail-modal-content .mail-modal-header {
  width: 100%;
  font-size: 30px;
  font-weight: 700;
  margin: 20px 0;
}

.mail-modal-content .mail-modal-footer {
  width: 100%;
  font-size: 18px;
  color: rgba(0,0,0,0.7);
  margin-bottom: 20px;
}

.mail-modal-content .mail-valid-input {
  width: 94%;
  height: 40px;
  padding-left: 6%;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
  border: 1px solid rgba(0,0,0,0.01);
  border-radius: 20px;
  outline: none;
  margin-bottom: 20px;
}

.mail-modal-content .mail-valid-btn {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border: 1px solid rgba(0,0,0,0);
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 14px;
  cursor: pointer;
  transition: .5s;
}

.mail-modal-content .mail-modal-submit {
  background-color: #80c3ff;
  font-weight: 700;
  transition: .5s;
}

.mail-modal-content .mail-modal-re:hover {
  background-color: rgb(253, 253, 150);
  font-weight: 700;
}
</style>
