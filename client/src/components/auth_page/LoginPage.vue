<template>
  <div class="wrapper">
    <LoginBlock/>
    <p>Нет аккаунта - <a href="./register">создай его!</a></p>
  </div>
</template>

<script>
import LoginBlock from "./LoginBlock";

export default {
  name: "AuthPage",

  components: {LoginBlock}
}
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 90vh;
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
