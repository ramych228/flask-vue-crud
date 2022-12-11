<template>
  <div class="wrapper">
    <button>{{text}}</button>
  </div>
</template>

<script>
export default {
  name: "ButtonAbout",

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
    if (this.type === "primary") {
      this.$el.children[0].classList.add("pulse-ring");
      this.$el.children[1].classList.add("pulse-button");
    } else {
      this.$el.children[0].style.display = "none";
    }
  }
}


</script>

<style scoped>
.wrapper {
}

button {
  width: 90%;
  height: 90%;
  position: absolute;
  background-color: #42b983;
  color: #ffffffff;
  font-size: 1em;
  font-family: "Comic Sans MS", cursive, sans-serif;
  border: none;
  cursor: pointer;
  border-radius: 32px;
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
}

.pulse-ring {
  animation: pulse 4s -2s infinite ease-in-out;
}

.pulse-button {
  animation: pulse 4s infinite ease-in-out;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.95);
  }
  100% {
    transform: scale(1);
  }
}
</style>
