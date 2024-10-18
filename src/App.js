// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import StockMarket from './components/StockMarket';
import Portfolio from './components/Portfolio';
import Chatbot from './components/Chatbot';
import SignInCreateAccount from './components/SignInCreateAccount';

function App() {
  return (
    <Router>
      <div style={styles.container}>
        <nav style={styles.navbar}>
          <NavLink to="/" exact style={styles.navLink} activeStyle={styles.activeNavLink}>Dashboard</NavLink>
          <NavLink to="/market" style={styles.navLink} activeStyle={styles.activeNavLink}>Stock Market</NavLink>
          <NavLink to="/portfolio" style={styles.navLink} activeStyle={styles.activeNavLink}>Portfolio</NavLink>
          <NavLink to="/chatbot" style={styles.navLink} activeStyle={styles.activeNavLink}>Chatbot</NavLink>
          <NavLink to="/signin-create-account" style={styles.navLink} activeStyle={styles.activeNavLink}>Sign In / Create Account</NavLink>
        </nav>

        <div style={styles.content}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/market" element={<StockMarket />} />
            <Route path="/portfolio" element={<Portfolio />} />
            <Route path="/chatbot" element={<Chatbot />} />
            <Route path="/signin-create-account" element={<SignInCreateAccount />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

const styles = {
  container: { fontFamily: 'Arial, sans-serif' },
  navbar: {
    backgroundColor: '#333',
    padding: '10px',
    display: 'flex',
    justifyContent: 'space-around',
  },
  navLink: {
    color: '#fff',
    textDecoration: 'none',
    padding: '10px',
    fontSize: '18px',
  },
  activeNavLink: {
    borderBottom: '2px solid #fff',
  },
  content: {
    padding: '20px',
  },
};

export default App;
