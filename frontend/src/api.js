  // src/api.js
  import axios from "axios";

  const API = axios.create({
    baseURL: "http://127.0.0.1:5000", // tu Flask
  });

  // Agrega el token a cada request si existe
  API.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");  
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });

  export const login = (username, password) =>
    API.post("/usuarios/login", { username, password });

  export const getPacientes = () => API.get("/pacientes/");
  export const createPaciente = (data) => API.post("/pacientes/", data);
  export const getPaciente = (id) => API.get(`/pacientes/${id}`);
  export const updatePaciente = (id, data) => API.put(`/pacientes/${id}`, data);
  export const deletePaciente = (id) => API.delete(`/pacientes/${id}`);

  export default API;
