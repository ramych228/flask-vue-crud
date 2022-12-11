<template>
  <main class="wrapper">
    <IntroductionSection/>
    <BurseProjectFinder/>
  </main>
</template>

<script>
import IntroductionSection from "./IntroductionSection";
import BurseProjectFinder from "./BurseProjectFinder";

export default {
  name: "ExchangePage",
  components: {
    BurseProjectFinder,
    IntroductionSection,
  }
}
</script>

<style scoped>
main {
  background-color: #5f7a89;
}
</style>
