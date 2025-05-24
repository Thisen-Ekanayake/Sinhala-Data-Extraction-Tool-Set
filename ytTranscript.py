from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import os

# === CONFIG ===
video_id = ""  # replace with the actual video ID
save_dir = "youtube_transcripts"
os.makedirs(save_dir, exist_ok=True)

def save_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['si'])

        # Format content
        lines = [f"{entry['start']:.2f}s: {entry['text']}" for entry in transcript]
        full_text = "\n".join(lines)

        # Save to file
        file_path = os.path.join(save_dir, f"{video_id}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_text)

        print(f"[{video_id}] ✔️ Transcript saved ({len(lines)} lines)")

    except TranscriptsDisabled:
        print(f"[{video_id}] Transcripts disabled")
    except NoTranscriptFound:
        print(f"[{video_id}] No Sinhala transcript found")
    except Exception as e:
        print(f"[{video_id}] Error: {e}")

# === RUN ===
save_transcript(video_id)
