> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cinema Studio 4.0 — Generate API

> Generate with Cinema Studio 4.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Cinema Studio 4.0](/docs/models/cinema-studio-4)

**Endpoint:** `POST https://api.higgsfield.ai/higgsfield/cinema-studio/4.0`

**Endpoint ID:** `higgsfield/cinema-studio/4.0`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/higgsfield%2Fcinema-studio%2F4.0/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Cinema Studio 4.0 · Generate</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* This is the public Cinema Studio 4.0 workflow. It uses text-to-video when references are absent and reference-to-video when any media array is nonempty.
* Omit creative-control fields to let the director choose them automatically; the literal value "auto" is not accepted for these enum fields.
* Optional prompt references use one-based tokens such as \<\<\<image\_1>>>, \<\<\<video\_1>>> and \<\<\<audio\_1>>>. Each token must refer to an attached item of the same media type.
* This endpoint produces a new video. Editing and extension use the separate Seedance 2.5 endpoints.
* Reference media are limited to 30 images, 10 videos and 10 audio files, with at most 50 items total. Video and audio may be normalized to separate 30-second total budgets.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/higgsfield/cinema-studio/4.0 \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement."
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.'}
  )
  result = higgsfield_client.subscribe(
      "higgsfield/cinema-studio/4.0",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("higgsfield/cinema-studio/4.0", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement."
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="era" type="string">
  Allowed values: `"1960s"`, `"1980s"`, `"1990s"`, `"2000s"`, `"2020s"`.
</ParamField>

<ParamField body="genre" type="string">
  Allowed values: `"epic"`, `"drama"`, `"noir"`, `"comedy"`, `"horror"`, `"action"`.
</ParamField>

<ParamField body="light" type="string">
  Allowed values: `"silhouette"`, `"practicals"`, `"window"`, `"overhead-fall"`, `"contre-jour"`, `"soft-cross"`.
</ParamField>

<ParamField body="pacing" type="string">
  Allowed values: `"chaotic"`, `"dynamic"`, `"calm"`, `"single-shot"`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Text instructions for the generation or edit.
  Minimum characters: `1`.
  Pattern: `\S`.
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `4`.
  Maximum: `30`.
</ParamField>

<ParamField body="audio_urls" type="array">
  Ordered public audio reference URLs.
  Maximum items: `10`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Maximum items: `30`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`.
</ParamField>

<ParamField body="video_urls" type="array">
  Ordered public video reference URLs.
  Maximum items: `10`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="camera_lens" type="string">
  Allowed values: `"clean-sharp"`, `"anamorphic"`, `"vintage-anamorphic"`, `"warm-vintage"`, `"halation-vintage"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, `"9:16"`, `"21:9"`.
</ParamField>

<ParamField body="camera_model" type="string">
  Allowed values: `"modern"`, `"35mm-film"`, `"8mm-film"`, `"dv-camcorder"`.
</ParamField>

<ParamField body="color_palette" type="string">
  Allowed values: `"static-noon"`, `"twilight-fable"`, `"back-row-kissing-seats"`, `"on-the-other-side-of-the-porthole"`, `"the-emerald-ambush"`, `"highway-standoff"`, `"the-faded-fresco"`, `"oil-ochre"`, `"the-mountain-convent"`, `"ghost-in-the-code"`, `"pink-velvet"`, `"two-days-to-the-horizon"`, `"industrial-fog"`, `"stairs-go-up"`, `"field-post"`, `"home-is-the-next-gas-station"`, `"glossy-flesh"`, `"the-crimson-ballet"`, `"neon-rain-at-midnight"`, `"the-morning-after-rain"`, `"the-iron-borough"`, `"the-ground"`, `"the-investigation"`, `"turquoise-mirage"`, `"a-dream-in-color"`, `"breakfast-on-schedule"`, `"favela-gold"`, `"a-hotel-for-one"`, `"after-dark"`, `"crimson-vigi"`, `"the-neighbors-saw-everything"`, `"the-grey-channel"`, `"mirage-at-noon"`, `"bubblegum-boulevard"`, `"yellow-room"`, `"the-earth-keeps-things-reluctantly"`, `"tropic-fever-dream"`, `"bioluminescent-night"`, `"dont-turn-it-off-im-watching"`, `"the-silk-curtain-falls"`, `"the-butterfly"`, `"playtime"`, `"wallpaper-romance"`, `"overtime"`, `"the-way-home-is-longer"`, `"everyone-speaks-in-whispers"`, `"runaway-summer"`, `"amber-wasteland"`, `"the-circus"`, `"gasoline-sunset"`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<ParamField body="camera_aperture" type="string">
  Allowed values: `"f14-wide-open"`, `"f4-moderate"`, `"f11-deep-focus"`.
</ParamField>

<ParamField body="camera_movement" type="string">
  Allowed values: `"snorricam"`, `"robot-arm"`, `"tilt-up"`, `"rack-focus"`, `"tilt-down"`, `"pov"`, `"pan-left"`, `"crane-up"`, `"pan-right"`, `"crane-down"`, `"side-tracking"`, `"pedestal-up"`, `"pedestal-down"`, `"handheld"`, `"tracking"`, `"drone-orbit"`, `"dolly-zoom"`, `"aerial-pullback"`, `"static-shot"`, `"bullet-time"`, `"whip-pan"`, `"slow-zoom-in"`, `"arc-left"`, `"slow-zoom-out"`, `"arc-right"`, `"truck-right"`, `"dolly-in"`, `"truck-left"`, `"dolly-out"`, `"slider-right"`, `"crush-zoom"`, `"slider-left"`, `"helicopter-shot"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "required": [
      "prompt"
    ],
    "properties": {
      "era": {
        "enum": [
          "1960s",
          "1980s",
          "1990s",
          "2000s",
          "2020s"
        ],
        "type": "string"
      },
      "genre": {
        "enum": [
          "epic",
          "drama",
          "noir",
          "comedy",
          "horror",
          "action"
        ],
        "type": "string"
      },
      "light": {
        "enum": [
          "silhouette",
          "practicals",
          "window",
          "overhead-fall",
          "contre-jour",
          "soft-cross"
        ],
        "type": "string"
      },
      "pacing": {
        "enum": [
          "chaotic",
          "dynamic",
          "calm",
          "single-shot"
        ],
        "type": "string"
      },
      "prompt": {
        "type": "string",
        "pattern": "\\S",
        "minLength": 1
      },
      "duration": {
        "type": "integer",
        "default": 5,
        "maximum": 30,
        "minimum": 4
      },
      "audio_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 10
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 30
      },
      "resolution": {
        "enum": [
          "480p",
          "720p"
        ],
        "type": "string",
        "default": "720p"
      },
      "video_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 10
      },
      "camera_lens": {
        "enum": [
          "clean-sharp",
          "anamorphic",
          "vintage-anamorphic",
          "warm-vintage",
          "halation-vintage"
        ],
        "type": "string"
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "4:3",
          "1:1",
          "3:4",
          "9:16",
          "21:9"
        ],
        "type": "string",
        "default": "16:9"
      },
      "camera_model": {
        "enum": [
          "modern",
          "35mm-film",
          "8mm-film",
          "dv-camcorder"
        ],
        "type": "string"
      },
      "color_palette": {
        "enum": [
          "static-noon",
          "twilight-fable",
          "back-row-kissing-seats",
          "on-the-other-side-of-the-porthole",
          "the-emerald-ambush",
          "highway-standoff",
          "the-faded-fresco",
          "oil-ochre",
          "the-mountain-convent",
          "ghost-in-the-code",
          "pink-velvet",
          "two-days-to-the-horizon",
          "industrial-fog",
          "stairs-go-up",
          "field-post",
          "home-is-the-next-gas-station",
          "glossy-flesh",
          "the-crimson-ballet",
          "neon-rain-at-midnight",
          "the-morning-after-rain",
          "the-iron-borough",
          "the-ground",
          "the-investigation",
          "turquoise-mirage",
          "a-dream-in-color",
          "breakfast-on-schedule",
          "favela-gold",
          "a-hotel-for-one",
          "after-dark",
          "crimson-vigi",
          "the-neighbors-saw-everything",
          "the-grey-channel",
          "mirage-at-noon",
          "bubblegum-boulevard",
          "yellow-room",
          "the-earth-keeps-things-reluctantly",
          "tropic-fever-dream",
          "bioluminescent-night",
          "dont-turn-it-off-im-watching",
          "the-silk-curtain-falls",
          "the-butterfly",
          "playtime",
          "wallpaper-romance",
          "overtime",
          "the-way-home-is-longer",
          "everyone-speaks-in-whispers",
          "runaway-summer",
          "amber-wasteland",
          "the-circus",
          "gasoline-sunset"
        ],
        "type": "string"
      },
      "generate_audio": {
        "type": "boolean",
        "default": true
      },
      "camera_aperture": {
        "enum": [
          "f14-wide-open",
          "f4-moderate",
          "f11-deep-focus"
        ],
        "type": "string"
      },
      "camera_movement": {
        "enum": [
          "snorricam",
          "robot-arm",
          "tilt-up",
          "rack-focus",
          "tilt-down",
          "pov",
          "pan-left",
          "crane-up",
          "pan-right",
          "crane-down",
          "side-tracking",
          "pedestal-up",
          "pedestal-down",
          "handheld",
          "tracking",
          "drone-orbit",
          "dolly-zoom",
          "aerial-pullback",
          "static-shot",
          "bullet-time",
          "whip-pan",
          "slow-zoom-in",
          "arc-left",
          "slow-zoom-out",
          "arc-right",
          "truck-right",
          "dolly-in",
          "truck-left",
          "dolly-out",
          "slider-right",
          "crush-zoom",
          "slider-left",
          "helicopter-shot"
        ],
        "type": "string"
      }
    },
    "additionalProperties": false
  }
  ```
</Accordion>

## Response

Submission returns a request handle. Poll `status_url` until `status` is `completed`, or use [webhooks](/docs/how-to/webhooks).

```json Accepted theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "status": "queued",
  "request_id": "REQUEST_ID",
  "status_url": "https://api.higgsfield.ai/requests/REQUEST_ID/status",
  "cancel_url": "https://api.higgsfield.ai/requests/REQUEST_ID/cancel"
}
```

A completed response includes the following output fields:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "status": "completed",
  "request_id": "REQUEST_ID",
  "video": {
    "url": "https://example.com/output.mp4"
  }
}
```

See [idempotent requests](/docs/concepts/idempotency), [polling](/docs/concepts/polling), [request errors](/docs/concepts/errors) and [authentication](/docs/authentication) for shared request handling.


## Related topics

- [Cinema Studio 4.0 API](/docs/models/cinema-studio-4.md)
- [Ideogram 4.0 — Generate API](/docs/models/ideogram-4/generate.md)
- [Ads Studio — Generate ads API](/docs/models/ads-studio/generate.md)
- [Image Generation API](/docs/models/image-generation.md)
- [Ideogram 4.0 API](/docs/models/ideogram-4.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.