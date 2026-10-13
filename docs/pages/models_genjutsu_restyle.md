> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Genjutsu — Restyle API

> Restyle with Genjutsu: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Genjutsu](/docs/models/genjutsu)

**Endpoint:** `POST https://api.higgsfield.ai/higgsfield/genjutsu/restyle/v1.0`

**Endpoint ID:** `higgsfield/genjutsu/restyle/v1.0`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/higgsfield%2Fgenjutsu%2Frestyle%2Fv1.0/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Genjutsu · Restyle</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Restyle changes the visual style of a source video while retaining its motion, shot composition, and source audio. Each request produces one video.
* Select a current style from GET /models/higgsfield/genjutsu/restyle/v1.0/presets and send its UUID as preset\_id. The example UUID below is illustrative of a published preset; fetch the current catalog before submitting.
* The source must be at least 4 seconds and no larger than 200 MiB. Videos longer than 30 seconds are trimmed to their first 30 seconds, including audio.
* Character references are optional: omit image\_urls or send \[] to restyle the existing source subjects. Supply up to 5 character images to guide their appearance.
* Defaults apply to omitted optional fields. Use \[] or an empty string where appropriate; null is not accepted.
* Output framing is derived from the source and animation cadence can depend on the selected style. Exact output duration and FPS may differ from the source.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/higgsfield/genjutsu/restyle/v1.0 \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "video_url": "https://example.com/input.mp4",
    "preset_id": "c2143317-f28d-4c3c-a0b8-39bd547e08a7",
    "image_urls": [],
    "prompt": "Preserve the original movement and camera composition.",
    "resolution": "720p"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'video_url': 'https://example.com/input.mp4',
       'preset_id': 'c2143317-f28d-4c3c-a0b8-39bd547e08a7',
       'image_urls': [],
       'prompt': 'Preserve the original movement and camera composition.',
       'resolution': '720p'}
  )
  result = higgsfield_client.subscribe(
      "higgsfield/genjutsu/restyle/v1.0",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("higgsfield/genjutsu/restyle/v1.0", {
    input:
      {
        "video_url": "https://example.com/input.mp4",
        "preset_id": "c2143317-f28d-4c3c-a0b8-39bd547e08a7",
        "image_urls": [],
        "prompt": "Preserve the original movement and camera composition.",
        "resolution": "720p"
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="prompt" type="string" default="">
  Optional additional guidance for the final video alongside the preset, source motion, and character references. Describe subject roles or details to retain, for example: “Keep the referenced character’s pink hair consistent across shots.” An empty string uses the visual inputs without additional instructions. This supplements preset\_id; it does not create a custom style or set duration, resolution, FPS, or audio behavior. Instructions guide a generative result and do not guarantee exact preservation.
  Maximum characters: `10000`.
</ParamField>

<ParamField body="preset_id" type="string" required>
  Required UUID from items\[].id in the [available styles](#available-styles) response. Selects one visual style for the subjects and scene. Send the ID, not the style name, preview URL, or list index. A prompt or character image does not replace this field. Hidden or unavailable presets fail input preparation; no alternative style is selected automatically. Custom/personal presets and multiple simultaneous styles are not supported.
  Format: `uuid`.
</ParamField>

<ParamField body="video_url" type="string" required>
  Direct URL of the source video that supplies motion, camera movement, composition, and the source scene. It must be downloadable without browser cookies or custom authentication headers; an unexpired signed HTTPS URL is suitable. Minimum duration: 4 seconds. Maximum download size: 200 MiB (209,715,200 bytes), including files that will be trimmed. Longer clips use only their first 30 seconds; trim your upload first if you need another segment. Use a decodable video such as MP4, not a player page or local file path. Original audio is retained when present; there is no new-soundtrack control.
  Minimum characters: `1`.
  Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array" default="[]">
  Optional character appearance references, in a stable order. Omit this field or send \[] to derive the styled subjects and scene from the source video. With references, each character image is restyled and the source background is cleaned and styled separately before video generation. Each URL must point directly to a downloadable image; JPEG and PNG are practical choices. Maximum download size: 64 MiB (67,108,864 bytes) per image. Images are normalized, so their dimensions do not set the output video size. These are character references, not style previews or background-only inputs. For multiple characters, describe the intended roles in prompt; the public API provides no explicit reference-to-person mapping.
  Maximum items: `5`.
  Each item: string. Minimum characters: `1`. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier; strings are case-sensitive. Defaults to 720p. Send a supported string such as "720p", not the number 720 or "HD". This setting selects the video price tier and does not set the aspect ratio, duration, or FPS.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Genjutsu Restyle",
    "required": [
      "video_url",
      "preset_id"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "default": "",
        "maxLength": 10000
      },
      "preset_id": {
        "type": "string",
        "title": "Style preset",
        "format": "uuid"
      },
      "video_url": {
        "type": "string",
        "title": "Source video",
        "format": "uri",
        "minLength": 1,
        "description": "Source video, 4–30 seconds. Longer videos are trimmed to 30 seconds."
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri",
          "minLength": 1
        },
        "title": "Character images",
        "default": [],
        "maxItems": 5,
        "description": "Optional character references. Leave empty to restyle the source frame."
      },
      "resolution": {
        "enum": [
          "480p",
          "720p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "720p"
      }
    },
    "additionalProperties": false
  }
  ```
</Accordion>

## Available styles

Styles are called **presets** in the API. Fetch the catalog before selecting a style:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --fail-with-body --silent --show-error \
  'https://api.higgsfield.ai/models/higgsfield/genjutsu/restyle/v1.0/presets' \
  -H "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}"
```

No request body, query parameters, or pagination parameters are needed. The endpoint requires authentication and access to the Restyle model. It returns all currently selectable system presets, ordered by name and ID. Hidden or unusable presets are omitted; personal/custom styles are not included.

Example response, shortened to one item:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "model": "higgsfield/genjutsu/restyle/v1.0",
  "items": [
    {
      "id": "c2143317-f28d-4c3c-a0b8-39bd547e08a7",
      "name": "Cel-Shaded CG Anime",
      "preview_url": "https://cdn.higgsfield.ai/restyle_presets/259d7ddb-4201-49f7-8a91-cee5bce28715.webp"
    }
  ]
}
```

| Response field | Meaning |
| - | - |
| `model` | The generation model to which this catalog belongs. |
| `items` | Array of available styles. Treat an empty array as no selectable styles. |
| `items[].id` | Style UUID. Copy this value into the generation request's `preset_id`. |
| `items[].name` | Human-readable style name for a menu or style picker. |
| `items[].preview_url` | Style preview image for display. This is not the value of `preset_id` and does not need to be sent in `image_urls`. |

Select exactly one item. Use its `id`, not its name, list position, or preview URL. The example ID above was available when this documentation was written; always use the current catalog in your application. If a saved selection disappears, refresh the list and select an available style.

## Character references

Without `image_urls`, Restyle takes the existing source subject and scene as its appearance reference. With `image_urls`, it styles each supplied character image and prepares a styled background from the source scene. In both cases, `video_url` supplies the motion and `preset_id` supplies the visual style.

For example, use this generation body to include a character reference. Replace the media URLs and select a current preset ID:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "video_url": "https://example.com/input.mp4",
  "preset_id": "c2143317-f28d-4c3c-a0b8-39bd547e08a7",
  "image_urls": ["https://example.com/character.png"],
  "prompt": "Keep the referenced character consistent across shots while preserving the original movement.",
  "resolution": "1080p"
}
```

There are only five public model inputs: `video_url`, `preset_id`, `image_urls`, `prompt`, and `resolution`. Batch size, duration, aspect ratio, FPS, scene mode, a separate background image, seed, and provider selection are not exposed by this model.

## Approximate pricing

| Resolution | Approximate price per source-video second |
| - | - |
| `480p` | \$0.318 |
| `720p` | \$0.681 |
| `1080p` | \$1.632 |

These are approximate per-second rates, not an exact total quote. Source duration is rounded up to whole seconds after trimming to 30 seconds: an 8.1-second source is billed as 9 seconds.

## Check request status

The same API key is used to list styles, submit generation, and poll the result. Set `HF_API_KEY_ID` and `HF_API_KEY_SECRET` to your API credentials. Set a unique `IDEMPOTENCY_KEY` for each intended generation, and reuse it only when retrying that request.

After submission, poll the returned `status_url`, or set `REQUEST_ID` to the returned ID:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --fail-with-body --silent --show-error \
  "https://api.higgsfield.ai/requests/${REQUEST_ID}/status" \
  -H "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}"
```

A request can be `queued` or `in_progress` before it completes. Stop polling on `completed`, `failed`, `nsfw`, or `canceled`. A failed response includes an `error` message. Media download and unavailable-preset errors can occur after acceptance; a request handle alone does not mean that generation succeeded. Keep signed media URLs valid while inputs are fetched.

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

- [Genjutsu API](/docs/models/genjutsu.md)
- [Genjutsu — Motion transfer API](/docs/models/genjutsu/motion-transfer.md)
- [Genjutsu — Object swap API](/docs/models/genjutsu/object-swap.md)
- [Video Generation API](/docs/models/video-generation.md)
- [Model API Reference](/docs/models.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.