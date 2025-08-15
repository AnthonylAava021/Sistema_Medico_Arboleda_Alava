import React, { useState } from "react";
import { login as loginRequest } from "./api";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const { data } = await loginRequest(username, password);
      const token = data.access_token;
      localStorage.setItem("token", token);
      setMessage("Login exitoso");
      onLogin(token);
    } catch (error) {
      console.error(error);
      setMessage("Usuario o contraseña incorrectos");
    }
  };

  return (
    <div style={{ maxWidth: 320, margin: "40px auto" }}>
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
