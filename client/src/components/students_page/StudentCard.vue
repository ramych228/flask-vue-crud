<template>
  <div class="container">
    <img src="assets/logo.png" alt="student-card">
    <b>{{ student.name }}</b>
    <p>{{ student.description }}</p>
    <PrimeButton class="details-button" text="Подробнее" type="2"/>
  </div>
</template>

<script>
import PrimeButton from "../default_components/PrimeButton";
export default {
  name: "StudentCard",
  components: {
    PrimeButton
  },

  props: {
    student: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 300px;
  border: 1px solid white;
  margin: 10px;
  gap: 10px;
}

.details-button {
  width: 60%;
  height: 10%;
  font-size: 13px;
}
</style>
