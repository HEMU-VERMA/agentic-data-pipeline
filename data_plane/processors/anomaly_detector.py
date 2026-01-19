import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        # Isolation Forest is ideal for detecting spikes or drops in streaming data
        self.model = IsolationForest(contamination=0.05, random_state=42)

    def detect_anomalies(self, data_points: list):
        """
        Takes a list of values (e.g., hourly sales) and flags unusual behavior.
        """
        if len(data_points) < 5:
            return [] # Need at least 5 points to start modeling

        # Prepare data for sklearn
        df = pd.DataFrame(data_points, columns=['value'])
        
        # Fit model and predict (-1 is anomaly, 1 is normal)
        self.model.fit(df)
        preds = self.model.predict(df)
        
        # Identify indices where anomalies exist
        anomaly_indices = np.where(preds == -1)[0]
        
        results = []
        for idx in anomaly_indices:
            results.append({
                "index": int(idx),
                "value": float(data_points[idx]),
                "status": "CRITICAL_ANOMALY"
            })
            
        return results