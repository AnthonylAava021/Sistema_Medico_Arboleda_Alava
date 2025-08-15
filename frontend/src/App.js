import React, { useState } from "react";
import { Routes, Route, Navigate, Link } from "react-router-dom";
import Login from "./Login";
import Pacientes from "./pages/Pacientes";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || null);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return (
    <div>
      {/* Navbar simple */} 
      <nav style={{ padding: 12, borderBottom: "1px solid #eee" }}>
        <Link to="/" style={{ marginRight: 12 }}>Inicio</Link>
        {token && <Link to="/pacientes" style={{ marginRight: 12 }}>Pacientes</Link>}
        {token ? (
          <button onClick={handleLogout}>Cerrar sesión</button>
        ) : (
          <Link to="/login">Iniciar sesión</Link>
        )}
      </nav>

      <Routes>
        <Route
          path="/"
          element={<Navigate to={token ? "/pacientes" : "/login"} replace />}
        />
        <Route path="/login" element={<Login onLogin={setToken} />} />
        <Route
          path="/pacientes"
          element={
            <ProtectedRoute token={token}>
              <Pacientes />
            </ProtectedRoute>
          }
        />
        <Route path="*" element={<div style={{ padding: 20 }}>404</div>} />
      </Routes>
    </div>
  );
}

export default App;
