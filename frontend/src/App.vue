<template>
  <div id="app">
    <render-file></render-file>
  </div>
</template>

<script>
import RenderFile from "./components/RenderFile.vue";

export default {
  name: "App",
  components: {
    RenderFile,
  },
};
</script>
