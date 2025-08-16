import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000", // Flask backend
});

// Agrega el token a cada request si existe
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// ======================
//  AUTH
// ======================
export const login = (username, password) =>
  API.post("/usuarios/login", { username, password });

// ======================
//  PACIENTES
// ======================
export const getPacientes = () => API.get("/pacientes");
export const createPaciente = (data) => API.post("/pacientes", data);
export const getPaciente = (id) => API.get(`/pacientes/${id}`);
export const updatePaciente = (id, data) => API.put(`/pacientes/${id}`, data);
export const deletePaciente = (id) => API.delete(`/pacientes/${id}`);

// ======================
//  DOCTORES
// ======================
export const getDoctores = () => API.get("/doctores");
export const createDoctor = (data) => API.post("/doctores", data);
export const getDoctor = (id) => API.get(`/doctores/${id}`);
export const updateDoctor = (id, data) => API.put(`/doctores/${id}`, data);
export const deleteDoctor = (id) => API.delete(`/doctores/${id}`);

export default API;
