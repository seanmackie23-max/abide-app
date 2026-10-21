# The first reel (20 s, 1080 × 1920)

1. Serve the built site on port 8767 (`node build.mjs`, copy `.cache/art` into `dist/art`, `python3 -m http.server 8767` in `dist`).
2. Copy into this folder: the paintings (`pannini-st-peters-1400.jpg`, `saenredam-cathedral-1400.jpg`, `strozzi-francis-prayer-1400.jpg` from `.cache/art`) and the fonts from `public/fonts`.
3. `node shots.mjs` (app screens), `node render.mjs` (630 frames), then
   `ffmpeg -framerate 30 -i frames/f%04d.jpg -c:v libx264 -crf 19 -pix_fmt yuv420p -movflags +faststart rose-window-reel.mp4`.

`film.html` holds the timing and the words; change them there. The video is silent: add music in Instagram's own library when posting.
