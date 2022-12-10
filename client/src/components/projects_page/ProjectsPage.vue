<template>
  <div class="container">
    <h1>
      Проекты
    </h1>
    <p>От ведущих компаний</p>
    <h3>Цифровой платформы</h3>

    <ProjectTable :projects="projects"/>
    <div class="partner-container">
      <div class="partner-text">
        <h2>Станьте партнером ЦИФРОВОЙ ПЛАТФОРМЫ</h2>
        <p>Отправьте заявку с проектом от вашей компании.
          Наши студенты займутся его реализацией.
        <p/>
      </div>
      <PrimeButton text="Создать проект"/>
    </div>
  </div>
</template>

<script>
import ProjectCard from "./ProjectCard";
import ProjectTable from "./ProjectTable";
import PrimeButton from "../default_components/PrimeButton";
import axios from "axios";

export default {
  name: "ProjectsPage",
  components: {
    ProjectTable,
    ProjectCard,
    PrimeButton
  },
  methods: {
    fetchProjects() {
      axios.get("http://localhost:5000/api/projects")
        .then(response => {
          this.projects = response.data.projects;
        })
        .catch(error => {
          console.log(error);
        });
      // this.projects = [
      //   {
      //     id: 1,
      //     name: "Проект 1",
      //     brief: "Описание проекта 1",
      //   },
      //   {
      //     id: 2,
      //     name: "Проект 2",
      //     brief: "Описание проекта 2",
      //   },
      //   {
      //     id: 3,
      //     name: "Проект 3",
      //     brief: "Описание проекта 3",
      //   },
      //   {
      //     id: 4,
      //     name: "Проект 4",
      //     brief: "Описание проекта 4",
      //   },
      //   {
      //     id: 5,
      //     name: "Проект 5",
      //     brief: "Описание проекта 5",
      //   },
      //   {
      //     id: 6,
      //     name: "Проект 6",
      //     brief: "Описание проекта 6",
      //   },
      //   {
      //     id: 7,
      //     name: "Проект 7",
      //     brief: "Описание проекта 7",
      //   },
      //   {
      //     id: 8,
      //     name: "Проект 8",
      //     brief: "Описание проекта 8",
      //   },
      //   {
      //     id: 9,
      //     name: "Проект 9",
      //     brief: "Описание проекта 9",
      //   },
      //   {
      //     id: 10,
      //     name: "Проект 10",
      //     brief: "Описание проекта 10",
      //   },
      // ];
    }
  },
  data() {
    return {
      projects: []
    }
  },
  mounted() {
    this.fetchProjects();
  }

}
</script>

<style scoped>
.partner-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  gap: 80px;
}
</style>
