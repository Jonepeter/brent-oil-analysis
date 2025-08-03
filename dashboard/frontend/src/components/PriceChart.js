import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';
import { Typography, Box } from '@mui/material';

const PriceChart = ({ data, events, changepoints }) => {
  if (!data) return <Typography>No data available</Typography>;

  const chartData = data.dates.map((date, index) => ({
    date,
    price: data.prices[index],
    returns: data.returns[index]
  }));

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        Brent Oil Price with Change Points
      </Typography>
      
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            tick={{ fontSize: 12 }}
            interval="preserveStartEnd"
          />
          <YAxis />
          <Tooltip 
            labelFormatter={(value) => `Date: ${value}`}
            formatter={(value, name) => [
              name === 'price' ? `$${value.toFixed(2)}` : value.toFixed(4),
              name === 'price' ? 'Price (USD/barrel)' : 'Log Returns'
            ]}
          />
          <Legend />
          <Line 
            type="monotone" 
            dataKey="price" 
            stroke="#1976d2" 
            strokeWidth={2}
            dot={false}
            name="Price"
          />
          
          {changepoints && changepoints.map((cp, index) => (
            <ReferenceLine 
              key={index}
              x={cp.date} 
              stroke="red" 
              strokeDasharray="5 5"
              label={{ value: "Change Point", position: "top" }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>

      <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
        Log Returns
      </Typography>
      
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            tick={{ fontSize: 12 }}
            interval="preserveStartEnd"
          />
          <YAxis />
          <Tooltip 
            labelFormatter={(value) => `Date: ${value}`}
            formatter={(value) => [value.toFixed(4), 'Log Returns']}
          />
          <Line 
            type="monotone" 
            dataKey="returns" 
            stroke="#dc004e" 
            strokeWidth={1}
            dot={false}
            name="Returns"
          />
          
          {changepoints && changepoints.map((cp, index) => (
            <ReferenceLine 
              key={index}
              x={cp.date} 
              stroke="red" 
              strokeDasharray="5 5"
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default PriceChart;