from datetime import datetime, timedelta
from events import SignalEvent
from random import random 
import numpy as np

class OptStrategy:
    def __init__(self, data_handler, events):
        """
        Initializes the OptStrategy with a data handler and an event queue.
        """
        self.data_handler = data_handler
        self.events = events
        self.rebalance_interval = timedelta(days=30)  # Example: rebalance monthly
        self.next_rebalance_time = None

    def calculate_signals(self, event):
        """
        Calculates trading signals based on market data.
        """
        if event.type == 'MARKET':
            # Perform signal generation logic here
            # Example: Generate a random signal for demonstration purposes
            symbol = self.data_handler.symbol_list[0]  # Select the first symbol from the list
            signal_type = 'LONG' if np.random.random() > 0.5 else 'SHORT'
            strength = 1.0
    
            # Create a SignalEvent and place it onto the event queue
            signal = SignalEvent(symbol, datetime.now(), signal_type, strength)
            self.events.put(signal)

    def calculate_target_weights(self):
        """
        Calculates target weights for each asset in the portfolio. This method can be
        replaced or modified to implement different portfolio optimization strategies.
        """
        # Equal weighting strategy for simplicity
        num_assets = len(self.data_handler.symbol_list)
        target_weights = {symbol: 1.0 / num_assets for symbol in self.data_handler.symbol_list}
        return target_weights

    def rebalance_portfolio(self, current_time):
        """Checks if it's time to rebalance the portfolio and adjusts positions accordingly.
        """
        if self.next_rebalance_time is None or current_time >= self.next_rebalance_time:
            target_weights = self.calculate_target_weights()
            self.adjust_positions(target_weights)
            self.next_rebalance_time = current_time + self.rebalance_interval

    def adjust_positions(self, target_weights):
        """
        Generates SignalEvents to adjust the portfolio positions according to the target weights.
        """
        for symbol, target_weight in target_weights.items():
            # Perform position adjustment logic here
            # Example: Generate a random signal for demonstration purposes
            signal_type = 'LONG' if np.random.random() > 0.5 else 'SHORT'
            strength = 1.0
    
            # Create a SignalEvent and place it onto the event queue
            signal = SignalEvent(symbol, datetime.now(), signal_type, strength)
            self.events.put(signal)
