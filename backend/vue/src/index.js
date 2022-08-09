// import './index.css'
// import './fight'
// import './statistic'
require('./index.css')
require('./fight')
require('./statistic')

var app = new Vue({
    el: '#app_login',
    data: () => ({
        message: 'Message',
        username: '',
        password: '',
    }),
    methods: {
        login () {
            axios.post('http://127.0.0.1:8000/api/users/login/', {
                user: {
                    username: this.username,
                    password: this.password,
                }
              })
              .then(function (response) {
                localStorage.setItem('token', response.data.user.token);
                sessionStorage.setItem('token', response.data.user.token);
                window.location = './fight.html';
              })
              .catch(function (error) {
                  alert('Неверные имя пользователя или пароль');
                console.log(error);
              });
        }
    }
})