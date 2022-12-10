<template>
  <div class="container">
    <StudentCard v-for="student in students" :student="student" :key="student.id"/>
  </div>
</template>

<script>
import StudentCard from "./StudentCard";
export default {
  name: "StudentsTable",
  components: { StudentCard },
  props: {
    students: {
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
}
</style>
