import axios from "axios";

// export var BASE_URL = 'http://127.0.0.1:8000/'
// export var headers =  {
//               Authorization: `Token ${sessionStorage.getItem('token')}`
//             }
// export var instance = axios.create({
//   baseURL: BASE_URL,
//   timeout: 1000,
//   headers: headers
// });

export default ({ requiresAuth = false } = {}) => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';

  //? Decide add token or not
  if (requiresAuth) {
    options.headers.Authorization = `Token ${sessionStorage.getItem('token')}`
  }
  const instance = axios.create(options);
  return instance;
};
