// src/pages/Citas.jsx
import React, { useEffect, useState } from "react";
import { getCitas, createCita, deleteCita, updateCita } from "../api";

function Citas() {
  const [citas, setCitas] = useState([]);
  const [form, setForm] = useState({
    fecha: "",
    hora: "",
    motivo: "",
    paciente_id: "",
    doctor_id: "",
  });

  // Cargar citas al iniciar
  useEffect(() => {
    fetchCitas();
  }, []);

  const fetchCitas = async () => {
    try {
      const res = await getCitas();
      setCitas(res.data);
    } catch (err) {
      console.error("❌ Error cargando citas", err);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createCita(form);
      setForm({
        fecha: "",
        hora: "",
        motivo: "",
        paciente_id: "",
        doctor_id: "",
      });
      fetchCitas(); // recargar lista
    } catch (err) {
      console.error("❌ Error creando cita", err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Seguro que deseas eliminar esta cita?")) {
      try {
        await deleteCita(id);
        fetchCitas();
      } catch (err) {
        console.error("❌ Error eliminando cita", err);
      }
    }
  };

  const handleEdit = (cita) => {
    setForm(cita);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Gestión de Citas</h2>

      {/* Formulario */}
      <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
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
        <button type="submit">Agregar Cita</button>
      </form>

      {/* Lista de citas */}
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Motivo</th>
            <th>Paciente ID</th>
            <th>Doctor ID</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {citas.map((c, i) => (
            <tr key={i}>
              <td>{c.fecha}</td>
              <td>{c.hora}</td>
              <td>{c.motivo}</td>
              <td>{c.paciente_id}</td>
              <td>{c.doctor_id}</td>
              <td>
                <button onClick={() => handleEdit(c)}>Editar</button>
                <button onClick={() => handleDelete(c.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Citas;
