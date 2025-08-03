import React, { useState, useEffect } from 'react';
import { Container, Typography, Grid, Paper, Box } from '@mui/material';
import PriceChart from './components/PriceChart';
import EventsList from './components/EventsList';
import AnalysisSummary from './components/AnalysisSummary';
import axios from 'axios';

function App() {
  const [priceData, setPriceData] = useState(null);
  const [events, setEvents] = useState([]);
  const [changepoints, setChangepoints] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [priceRes, eventsRes, changepointsRes, summaryRes] = await Promise.all([
          axios.get('/api/price-data'),
          axios.get('/api/events'),
          axios.get('/api/changepoints'),
          axios.get('/api/analysis-summary')
        ]);

        setPriceData(priceRes.data);
        setEvents(eventsRes.data.events);
        setChangepoints(changepointsRes.data.changepoints);
        setSummary(summaryRes.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <Container>
        <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
          <Typography variant="h6">Loading...</Typography>
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Typography variant="h3" component="h1" gutterBottom align="center">
        Brent Oil Price Change Point Analysis
      </Typography>
      
      <Typography variant="subtitle1" align="center" color="text.secondary" paragraph>
        Detecting structural breaks and associating causes in oil price movements
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper sx={{ p: 2 }}>
            <AnalysisSummary summary={summary} />
          </Paper>
        </Grid>

        <Grid item xs={12} lg={8}>
          <Paper sx={{ p: 2 }}>
            <PriceChart 
              data={priceData} 
              events={events} 
              changepoints={changepoints} 
            />
          </Paper>
        </Grid>

        <Grid item xs={12} lg={4}>
          <Paper sx={{ p: 2 }}>
            <EventsList events={events} />
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;