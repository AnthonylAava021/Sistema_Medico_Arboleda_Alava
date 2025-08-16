// src/App.jsx
import React, { useState } from "react";
import { Routes, Route, Navigate, Link } from "react-router-dom";
import Login from "./Login";
import Pacientes from "./pages/Pacientes";
import Doctores from "./pages/Doctores";
import Citas from "./pages/Citas";   // 👈 importamos la vista de citas
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || null);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return (
    <div>
      {/* Navbar */}
      <nav style={{ padding: 12, borderBottom: "1px solid #eee" }}>
        <Link to="/" style={{ marginRight: 12 }}>Inicio</Link>
        {token && <Link to="/pacientes" style={{ marginRight: 12 }}>Pacientes</Link>}
        {token && <Link to="/doctores" style={{ marginRight: 12 }}>Doctores</Link>}
        {token && <Link to="/citas" style={{ marginRight: 12 }}>Citas</Link>} {/* 👈 nuevo link */}
        {token ? (
          <button onClick={handleLogout}>Cerrar sesión</button>
        ) : (
          <Link to="/login">Iniciar sesión</Link>
        )}
      </nav>

      {/* Rutas */}
      <Routes>
        <Route
          path="/"
          element={<Navigate to={token ? "/pacientes" : "/login"} replace />}
        />
        <Route path="/login" element={<Login onLogin={setToken} />} />

        {/* Pacientes */}
        <Route
          path="/pacientes"
          element={
            <ProtectedRoute token={token}>
              <Pacientes />
            </ProtectedRoute>
          }
        />

        {/* Doctores */}
        <Route
          path="/doctores"
          element={
            <ProtectedRoute token={token}>
              <Doctores />
            </ProtectedRoute>
          }
        />

        {/* Citas */}
        <Route
          path="/citas"
          element={
            <ProtectedRoute token={token}>
              <Citas />
            </ProtectedRoute>
          }
        />

        <Route path="*" element={<div style={{ padding: 20 }}>404</div>} />
      </Routes>
    </div>
  );
}

export default App;
