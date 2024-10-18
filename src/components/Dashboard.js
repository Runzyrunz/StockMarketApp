// src/components/Dashboard.js
import React from 'react';

const Dashboard = () => {
  return (
    <div style={styles.container}>
      <h1>StockSim Dashboard</h1>
      <div style={styles.section}>
        <h2>Your Portfolio</h2>
        <p>Portfolio Value: $10,000</p>
        <p>Total Gains: +$500</p>
      </div>
      
      <div style={styles.section}>
        <h2>Market Overview</h2>
        <p>Trending Stocks: AAPL, TSLA, AMZN</p>
      </div>

      <div style={styles.navigation}>
        <button style={styles.button}>Buy/Sell Stocks</button>
        <button style={styles.button}>Predictions</button>
        <button style={styles.button}>Learn</button>
      </div>
    </div>
  );
};

const styles = {
  container: { padding: '20px', textAlign: 'center' },
  section: { margin: '20px 0' },
  navigation: { display: 'flex', justifyContent: 'space-around' },
  button: { padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer' },
};

export default Dashboard;
