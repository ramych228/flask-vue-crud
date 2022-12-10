<template>
  <div class="wrapper">
    <div v-if="type === 'primary'" class="ring"></div>
    <button class="color" :col="color">{{ text }}</button>
  </div>
</template>

<script>
export default {
  name: "PrimeButton",

  props: {
    text: {
      type: String,
      default: "Button"
    },
    color: {
      type: String,
      default: "#7B45EC"
    },
    type: {
      type: String,
      default: "primary"
    }
  },

  mounted() {
    this.$el.children[0].style.borderColor = this.color;
    this.$el.children[1].style.backgroundColor = this.color;
  }
}


</script>

<style scoped>
.wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
  width: 400px;
}

button {
  width: 90%;
  height: 90%;
  position: absolute;
  background-color: #42b983;
  color: #ffffffff;
  font-size: 40px;
  font-family: "Comic Sans MS", cursive, sans-serif;
  border: none;
  cursor: pointer;
  border-radius: 32px;

  animation: pulse 4s infinite ease-in-out;
}

.ring {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background-color: #42b98300;
  border-radius: 32px;
  border-color: #2c3e50;
  border-width: 2px;
  border-style: solid;
  animation: pulse 4s -2s infinite ease-in-out;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.9);
  }
  100% {
    transform: scale(1);
  }
}
</style>
