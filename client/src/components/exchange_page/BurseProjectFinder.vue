<template>
  <div class="wrapper">
    <div class="filter">
      <p>Направление</p>
      <ul>
        <li v-for="direction in directions" :key="direction.id">
          <input type="checkbox" :id="direction.id" :value="direction.id" v-model="selectedDirections">
          <label :for="direction.id">{{ direction.name }}</label>
        </li>
      </ul>
    </div>

    <div class="projects-table">
      <BurseProjectCard v-for="project in projects" :project="project" :key="project.id"/>
    </div>
  </div>
</template>

<script>
import BurseProjectCard from "./BurseProjectCard";
export default {
  name: "BurseProjectFinder",
  components: {BurseProjectCard},
  data() {
    return {
      selectedDirections: [],
      directions: [
        {id: 1, name: "Crypto Tech"},
        {id: 2, name: "Daily Technologies"},
        {id: 3, name: "Food TECH"},
        {id: 4, name: "Медицина и фармацевтика"},
        {id: 5, name: "Нефтегазовая отрасль"},
        {id: 6, name: "Оптимизация производств"},
      ],
    };
  }
}
</script>

<style scoped>
.wrapper {
  background-color: #42b983;
  padding: 50px 0;
}
</style>
