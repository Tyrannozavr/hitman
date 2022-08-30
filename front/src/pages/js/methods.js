import axios from "axios";

export default () => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';
  options.timeout = 1000;

  const instance = axios.create(options);
  instance.interceptors.response.use(
      function(response) {
        return response
      },
      function(error) {
    if (error.response && error.response.data && error.response.data.detail === "Authentication credentials were not provided.") {
      let data = {method: error.config.method, url: error.config.url,
        headers: {'Authorization': `Token ${sessionStorage.getItem('token')}`}}
      if (error.config.data) {
        data.data = JSON.parse(error.config.data)
      }
      return instance(data)
    }
    return Promise.reject(error);
  })
  return instance;
};