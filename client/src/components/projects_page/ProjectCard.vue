<template>
  <div class="container">
    <div class="header">
      <h3 class="text_name">{{project.name}}</h3>
      <p class="arrow">⟩</p>
    </div>
    <p class="text_brief">{{project.brief}}</p>
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
