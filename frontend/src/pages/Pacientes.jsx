// src/pages/Pacientes.jsx
import { useEffect, useState } from "react";
import { getPacientes } from "../api";

export default function Pacientes() {
  const [pacientes, setPacientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    getPacientes()
      .then((res) => setPacientes(res.data))
      .catch((err) => setError("No se pudieron cargar los pacientes"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Cargando pacientes...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div style={{ padding: 20 }}>
      <h1>Pacientes</h1>
      {Array.isArray(pacientes) && pacientes.length > 0 ? (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
            </tr>
          </thead>
          <tbody>
            {pacientes.map((p) => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.nombre || p.name || p.fullname || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <pre style={{ background: "#f5f5f5", padding: 16 }}>
          {JSON.stringify(pacientes, null, 2)}
        </pre>
      )}
    </div>
  );
}
