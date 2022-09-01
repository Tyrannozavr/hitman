import axios from "axios";

export default ({requiresAuth = false} = {}) => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';
  options.timeout = 1000;
  if (requiresAuth && sessionStorage.getItem('token')) {
    options.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`}
      // console.log('no token')
  }

  const instance = axios.create(options);

  instance.interceptors.response.use(
      function(response) {
        return response
      },
      function (error) {
          // console.log('error: ', error.response.status)
          if (error.response.status === 401) {
              alert('you need to re-login');
              sessionStorage.removeItem('token')
              // console.log('you need re-login', error.response.status)
              window.location = './'
          }
        // console.log('error', error.message);
      return Promise.reject(error)
      }
  )
    return instance
};