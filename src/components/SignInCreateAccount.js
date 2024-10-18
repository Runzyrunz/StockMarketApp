// src/components/SignInCreateAccount.js
import React, { useState } from 'react';

const SignInCreateAccount = () => {
  const [isSigningIn, setIsSigningIn] = useState(true); // State to toggle between Sign In and Create Account

  // Form fields
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  // Handle Sign In form submission
  const handleSignIn = (e) => {
    e.preventDefault();
    // Add your sign-in logic here
    console.log('Signing in with:', email, password);
  };

  // Handle Create Account form submission
  const handleCreateAccount = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords don't match!");
      return;
    }
    // Add your create account logic here
    console.log('Creating account with:', email, password);
  };

  return (
    <div style={styles.container}>
      <div style={styles.toggleContainer}>
        <button
          style={isSigningIn ? styles.activeToggle : styles.toggleButton}
          onClick={() => setIsSigningIn(true)}
        >
          Sign In
        </button>
        <button
          style={!isSigningIn ? styles.activeToggle : styles.toggleButton}
          onClick={() => setIsSigningIn(false)}
        >
          Create Account
        </button>
      </div>

      {isSigningIn ? (
        // Sign In Form
        <form onSubmit={handleSignIn} style={styles.form}>
          <h1>Sign In</h1>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={styles.input}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={styles.input}
          />
          <button type="submit" style={styles.button}>Sign In</button>
        </form>
      ) : (
        // Create Account Form
        <form onSubmit={handleCreateAccount} style={styles.form}>
          <h1>Create Account</h1>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={styles.input}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={styles.input}
          />
          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
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
    padding: '20px',
    textAlign: 'center',
  },
  toggleContainer: {
    display: 'flex',
    justifyContent: 'center',
    marginBottom: '20px',
  },
  toggleButton: {
    padding: '10px 20px',
    fontSize: '16px',
    border: '1px solid #ccc',
    cursor: 'pointer',
    backgroundColor: '#f0f0f0',
    margin: '0 5px',
  },
  activeToggle: {
    padding: '10px 20px',
    fontSize: '16px',
    border: '1px solid #4CAF50',
    cursor: 'pointer',
    backgroundColor: '#4CAF50',
    color: 'white',
    margin: '0 5px',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  input: {
    margin: '10px 0',
    padding: '10px',
    fontSize: '16px',
    border: '1px solid #ccc',
  },
  button: {
    padding: '10px',
    backgroundColor: '#4CAF50',
    color: '#fff',
    border: 'none',
    cursor: 'pointer',
  },
};

export default SignInCreateAccount;
