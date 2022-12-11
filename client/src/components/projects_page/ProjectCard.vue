<template>
  <div class="container">
    <div class="header">
      <h3 class="text_name">{{project.name}}</h3>
      <p class="arrow">⟩</p>
    </div>
    <p>{{project.brief}}</p>
    <button @click="AddStudent" id="add_student">Записаться на проект</button>
    <p class="text_brief">{{project.brief}}</p>
  </div>
</template>

<script>
import PrimeButton from "../default_components/PrimeButton";
import axios from "axios";
export default {
  name: "ProjectCard",
  components: {PrimeButton},
  props: {
    project: {
      type: Object,
      required: true
    }
  },

  methods: {
    AddStudent() {
      axios.post("http://localhost:5000/api/projects/add", {
        project_id: this.project.id,
        student_id: localStorage.getItem("token")
      }).then(response => {
        alert("Вы записаны на проект");
      }).catch(error => {
        console.log(error);
      })
    }
  },

  mounted() {
    this.$el.style.backgroundImage = `url(${this.project.image_path})`;

    if (localStorage.getItem("role") !== "student") {
      this.$el.querySelector("#add_student").style.display = "none";
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 250px;
  height: 150px;
  padding: 10px;
  gap: 10px;
  border-radius: 10px;
  background-repeat: no-repeat;
  background-size: 200%;
  transition: all 1s;
  font-family: 'Montserrat', sans-serif;
  padding-left: 25px;
  padding-right: 25px;
  filter: brightness(75%);
}
.container:hover {
  transition: all 0.5s;
  background-size: 210%; 
}

.header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
button {
  width: 80%;
  height: 30px;
  border-radius: 5px;
  border: none;
  background-color: #266b4c;
  color: white;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

button:hover {
  background-color: #1e4f3a;
}

.text_name {
  font-family: 'Montserrat', sans-serif;
}
.text_brief {
  font-family: 'Montserrat', sans-serif;
}
.arrow{
  font-family: 'Montserrat', sans-serif;
  font-size: 2em;
  margin-top: 0;
  margin-bottom: 0;
}
</style>
