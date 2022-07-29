import "./index.css"

var app = new Vue({
    el: '#app',
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
                // window.location = '../../templates/authentication/fight.html';
              })
              .catch(function (error) {
                  alert('Неверные имя пользователя или пароль');
                console.log(error);
              });
        }
    }
})