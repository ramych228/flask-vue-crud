<template>
  <div class="wrapper">
    <h1>Вход</h1>
    <form>
      <div class="input-wrapper">
        <label for="login">Логин</label>
        <input type="text" id="login" v-model="login">
      </div>
      <div class="input-wrapper">
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password">
      </div>
      <p id="error_text" class="error-text"></p>
      <div class="input-wrapper">
        <button type="button" @click="loginUser">Войти</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginBlock",

  data() {
    return {
      login: "",
      password: ""
    }
  },

  methods: {
    loginUser() {
      if (this.login === "" || this.password === "") {
        document.getElementById("error_text").innerText = "Заполните все поля";
        return;
      }

      axios.post("http://localhost:5000/api/login", {
        login: this.login,
        password: this.password
      }).then(response => {
        localStorage.setItem("loginToken", response.data.token);
      }).catch(error => {
        document.getElementById("error_text").innerText = "Неверный логин или пароль";
      })
    }
  }
}
</script>

<style scoped>
.wrapper {
  height: fit-content;
  border: 3px solid white;
  border-radius: 20px;

  padding: 20px 40px;

  font-family: 'Roboto', sans-serif;
}

.input-wrapper {
  margin: 20px 0;
}

.input-wrapper label {
  display: block;
  margin-bottom: 5px;
}

.input-wrapper input {
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
  background-color: rgba(84,162,231,0);
  color: white;
}

.input-wrapper input:focus {
  outline: none;
}

.error-text {
  color: #53e3a2;
  font-size: 14px;
  margin: 0;
}

.input-wrapper button {
  width: 100%;
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
  background-color: #266b4c;
  color: white;
  cursor: pointer;
}

.input-wrapper button:hover {
  background-color: #2e8e5e;
}
</style>
