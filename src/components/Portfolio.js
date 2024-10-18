// src/components/Portfolio.js
import React, { useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

const Portfolio = () => {
  const [portfolio] = useState([
    { stock: 'AAPL', shares: 10, currentValue: 1500, gains: '+$200' },
    { stock: 'TSLA', shares: 5, currentValue: 3600, gains: '+$300' },
    { stock: 'AMZN', shares: 3, currentValue: 9900, gains: '+$400' },
  ]);

  const totalValue = portfolio.reduce((total, item) => total + item.currentValue, 0);

  // Mock data for the chart
  const performanceData = [
    { name: 'Week 1', value: 8000 },
    { name: 'Week 2', value: 8500 },
    { name: 'Week 3', value: 9500 },
    { name: 'Week 4', value: 11000 },
  ];

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Your Portfolio</h1>

      <div style={styles.portfolioSummary}>
        <h2 style={styles.subTitle}>Portfolio Value: ${totalValue}</h2>
      </div>

      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Stock</th>
            <th style={styles.th}>Shares</th>
            <th style={styles.th}>Current Value</th>
            <th style={styles.th}>Gains/Losses</th>
          </tr>
        </thead>
        <tbody>
          {portfolio.map((item, index) => (
            <tr key={index} style={styles.tr}>
              <td style={styles.td}>{item.stock}</td>
              <td style={styles.td}>{item.shares}</td>
              <td style={styles.td}>${item.currentValue}</td>
              <td style={styles.td}>{item.gains}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div style={styles.chartContainer}>
        <h3>Portfolio Performance Over Time</h3>
        <div style={styles.chartWrapper}>
          <LineChart width={600} height={300} data={performanceData}>
            <Line type="monotone" dataKey="value" stroke="#4CAF50" strokeWidth={2} />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
          </LineChart>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: { maxWidth: '900px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif', color: '#333' },
  title: { textAlign: 'center', marginBottom: '20px', fontSize: '32px', color: '#4CAF50' },
  portfolioSummary: { textAlign: 'center', marginBottom: '20px' },
  subTitle: { fontSize: '24px', fontWeight: 'bold' },
  table: { width: '100%', borderCollapse: 'collapse', marginBottom: '30px', boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)' },
  th: { backgroundColor: '#4CAF50', color: 'white', padding: '10px', fontSize: '18px', textAlign: 'left' },
  td: { padding: '15px', borderBottom: '1px solid #ddd', fontSize: '16px' },
  tr: { backgroundColor: '#f9f9f9' },
  chartContainer: {
    textAlign: 'center',
    padding: '20px',
    backgroundColor: '#f0f0f0',
    borderRadius: '8px',
  },
  chartWrapper: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
};

export default Portfolio;
