# Hi

This is a tiny Python script to help me get something to read during the hot,
dry, dehydrated and boring afternoon using subtitles from TV shows and cartoons in
French. It'll translate the ```.srt``` file to an easy, nice to eyes, formatted markdown
file with English translations side by side(using ollama, of course. It's 2025.).

Besides that, my github Sematary's stony ground haven't been dig open for ages now.
So I'm just gonna bring this tiny thing, not even a project here. Maybe one day.
It'll be resurrected and return to my laptop. Or maybe, sometime,
it stays here is better.

---

## Use example:


```bash

$ srt2md -i path_to_srt -o path_to_md -s ollama_server_url

```

Almost forgot to mention that the llm model is hard coded in the script. In this
case, it's ```gemma3:4b```. So if you somehow, in some way you stumble upon this page and
decide to use it, make sure you have a working ollama server up and running.
