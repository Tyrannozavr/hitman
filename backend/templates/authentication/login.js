var app = new Vue({
    el: '#app',
    data: () => ({
        message: 'Message',
        username: '',
        password: '',
    }),
    methods: {
        login () {
            console.log(this.username, this.password);
            axios.post('http://127.0.0.1:8000/api/users/login/', {
                user: {
                    username: 'dmiv',
                    password: 123456
                }
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
})
// axios.post('http://127.0.0.1:8000/api/users/login/', {
//     user: {
//         username: 'dmiv',
//         password: 123456
//     }
//   })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   });