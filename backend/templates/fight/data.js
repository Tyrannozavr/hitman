var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello, Vue'
    }
})
// console.log('Hello');
// console.log('Hello');
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
