import React, { useState } from "react";
import axios from "axios";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/usuarios/login", {
        username,
        password,
      });
      const token = response.data.access_token;
      localStorage.setItem("token", token);
      setMessage("Login exitoso");
      onLogin(token); // Mandamos token a App.js
    } catch (error) {
      console.error(error);
      setMessage("Usuario o contraseña incorrectos");
    }
  };

  return (
    <div style={{ maxWidth: "300px", margin: "auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Usuario:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Contraseña:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Ingresar</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Login;
