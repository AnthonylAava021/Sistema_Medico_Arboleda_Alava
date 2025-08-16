import React, { useEffect, useState } from "react";
import { getDoctores, createDoctor, deleteDoctor, updateDoctor } from "../api";

function Doctores() {
  const [doctores, setDoctores] = useState([]);
  const [form, setForm] = useState({
    nombre: "",
    cedula: "",
    genero: "",
    especialidad: "",
    telefono: "",
    cargo: "",
  });

  // cargar doctores al iniciar
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
        // si hay id en el form → estamos editando
        await updateDoctor(form.id, form);
      } else {
        await createDoctor(form);
      }

      // resetear form
      setForm({
        nombre: "",
        cedula: "",
        genero: "",
        especialidad: "",
        telefono: "",
        cargo: "",
      });

      fetchDoctores(); // recargar lista
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
    <div style={{ padding: 20 }}>
      <h2>Gestión de Doctores</h2>

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
          placeholder="Género"
          name="genero"
          value={form.genero}
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
          placeholder="Cargo"
          name="cargo"
          value={form.cargo}
          onChange={handleChange}
          required
        />

        <button type="submit">
          {form.id ? "Actualizar Doctor" : "Agregar Doctor"}
        </button>
      </form>

      {/* Lista de doctores */}
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Cédula</th>
            <th>Género</th>
            <th>Especialidad</th>
            <th>Teléfono</th>
            <th>Cargo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {doctores.map((d) => (
            <tr key={d.id}>
              <td>{d.nombre}</td>
              <td>{d.cedula}</td>
              <td>{d.genero}</td>
              <td>{d.especialidad}</td>
              <td>{d.telefono}</td>
              <td>{d.cargo}</td>
              <td>
                <button onClick={() => handleEdit(d)}>Editar</button>
                <button onClick={() => handleDelete(d.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Doctores;
