<template>
  <div class="container">
    <div class="photo"></div>
    <b class="text_name">{{ student.name }}</b>
    <p class="text_description">{{ student.description }}</p>
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
  justify-content: flex-end;
  width: 300px;
  height: 400px;
  border: 1px solid white;
  margin: 10px;
  padding-bottom: 20px;
  gap: 10px;
}


.photo {
  width: 100px;
  flex-grow: 1;
  background: url("../../../assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-color: red;
}


.text_name {
  font-family: 'Montserrat', sans-serif;
  text-align: center;
  margin-top: 0px;
  margin-bottom: 0px;
}

.text_description {
  font-family: 'Montserrat', sans-serif;
  text-align: center;
  margin-top: 0px;
  margin-bottom: 0px;
}

.details-button {
  width: 60%;
  height: 10%;
  font-size: 3px;

}
</style>
