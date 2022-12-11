<template>
  <div class="wrapper">
    <WaveHole/>
    <WaveHole/>
    <WaveHole/>
    <WaveHole/>
    <p class="solid-header-text">БИРЖА</p><br/>
    <p class="hollow-header-text">ЦИФРОВОЙ</p><br/>
    <p class="hollow-header-text">ПЛАТФОРМЫ</p>
    <p class="solid-subheader-text">Самые амбициозные проекты студентов передовой инженерной школы ИТМО</p>
    <PrimeButton :texts="['Подать заявку', 'Найти инвестиции', 'Развивать стартап']" type="black-shadow"/>
  </div>
</template>

<script>
import PrimeButton from "../default_components/PrimeButton";
import WaveHole from "./WaveHole";
export default {
  name: "IntroductionSection",
  components: {WaveHole, PrimeButton}
}
</script>

<style scoped>
.wrapper {
  background-color: #2c3e50;
  padding: 50px 0;
}
</style>
