import axios from "axios";

export default ({ requiresAuth = false } = {}) => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';
  options.timeout = 1000;

  //? Decide add token or not
  if (requiresAuth) {
    options.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`}
  }
  const instance = axios.create(options);
  // instance.interceptors.request.use(function (config) {
  //   // console.log('request', config.baseURL, config.url);
  //   // Do something before request is sent
  //   return config;
  // }, function (error) {
  //   // Do something with request error
  //   return Promise.reject(error);
  // });
  instance.interceptors.response.use(
      function(response) {
        console.log('response')
        return response
      },
      function(error) {
    // console.log('error interceptors');
    if (error.response.data.detail === "Authentication credentials were not provided.") {
      console.log('headers');
      let OrigRequest = error.config
      OrigRequest.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`}
      return instance(OrigRequest);

      // options.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`};
      // requiresAuth = true;
    }
    return Promise.reject(error);
  })
  return instance;
};
// axios.interceptors.response.use( function(error) {
//   console.log('error')
// })
// axios.interceptors.response.use(
//     function (response) {
//     // Any status code that lie within the range of 2xx cause this function to trigger
//     // Do something with response data
//     return response;
//   },
//     function (error) {
//       console.log('error in interception')
//     // Any status codes that falls outside the range of 2xx cause this function to trigger
//     // Do something with response error
//     return Promise.reject(error);
//   });