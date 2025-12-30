"""
Utility Module
Helper functions for logging and path management
"""

import os
import logging
from datetime import datetime

def setup_paths(root_dir='.'):
    """
    Setup and verify project paths
    
    Args:
        root_dir (str): Project root directory
        
    Returns:
        dict: Path configuration
    """
    paths = {
        'root': root_dir,
        'data_raw': os.path.join(root_dir, 'data/raw'),
        'data_processed': os.path.join(root_dir, 'data/processed'),
        'models': os.path.join(root_dir, 'models'),
        'visualizations': os.path.join(root_dir, 'visualizations'),
        'reports': os.path.join(root_dir, 'reports'),
        'config': os.path.join(root_dir, 'config')
    }
    
    print("Project Paths:")
    for key, path in paths.items():
        exists = "✓" if os.path.exists(path) else "✗"
        print(f"  {exists} {key}: {path}")
    
    return paths


def create_logger(name, log_level=logging.INFO):
    """
    Create a logger instance
    
    Args:
        name (str): Logger name
        log_level: Logging level
        
    Returns:
        logging.Logger: Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


def save_summary(summary_text, output_file='reports/analysis_summary.txt'):
    """
    Save analysis summary to file
    
    Args:
        summary_text (str): Summary text
        output_file (str): Output file path
    """
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n")
            f.write(summary_text)
        print(f"✓ Summary saved: {output_file}")
    except Exception as e:
        print(f"✗ Error saving summary: {str(e)}")