import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    common: {'Content-Type': 'application/json' },
  },
});

api.interceptors.response.use(
  (response) => {
    response.ok = true;
    return response;
  },
  (error) => {
    return Promise.reject(error);
  },
);

export default api;
