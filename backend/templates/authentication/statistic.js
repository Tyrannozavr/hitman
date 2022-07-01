axios.get('http://127.0.0.1:8000/fight/statistic/', {

  })
  .then(function (response) {
      console.log(response);
      var app = new Vue({
          el: '#app',
          data: {
              rounds: response.data
          }
      })
  })
  .catch(function (error) {
      alert('Неверные имя пользователя или пароль');
    console.log(error);
  });