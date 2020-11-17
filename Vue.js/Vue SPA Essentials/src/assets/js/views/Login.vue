<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8 col-md-offset-2">
        <div class="panel panel-default">
          <div class="panel-heading">Login Page</div>

          <div class="panel-body">
            <div class="columns">
              <div class="column is-4">
                <form id="login-form">
                  <div class="field">
                    <label class="label">Username</label>
                    <div class="control has-icons-left has-icons-right">
                      <input class="input" type="text" placeholder="Username" />
                      <span class="icon is-small is-left">
                        <i class="fas fa-user"></i>
                      </span>
                    </div>
                    <div class="field">
                      <label class="label">Password</label>
                      <div class="control has-icons-left has-icons-right">
                        <input
                          class="input"
                          type="password"
                          placeholder="Password"
                        />
                        <span class="icon is-small is-left">
                          <i class="fas fa-user"></i>
                        </span>
                      </div>
                    </div>
                    <div class="field">
                      <button class="button" @click="submit">Login</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",

  methods: {
    submit() {
      fetch("http://localhost:5000/auth/login/");
    }
  }
};
</script>
