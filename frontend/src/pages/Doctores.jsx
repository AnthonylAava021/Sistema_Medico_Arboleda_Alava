// src/pages/Doctores.jsx
import React, { useEffect, useState } from "react";
import { getDoctores, createDoctor, deleteDoctor, updateDoctor } from "../api";
import "./Doctores.css";

function Doctores() {
  const [doctores, setDoctores] = useState([]);
  const [form, setForm] = useState({
    nombre: "",
    especialidad: "",
    telefono: "",
    email: "",
  });

  useEffect(() => {
    fetchDoctores();
  }, []);

  const fetchDoctores = async () => {
    try {
      const res = await getDoctores();
      setDoctores(res.data);
    } catch (err) {
      console.error("Error cargando doctores", err);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (form.id) {
        await updateDoctor(form.id, form);
      } else {
        await createDoctor(form);
      }

      setForm({
        nombre: "",
        especialidad: "",
        telefono: "",
        email: "",
      });

      fetchDoctores();
    } catch (err) {
      console.error("Error guardando doctor", err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Seguro que deseas eliminar este doctor?")) {
      try {
        await deleteDoctor(id);
        fetchDoctores();
      } catch (err) {
        console.error("Error eliminando doctor", err);
      }
    }
  };

  const handleEdit = (doctor) => {
    setForm(doctor);
  };

  return (
    <div className="doctores-container">
      <h2>Gestión de Doctores</h2>

      {/* Formulario */}
      <form className="doctor-form" onSubmit={handleSubmit}>
        <input
          placeholder="Nombre"
          name="nombre"
          value={form.nombre}
          onChange={handleChange}
          required
        />
        <input
          placeholder="Especialidad"
          name="especialidad"
          value={form.especialidad}
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
          placeholder="Email"
          type="email"
          name="email"
          value={form.email}
          onChange={handleChange}
        />

        <button type="submit" className="btn-primary">
          {form.id ? " Guardar Cambios" : " Agregar Doctor"}
        </button>
      </form>

      {/* Tabla */}
      <table className="doctor-table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Especialidad</th>
            <th>Teléfono</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {doctores.map((d, i) => (
            <tr key={i}>
              <td>{d.nombre}</td>
              <td>{d.especialidad}</td>
              <td>{d.telefono}</td>
              <td>{d.email}</td>
              <td>
                <button className="btn-edit" onClick={() => handleEdit(d)}>
                   Editar
                </button>
                <button className="btn-delete" onClick={() => handleDelete(d.id)}>
                   Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Doctores;
