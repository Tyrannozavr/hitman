<template>
  <div class="container-fluid">
    <div class="col-md-4 offset-md-4">
      <div class="form-container">
        <div class="form-icon"><i class="fa fa-user"></i></div>
        <h3 class="title">Login</h3>
        <form class="form-horizontal" @submit.prevent="login" action="http://localhost:8080/fight/">
          <div class="form-group">
            <label>Login</label>
            <input class="form-control" placeholder="username" type="text" v-model="username">
            <label>Password</label>
            <input class="form-control" placeholder="password" type="password" v-model="password">
          </div>
          <button class="btn btn-default" type="submit">login</button>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axiosInstance from "@/utils/AxiosSetting";

export default {
  data: function () {
    return {
      message: 'Message',
      username: '',
      password: '',
    }
  },
  methods: {
    async login() {
      const response = await axiosInstance().post('api/users/login/', {
        user: {
          username: this.username,
          password: this.password
        }
      })
      try {
        sessionStorage.setItem('token', response.data.user.token);
        this.$router.push({name: 'fight'})
      } catch (error) {
          alert('Неверные данные пользователя или пароль');
        console.log(error)
      }
    }
  }
}
</script>
<style>
.form-container {
  background: #ecf0f3;
  font-family: 'Nunito', sans-serif;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;
}

.form-container .form-icon {
  color: #ac40ab;
  font-size: 55px;
  text-align: center;
  line-height: 100px;
  width: 100px;
  height: 100px;
  margin: 0 auto 15px;
  border-radius: 50px;
  box-shadow: 7px 7px 10px #cbced1, -7px -7px 10px #fff;
}

.form-container .title {
  color: #ac40ab;
  font-size: 25px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: center;
  margin: 0 0 20px;
}

.form-container .form-horizontal .form-group {
  margin: 0 0 25px 0;
}

.form-container .form-horizontal .form-group label {
  font-size: 15px;
  font-weight: 600;
  text-transform: uppercase;
}

.form-container .form-horizontal .form-control {
  color: #333;
  background: #ecf0f3;
  font-size: 15px;
  height: 50px;
  padding: 20px;
  letter-spacing: 1px;
  border: none;
  border-radius: 50px;
  box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px #fff;
  display: inline-block;
  transition: all 0.3s ease 0s;
}

.form-container .form-horizontal .form-control:focus {
  box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px #fff;
  outline: none;
}

.form-container .form-horizontal .form-control::placeholder {
  color: #808080;
  font-size: 14px;
}

.form-container .form-horizontal .btn {
  color: #000;
  background-color: #ac40ab;
  font-size: 15px;
  font-weight: bold;
  text-transform: uppercase;
  width: 100%;
  padding: 12px 15px 11px;
  border-radius: 20px;
  box-shadow: 6px 6px 6px #383b42, -6px -6px 6px #fff;
  border: none;
  transition: all 0.5s ease 0s;
}

.form-container .form-horizontal .btn:hover,
.form-container .form-horizontal .btn:focus {
  color: #fff;
  letter-spacing: 3px;
  box-shadow: none;
  outline: none;
}
</style>