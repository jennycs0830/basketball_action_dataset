# 🏀 Basketball Action Classification Dataset

This dataset was created for training and evaluating video-based action recognition models in basketball. It contains manually curated and labeled clips, categorized into five fundamental basketball actions: **Defense**, **Dribbling**, **Shooting**, **Passing**, and **Nothing**.

---

## 📌 Introduction

The dataset originates from private full-court game footage of our university basketball team. The footage is not publicly available and is used with permission from the team coach.

The goal of this project is to develop a livestream recording system integrated with an AI-powered action recognition model for automated data tagging and analysis. This dataset serves as the foundation for training models capable of performing real-time basketball action recognition.

### 🏷️ Action Classes

| Class     | Description                                                              |
|-----------|---------------------------------------------------------------------------|
| Defense   | Player is actively defending against an opponent.                        |
| Dribbling | Player is dribbling the ball.                                            |
| Shooting  | Player is attempting a shot.                                             |
| Passing   | Player is making a pass.                                                 |
| Nothing   | No significant action is occurring.                                      |

The "Nothing" class helps the model learn to distinguish between meaningful and irrelevant movements.

---

## 🎥 Data Collection

### 1. Screen Recording
Game footage was screen-recorded from a private YouTube channel containing full-court game videos. To extract shorter, meaningful clips:

- Each clip was trimmed to a duration of **0.3 seconds** using FFmpeg.
- Shorter clip lengths are not supported by most editing tools, so FFmpeg was used for precision:

```bash
ffmpeg -i input.mp4 -ss 00:00:05.50 -t 0.3 -an output.mp4

### 2. Cropping Video Size

After segmenting the game footage, each clip was manually cropped to highlight the **target player's action**. This was done using an iPhone, zooming in and cropping in **portrait mode (aspect ratio 16:9)** to reduce background noise and emphasize the relevant movement. This process ensures the model focuses on the player performing the action, rather than irrelevant areas on the court.

---

## 📊 Dataset Statistics

### Version 1 (V1)

| Class     | Train | Test | Total |
|-----------|-------|------|-------|
| Defense   | 30    | 6    | 36    |
| Dribbling | 56    | 12   | 68    |
| Shooting  | 13    | 8    | 21    |
| Passing   | 34    | 9    | 43    |
| Nothing   | 16    | 3    | 19    |
| **Total** | 149   | 38   | 187   |

### Version 2 (V2)

| Class     | Train | Test | Total |
|-----------|-------|------|-------|
| Defense   | 49    | 15   | 64    |
| Dribbling | 49    | 19   | 68    |
| Shooting  | 25    | 4    | 29    |
| Passing   | 55    | 10   | 65    |
| Nothing   | 48    | 9    | 57    |
| **Total** | 226   | 57   | 283   |

✅ **V2 is an extended and more balanced version of V1**, offering improved class distribution for training and evaluation.

---

## 🛠 Preprocessing

### 1. Resizing and Padding

To ensure consistent input size for deep learning models:

- All frames are resized to **224 × 224 pixels** using **resize with padding**.
- The aspect ratio is preserved by first resizing using the **shorter side**, then padding with black pixels to reach the desired dimensions.
- This format aligns with standard input sizes of popular pretrained CNN architectures (e.g., **ResNet**, **VGG**, **MobileNet**).

### 2. Fixed Frame Count per Clip

- Each clip is normalized to contain exactly **7 frames**.
- If a video has fewer than 7 frames, **black (empty) frames** are appended to meet the required length.
- This standardization ensures uniform input dimensions during training and inference.

---
