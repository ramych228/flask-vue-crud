<template>
  <div class="container">
    <div class="header">
      <h3>{{project.name}}</h3>
      <p>></p>
    </div>
    <p>{{project.brief}}</p>
  </div>
</template>

<script>
export default {
  name: "ProjectCard",
  props: {
    project: {
      type: Object,
      required: true
    }
  },

  mounted() {
    this.$el.style.backgroundImage = `url(${this.project.image_path})`;
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
</style>
