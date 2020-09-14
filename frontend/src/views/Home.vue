<template>
  <div class='wrap'>
    <div class="wrap-container home-container">
      <div class="schedule-box">
        <div class="recruit-box">
          <p class="recruit-header">추천공고</p>
          <div class="recruit-card-box">
            <div class="recruit-card">
              <div class="recruit-card-img-box">
                <img src="@/assets/images/samsung.png" alt="">
              </div>
              <p>삼성SDI</p>
            </div>
            <div class="recruit-card">
              <div class="recruit-card-img-box">
                <img src="@/assets/images/naver.png" alt="">
              </div>
              <p>네이버</p>
            </div>
            <div class="recruit-card">
              <div class="recruit-card-img-box">
                <img src="@/assets/images/kakao.png" alt="">
              </div>
              <p>카카오</p>
            </div>
          </div>
        </div>
        <div class="test-box">
          <p class="test-header">다가오는 시험</p>
          <div class="test-card-box">
            <div class="test-card">
              <div class="test-card-countdown countdown-lastday">D - 1</div>
              <div class="test-card-content">
                <p class="test-card-head">2020 기사 제4회 실기시험</p>
                <p class="test-card-footer">한국산업인력공단</p>
              </div>
            </div>
            <div class="test-card">
              <div class="test-card-countdown">D - 3</div>
              <div class="test-card-content">
                <p class="test-card-head">제49회 SQLD</p>
                <p class="test-card-footer">한국데이터산업진흥원</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="calendar-box">
        <p class="calendar-header">일정</p>
        <div class="calendar">
          <SingleDatePicker class='test' @selectDate='test()'/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SingleDatePicker from 'vue-single-date-picker';
import 'vue-single-date-picker/dist/vue-single-date-picker.css';

export default {
  name: 'Home',
  components: {
    SingleDatePicker
  },
  methods: {
    test() {
      console.log(event)
    }
  }
}
</script>

<style>
#single-date-picker {
  width: 100% !important;
}

.home-container {
  flex-direction: row;
}

.home-container .schedule-box {
}

.home-container .calendar-box {
  display: flex;
  flex-direction: column;
  margin-left: 50px;
}

.schedule-box .recruit-box {
  display: flex;
  flex-direction: column;
}

.recruit-box .recruit-header {
  margin: 40px 0 10px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.recruit-box .recruit-card-box {
  display: flex;
  justify-content: space-between;
}

.recruit-card-box .recruit-card {
  width: 220px;
  height: 280px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border-radius: 10px;
  border: 1px solid rgba(0,0,0,0);
  margin-right: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.recruit-card-box .recruit-card .recruit-card-img-box {
  display: flex;
  height: 70%;
  justify-content: center;
  align-items: center;
}

.recruit-card-box .recruit-card img {
  width: 70%;
}

.recruit-card-box .recruit-card p {
  font-size: 20px;
  font-weight: 700;
}

.schedule-box .test-box {
  display: flex;
  flex-direction: column;
}

.test-box .test-header {
  margin: 40px 0 10px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.test-box .test-card-box {
  display: flex;
  justify-content: space-between;
}

.test-card-box .test-card {
  min-width: 350px;
  height: 180px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border-radius: 10px;
  border: 1px solid rgba(0,0,0,0);
  margin-right: 20px;
  display: flex;
  flex-direction: column;
}

.test-card .test-card-countdown {
  width: 80px;
  height: 50px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px rgba(255,255,255,0.1),
            -0.5px -0.5px 0px rgba(0,0,0,0.05),
            0.5px 0.5px 0px rgba(0,0,0,0.05),
            0px 12px 10px -10px rgba(0,0,0,0.1);
  border: 1px solid rgba(0,0,0,0.01);
  border-radius: 20px;
  margin: 10px;
  font-weight: 900;
  display: flex;
  justify-content: center;
  align-items: center;
}

.test-card .countdown-lastday {
  color: red;
}

.test-card .test-card-content {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  width: 100%;
  height: 100%;
}

.test-card-content .test-card-head {
  font-size: 20px;
  font-weight: 900;
}

.test-card-content .test-card-footer {
  font-size: 15px;
  color: rgba(0,0,0,0.7)
}

.calendar-box .calendar-header {
  margin: 40px 0 10px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.calendar-box .calendar {
  width: 500px;
  height: 540px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
              -6px -6px 10px -1px rgba(255,255,255,0.7);
  border-radius: 10px;
  border: 1px solid rgba(0,0,0,0);
}
</style>