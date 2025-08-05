import React from 'react';
import { Grid, Card, CardContent, Typography, Box } from '@mui/material';
import { TrendingUp, Timeline, Event, Analytics } from '@mui/icons-material';

const AnalysisSummary = ({ summary }) => {
  if (!summary) return null;

  const summaryCards = [
    {
      title: 'Data Points',
      value: summary.total_observations.toLocaleString(),
      icon: <Timeline color="primary" />,
      subtitle: `${summary.date_range.start} to ${summary.date_range.end}`
    },
    {
      title: 'Average Price',
      value: `$${summary.price_stats.mean.toFixed(2)}`,
      icon: <TrendingUp color="primary" />,
      subtitle: `Range: $${summary.price_stats.min.toFixed(2)} - $${summary.price_stats.max.toFixed(2)}`
    },
    {
      title: 'Major Events',
      value: summary.total_events,
      icon: <Event color="primary" />,
      subtitle: 'Geopolitical & Economic'
    },
    {
      title: 'Change Points Detected',
      value: summary.changepoints_detected,
      icon: <Analytics color="primary" />,
      subtitle: 'Structural Breaks Detected'
    }
  ];

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        Analysis Summary
      </Typography>
      
      <Grid container spacing={2}>
        {summaryCards.map((card, index) => (
          <Grid item xs={12} sm={6} md={3} key={index}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                  {card.icon}
                  <Typography variant="h6" sx={{ ml: 1 }}>
                    {card.value}
                  </Typography>
                </Box>
                <Typography variant="subtitle2" color="text.primary">
                  {card.title}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {card.subtitle}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default AnalysisSummary;