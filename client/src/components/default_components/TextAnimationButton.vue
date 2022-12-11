<template>
<div class="button">
    <div class="typewriter">
        <h1>Отправить резюме</h1>
    </div>
</div>
</template>

<script>
export default {
  name: "TextAnimationButton",

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
.button {

}

.typewriter {
    display: inline-block;
}

.typewriter h1 {
  font-family: 'Montserrat', sans-serif;
  color:white;
  font-size: 0.5em;
  overflow: hidden;
  border-right: .15em solid white;
  white-space: nowrap;
  margin: 0 auto;
  letter-spacing: .15em;
  animation: 
    typing 1.5s steps(20, end),
    blink-caret .75s step-end infinite;
}

/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: white; }
}

</style>

