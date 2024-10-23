// src/components/StockMarket.js
import React, { useState } from 'react';

const StockMarket = () => {
  const [stocks, setStocks] = useState([
    { name: 'AAPL', price: 150, change: '+2.3%' },
    { name: 'TSLA', price: 720, change: '+1.8%' },
    { name: 'AMZN', price: 3300, change: '+0.5%' },
  ]);

  return (
    <div style={styles.container}>
      <h1>Stock Market</h1>
      <div style={styles.stockList}>
        {stocks.map((stock, index) => (
          <div key={index} style={styles.stockItem}>
            <h3>{stock.name}</h3>
            <p>Price: ${stock.price}</p>
            <p>Change: {stock.change}</p>
            <button style={styles.buySellButton}>Buy</button>
            <button style={styles.buySellButton}>Sell</button>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: { padding: '20px' },
  stockList: { display: 'flex', justifyContent: 'space-around' },
  stockItem: { border: '1px solid #ddd', padding: '20px', width: '200px', textAlign: 'center' },
  buySellButton: { padding: '10px', margin: '5px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer' },
};

export default StockMarket;
