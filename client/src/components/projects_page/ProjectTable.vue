<template>
  <div class="container">
    <ProjectCard v-for="project in projects" :project="project" :key="project.id"/>
  </div>
</template>

<script>
import ProjectCard from "./ProjectCard";

export default {
  name: "ProjectTable",
  components: {ProjectCard},
  props: {
    projects: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  gap: 30px;
}
</style>
