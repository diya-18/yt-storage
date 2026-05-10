# YT-Storage

This was a fun experimental project that started with the idea:
> “Can YouTube be used as cloud storage?”

The project basically converts files into image frames, stitches them into videos using FFmpeg, and later reconstructs the original file back from the video.

I also experimented with:
- lossless video encoding (FFV1)
- Reed-Solomon error correction
- YouTube API uploads

---

# Why This Is Not Practically Feasible

Even though the concept technically works locally, platforms like YouTube heavily reprocess uploaded videos which corrupts embedded binary data.

Some major limitations:
- YouTube compression destroys exact byte recovery
- FFV1/MKV archival formats are poorly supported
- storage overhead is huge
- uploads/downloads are slow
- no encryption/security layer
- not scalable for real-world storage

So this project is more of a systems engineering experiment than an actual cloud storage solution.

---

# Tech Used

- Python
- FFmpeg
- OpenCV
- NumPy
- ReedSolo
- YouTube Data API v3
- OAuth 2.0

---

# How It Works

```text
file
→ bytes
→ image frames
→ video
→ upload/store

video
→ frames
→ bytes
→ reconstructed file
```

---

# How To Run

## 1. Clone the repo

```bash
git clone https://github.com/diya-18/yt-storage.git
cd yt-storage
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

Also make sure FFmpeg is installed and added to PATH.

---

## 3. Add your input file

Put any file inside:

```text
data/input/
```

---

## 4. Run the pipeline

```bash
python -m cli.main
```

This will:
- encode the file into frames
- generate a video
- decode the video
- reconstruct the original file

---

# YouTube Uploads

To test uploads:
- enable YouTube Data API v3
- add OAuth credentials
- place `client_secret.json` inside:

```text
configs/
```

Then run the upload script.

---

# Learnings

This project taught me:
- how encoding pipelines work
- why metadata matters
- how error correction helps recovery
- how APIs + OAuth flows work
- why “technically correct” systems still fail in real-world environments

THIS really made me appreciate how difficult real distributed storage systems are.
