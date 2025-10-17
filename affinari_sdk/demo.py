# demo.py
import sys
from pathlib import Path

# --- ensure local import works even if not installed ---
root = Path(__file__).resolve().parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from matching import weighted_manhattan
from schema_loader import load_schema

# --- load example data ---
user = load_schema(root / "user_profile.json")
venue = load_schema(root / "venue_profile.json")

# --- assign simple uniform weights ---
weights = {trait: 1.0 for trait in user.keys()}

# --- compute score ---
score = weighted_manhattan(user, venue, weights)

print("Affinari Alignment Demo")
print("-----------------------")
print(f"User traits:  {user}")
print(f"Venue traits: {venue}")
print(f"\nAlignment score: {score:.3f}")
