import urllib.request
import os

# High-quality Greek Yogurt and Greek aesthetics photos from Unsplash
photos = [
    "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&q=80&w=800", # Yogurt bowl
    "https://images.unsplash.com/photo-1516100882582-96c3a05fe590?auto=format&fit=crop&q=80&w=800", # Honey and yogurt
    "https://images.unsplash.com/photo-1550507992-eb63ffee0847?auto=format&fit=crop&q=80&w=800", # Fruit and yogurt
    "https://images.unsplash.com/photo-1610450530932-8495a0242250?auto=format&fit=crop&q=80&w=800"  # Greek island aesthetic
]

target_dir = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera"

for i, url in enumerate(photos, 1):
    filename = f"ig{i}.jpg"
    filepath = os.path.join(target_dir, filename)
    print(f"Downloading {filename}...")
    try:
        # Using a User-Agent to avoid blocks
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

print("Done!")
