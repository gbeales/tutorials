<template>
  <div class="container">
    <div class="columns">
      <div class="column">
        <div class="message" :v-for="status in statuses">
          <div class="message-header">
            Joe said ...
            <p>{{ status.user.name }} said ...</p>
            <p>A moment ago ...</p>
          </div>
          <div class="message-body" v-text="status.body"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      status: []
    };
  },

  created() {
    window.axios.get("/statuses").then(({ data }) => (this.statuses = data));
  }
};
</script>
