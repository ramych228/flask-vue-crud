<template>
  <div id="app">
    <PrimeButton text="Click" />
    <router-view/>
  </div>
</template>

<script>
import PrimeButton from "./components/default_components/PrimeButton";
export default {
  name: 'App',
  components: {PrimeButton},
};
</script>

<style>
#app {
  margin-top: 60px
}
</style>
