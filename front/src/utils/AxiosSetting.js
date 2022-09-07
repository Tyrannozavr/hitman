import axios from "axios";
import router from "@/router";

export default () => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';
  options.timeout = 1000;
  if (sessionStorage.getItem('token')) {
    options.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`}
  } else {
      router.push({name: 'index'})
  }

  const axiosInstance = axios.create(options);

  axiosInstance.interceptors.response.use(
      function(response) {
        return response
      },
      function (error) {
          if (error.response.status === 401) {
              alert('you need to re-login');
              sessionStorage.removeItem('token')
              window.location = './'
          }
        // console.log('error', error.message);
      return Promise.reject(error)
      }
  )
    return axiosInstance
};