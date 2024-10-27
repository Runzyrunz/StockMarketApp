import React, { useState } from 'react';
import axios from 'axios';

const SignInCreateAccount = () => {
  const [isSigningIn, setIsSigningIn] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSignIn = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/sign-in/', { email, password });
      alert(response.data.message || "Sign in successful");
    } catch (error) {
      alert(error.response?.data?.error || "Sign in failed. Please try again.");
    }
  };

  const handleCreateAccount = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords don't match!");
      return;
    }
    try {
      const response = await axios.post('http://localhost:8000/api/create-account/', { email, password });
      alert(response.data.message || "Account created successfully");
      setIsSigningIn(true);
    } catch (error) {
      alert(error.response?.data?.error || "Account creation failed. Please try again.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.toggleContainer}>
        <button
          style={isSigningIn ? { ...styles.toggleButton, ...styles.activeToggle } : styles.toggleButton}
          onClick={() => setIsSigningIn(true)}
        >
          Sign In
        </button>
        <button
          style={!isSigningIn ? { ...styles.toggleButton, ...styles.activeToggle } : styles.toggleButton}
          onClick={() => setIsSigningIn(false)}
        >
          Create Account
        </button>
      </div>

      {isSigningIn ? (
        <form onSubmit={handleSignIn} style={styles.form}>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            style={styles.input}
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            style={styles.input}
          />
          <button type="submit" style={styles.button}>Sign In</button>
        </form>
      ) : (
        <form onSubmit={handleCreateAccount} style={styles.form}>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            style={styles.input}
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            style={styles.input}
          />
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm Password"
            style={styles.input}
          />
          <button type="submit" style={styles.button}>Create Account</button>
        </form>
      )}
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '400px',
    margin: '0 auto',
    padding: '40px',
    textAlign: 'center',
    backgroundColor: '#f9f9f9',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    borderRadius: '8px',
  },
  toggleContainer: {
    display: 'flex',
    justifyContent: 'center',
    marginBottom: '20px',
  },
  toggleButton: {
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
    borderRadius: '5px',
    margin: '0 5px',
    color: '#333',
    backgroundColor: '#e0e0e0',
    border: 'none',
    outline: 'none',
  },
  activeToggle: {
    backgroundColor: '#4CAF50',
    color: '#fff',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  input: {
    margin: '10px 0',
    padding: '12px',
    fontSize: '16px',
    borderRadius: '5px',
    border: '1px solid #ccc',
  },
  button: {
    padding: '12px',
    backgroundColor: '#4CAF50',
    color: '#fff',
    border: 'none',
    cursor: 'pointer',
    borderRadius: '5px',
    fontSize: '16px',
    marginTop: '10px',
  },
};

export default SignInCreateAccount;
