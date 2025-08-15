// src/pages/Pacientes.jsx
import React, { useEffect, useState } from "react";
import { getPacientes, createPaciente } from "../api";

function Pacientes() {
  const [pacientes, setPacientes] = useState([]);
  const [form, setForm] = useState({
    nombre: "",
    cedula: "",
    telefono: "",
    genero: "",
    direccion: "",
    historial_medico: "",
    fecha_nacimiento: "",
  });

  // Cargar pacientes al iniciar
  useEffect(() => {
    fetchPacientes();
  }, []);

  const fetchPacientes = async () => {
    try {
      const res = await getPacientes();
      setPacientes(res.data);
    } catch (err) {
      console.error("Error cargando pacientes", err);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createPaciente(form);
      setForm({
        nombre: "",
        cedula: "",
        telefono: "",
        genero: "",
        direccion: "",
        historial_medico: "",
        fecha_nacimiento: "",
      });
      fetchPacientes(); // recargar lista
    } catch (err) {
      console.error("Error creando paciente", err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Gestión de Pacientes</h2>

      {/* Formulario */}
      <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
        <input
          placeholder="Nombre"
          name="nombre"
          value={form.nombre}
          onChange={handleChange}
          required
        />
        <input
          placeholder="Cédula"
          name="cedula"
          value={form.cedula}
          onChange={handleChange}
          required
        />
        <input
          placeholder="Teléfono"
          name="telefono"
          value={form.telefono}
          onChange={handleChange}
        />
        <input
          placeholder="Género"
          name="genero"
          value={form.genero}
          onChange={handleChange}
          required
        />
        <input
          placeholder="Dirección"
          name="direccion"
          value={form.direccion}
          onChange={handleChange}
        />
        <input
          placeholder="Historial Médico"
          name="historial_medico"
          value={form.historial_medico}
          onChange={handleChange}
        />
        <input
          type="date"
          name="fecha_nacimiento"
          value={form.fecha_nacimiento}
          onChange={handleChange}
        />
        <button type="submit">Agregar Paciente</button>
      </form>

      {/* Lista de pacientes */}
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Cédula</th>
            <th>Teléfono</th>
            <th>Género</th>
          </tr>
        </thead>
        <tbody>
          {pacientes.map((p, i) => (
            <tr key={i}>
              <td>{p.nombre}</td>
              <td>{p.cedula}</td>
              <td>{p.telefono}</td>
              <td>{p.genero}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Pacientes;
