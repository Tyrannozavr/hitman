// myStorage = window.localStorage;
var app = new Vue({
    el: '#app',
    data: () => ({
        message: 'Message',
        username: '',
        password: '',
    }),
    methods: {
        login () {
            // console.log(this.username, this.password);
            axios.post('http://127.0.0.1:8000/api/users/login/', {
                user: {
                    username: this.username,
                    password: this.password,
                }
              })
              .then(function (response) {
                // console.log(response.data.user.token);
                localStorage.setItem('token', response.data.user.token);
                sessionStorage.setItem('token', response.data.user.token);
                // myStorage.setItem('dmiv', 'dmiv');
                window.location = 'fight.html';
                // this.cookie.set('name', 'dmiv');
                // window.location = 'file:///home/dmiv/PycharmProjects/hitman/backend/templates/fight/fight.html';
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
})