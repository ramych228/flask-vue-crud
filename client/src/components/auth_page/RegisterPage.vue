<template>
  <div class="wrapper">
    <RegisterBlock/>
    <p>Уже есть аккаунт - <a href="./login">войди в него!</a></p>
  </div>
</template>

<script>
import RegisterBlock from "./RegisterBlock";

export default {
  name: "RegisterPage",

  components: {RegisterBlock}
}
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

p {
  margin-top: 20px;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  font-weight: 300;
}

a {
  color: #42b983;
  text-decoration: none;
}
</style>
