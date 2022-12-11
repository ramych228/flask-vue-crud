<template>
  <div class="container">
    <div class="header">
      <h3>{{project.name}}</h3>
      <p>></p>
    </div>
    <p>{{project.brief}}</p>
    <button @click="AddStudent" id="add_student">Записаться на проект</button>
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
  width: 300px;
  height: 300px;
  padding: 10px;
  gap: 10px;
  border-radius: 10px;
  border: 1px solid white;
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
</style>
