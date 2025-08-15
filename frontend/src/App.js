import React, { useState, useEffect } from "react";
import axios from "axios";
import Login from "./Login";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || null);
  const [data, setData] = useState(null);

  // Cada vez que haya token, pedimos pacientes
  useEffect(() => {
    if (token) {
      axios.get("http://127.0.0.1:5000/pacientes", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => setData(response.data))
      .catch((error) => {
        console.error(error);
        if (error.response && error.response.status === 401) {
          // Si el token no es válido, lo borramos
          localStorage.removeItem("token");
          setToken(null);
        }
      });
    }
  }, [token]);

  // Función para cerrar sesión
  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setData(null);
  };

  return (
    <div style={{ padding: "20px" }}>
      {!token ? (
        <Login onLogin={setToken} />
      ) : (
        <div>
          <h1>Pacientes</h1>
          {data ? (
            <pre>{JSON.stringify(data, null, 2)}</pre>
          ) : (
            <p>Cargando pacientes...</p>
          )}
          <button onClick={handleLogout}>Cerrar sesión</button>
        </div>
      )}
    </div>
  );
}

export default App;
