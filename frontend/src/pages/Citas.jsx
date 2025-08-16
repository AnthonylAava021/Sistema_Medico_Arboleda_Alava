// src/pages/Citas.jsx
import React, { useEffect, useState } from "react";
import { getCitas, createCita, deleteCita, updateCita } from "../api";
import "./Citas.css";

function Citas() {
  const [citas, setCitas] = useState([]);
  const [form, setForm] = useState({
    paciente_id: "",
    doctor_id: "",
    fecha: "",
    hora: "",
    motivo: "",
  });

  useEffect(() => {
    fetchCitas();
  }, []);

  const fetchCitas = async () => {
    try {
      const res = await getCitas();
      setCitas(res.data);
    } catch (err) {
      console.error("Error cargando citas", err);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (form.id) {
        await updateCita(form.id, form);
      } else {
        await createCita(form);
      }

      setForm({
        paciente_id: "",
        doctor_id: "",
        fecha: "",
        hora: "",
        motivo: "",
      });

      fetchCitas();
    } catch (err) {
      console.error("Error guardando cita", err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Seguro que deseas eliminar esta cita?")) {
      try {
        await deleteCita(id);
        fetchCitas();
      } catch (err) {
        console.error("Error eliminando cita", err);
      }
    }
  };

  const handleEdit = (cita) => {
    setForm(cita);
  };

  return (
    <div className="citas-container">
      <h2>📅 Gestión de Citas</h2>

      {/* Formulario */}
      <form className="cita-form" onSubmit={handleSubmit}>
        <input
          placeholder="ID Paciente"
          name="paciente_id"
          value={form.paciente_id}
          onChange={handleChange}
          required
        />
        <input
          placeholder="ID Doctor"
          name="doctor_id"
          value={form.doctor_id}
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="fecha"
          value={form.fecha}
          onChange={handleChange}
          required
        />
        <input
          type="time"
          name="hora"
          value={form.hora}
          onChange={handleChange}
          required
        />
        <input
          placeholder="Motivo"
          name="motivo"
          value={form.motivo}
          onChange={handleChange}
        />

        <button type="submit" className="btn-primary">
          {form.id ? "💾 Guardar Cambios" : "➕ Agregar Cita"}
        </button>
      </form>

      {/* Tabla */}
      <table className="cita-table">
        <thead>
          <tr>
            <th>Paciente</th>
            <th>Doctor</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Motivo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {citas.map((c, i) => (
            <tr key={i}>
              <td>{c.paciente_id}</td>
              <td>{c.doctor_id}</td>
              <td>{c.fecha}</td>
              <td>{c.hora}</td>
              <td>{c.motivo}</td>
              <td>
                <button className="btn-edit" onClick={() => handleEdit(c)}>
                  ✏️ Editar
                </button>
                <button className="btn-delete" onClick={() => handleDelete(c.id)}>
                  🗑 Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Citas;
