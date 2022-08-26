import axios from "axios";

export default ({ requiresAuth = false } = {}) => {
  const options = {};
  options.baseURL = 'http://127.0.0.1:8000/';
  options.timeout = 1000;

  //? Decide add token or not
  if (requiresAuth) {
    options.headers = {'Authorization': `Token ${sessionStorage.getItem('token')}`}
    // options.headers.Authorization = `Token ${sessionStorage.getItem('token')}`
  }
  const instance = axios.create(options);
  return instance;
};
