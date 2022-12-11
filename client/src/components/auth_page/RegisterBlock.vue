<template>
  <div class="wrapper">
    <h1>Регистрация</h1>
    <form>
      <div class="input-wrapper">
        <label for="login">Логин</label>
        <input type="text" id="login" v-model="login">
      </div>
      <div class="input-wrapper">
        <label for="FIO">ФИО</label>
        <input type="text" id="FIO" v-model="fio">
      </div>
      <div class="input-wrapper">
        <label for="role">Роль</label>
        <select id="role" v-model="role">
          <option value="student">Студент</option>
          <option value="investor">Инвестор</option>
        </select>
      </div>
      <div class="input-wrapper">
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password">
      </div>
      <div class="input-wrapper">
        <label for="password">Повторите пароль</label>
        <input type="password" id="password" v-model="passwordRepeat">
      </div>
      <p id="error_text" class="error-text"></p>
      <div class="input-wrapper">
        <button type="button" @click="registerUser">Зарегистрироваться</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterBlock",

  data() {
    return {
      login: "",
      fio: "",
      role: "student",
      password: "",
      passwordRepeat: ""
    }
  },

  methods: {
    registerUser() {
      if (this.password !== this.passwordRepeat) {
        document.getElementById("error_text").innerText = "Пароли не совпадают";
        return;
      }

      if (this.login === "" || this.fio === "" || this.password === "") {
        document.getElementById("error_text").innerText = "Заполните все поля";
        return;
      }

      axios.post("http://localhost:5000/api/register", {
        login: this.login,
        fio: this.fio,
        role: this.role,
        password: this.password
      }).then(response => {
        localStorage.setItem("token", response.data.user.token);
        localStorage.setItem("role", response.data.user.role);
        localStorage.setItem("fio", response.data.user.fio);
        localStorage.setItem("login", response.data.user.login);
        this.$router.push("/");
      }).catch(error => {
        document.getElementById("error_text").innerText = "Ошибка регистрации";
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

.input-wrapper select {
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
  background-color: rgba(84,162,231,0);
  color: white;
}

.input-wrapper select:focus {
  outline: none;
}

.input-wrapper > select > option {
  background: rgba(0,0,0,1);
  color: white;
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
