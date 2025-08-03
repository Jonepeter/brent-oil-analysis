import React, { useState } from 'react';
import { 
  Typography, 
  List, 
  ListItem, 
  ListItemText, 
  Chip, 
  Box,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Button
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import axios from 'axios';

const EventsList = ({ events }) => {
  const [eventImpacts, setEventImpacts] = useState({});
  const [loadingImpacts, setLoadingImpacts] = useState({});

  const getEventImpact = async (eventIndex) => {
    if (eventImpacts[eventIndex]) return;
    
    setLoadingImpacts(prev => ({ ...prev, [eventIndex]: true }));
    
    try {
      const response = await axios.get(`/api/event-impact/${eventIndex}`);
      setEventImpacts(prev => ({ ...prev, [eventIndex]: response.data.impact }));
    } catch (error) {
      console.error('Error fetching event impact:', error);
    } finally {
      setLoadingImpacts(prev => ({ ...prev, [eventIndex]: false }));
    }
  };

  const getCategoryColor = (category) => {
    switch (category) {
      case 'Geopolitical': return 'error';
      case 'Economic': return 'warning';
      case 'OPEC Policy': return 'primary';
      case 'Sanctions': return 'secondary';
      default: return 'default';
    }
  };

  const getImpactColor = (impact) => {
    switch (impact) {
      case 'High': return 'error';
      case 'Medium': return 'warning';
      case 'Low': return 'success';
      default: return 'default';
    }
  };

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        Major Events ({events.length})
      </Typography>
      
      <List>
        {events.map((event, index) => (
          <Accordion key={index} sx={{ mb: 1 }}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Box sx={{ width: '100%' }}>
                <Typography variant="subtitle2" noWrap>
                  {event.Event}
                </Typography>
                <Box sx={{ display: 'flex', gap: 1, mt: 1 }}>
                  <Chip 
                    label={event.Category} 
                    size="small" 
                    color={getCategoryColor(event.Category)}
                  />
                  <Chip 
                    label={event.Impact_Expected} 
                    size="small" 
                    color={getImpactColor(event.Impact_Expected)}
                    variant="outlined"
                  />
                </Box>
              </Box>
            </AccordionSummary>
            
            <AccordionDetails>
              <Typography variant="body2" color="text.secondary" paragraph>
                <strong>Date:</strong> {new Date(event.Date).toLocaleDateString()}
              </Typography>
              
              <Typography variant="body2" paragraph>
                {event.Description}
              </Typography>

              {!eventImpacts[index] && (
                <Button 
                  size="small" 
                  onClick={() => getEventImpact(index)}
                  disabled={loadingImpacts[index]}
                >
                  {loadingImpacts[index] ? 'Loading.......' : 'Analyze Impact'}
                </Button>
              )}

              {eventImpacts[index] && (
                <Box sx={{ mt: 2, p: 2, bgcolor: 'grey.50', borderRadius: 1 }}>
                  <Typography variant="subtitle2" gutterBottom>
                    Impact Analysis:
                  </Typography>
                  <Typography variant="body2">
                    Price Change: {eventImpacts[index].price_change_pct.toFixed(2)}%
                  </Typography>
                  <Typography variant="body2">
                    Volatility Change: {eventImpacts[index].volatility_change_pct.toFixed(2)}%
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    Analysis window: ±{eventImpacts[index].analysis_window_days} days
                  </Typography>
                </Box>
              )}
            </AccordionDetails>
          </Accordion>
        ))}
      </List>
    </Box>
  );
};

export default EventsList;