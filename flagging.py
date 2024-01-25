import os

import argparse
from dotenv import load_dotenv

load_dotenv()

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='Example script with command-line flags.')

# Add flags/arguments
parser.add_argument('--host', type=str, help='Database host address.')
parser.add_argument('--database', type=str, help='Database name.')
parser.add_argument('--data', type=str, help='root dir to features.')

# Parse the command-line arguments
args = parser.parse_args()

args.host = args.host or os.getenv("FEATURE_PATH")
args.database = args.database or os.getenv("HOST")
args.data = args.data or os.getenv("FEATURE_PATH")