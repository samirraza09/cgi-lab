import os
import json

print("Content-type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))