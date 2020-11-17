<template>
  <div id="app" class="container">
      <form method="POST" action="/projects">

      <div class="control">

        <label for="name" class="label">Project Name:</label>

        <input type="text" id="name" name="name" class="input" v-mode="name">

      </div>

      <div class="control">
        <label for="description" class="label">Project Description:</label>

        <input type="text" id="description" name="description" class="input" v-model="description">

      </div>

      <div class="control">
        <button class="button is-primary">Create</button>
      </div>

    </form>
  </div>
</template>

<script>


export default {
  name: "App",
  components: {

  },

  data: function() {
    return {
      name: '',
      description: ''
    }

  },

  methods: {

  }
};
</script>

<style>
</style>
