> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 2.5 — Video extend API

> Video extend with Seedance 2.5: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Seedance 2.5](/docs/models/seedance-2-5)

**Endpoint:** `POST https://api.higgsfield.ai/bytedance/seedance-2.5/video-extend`

**Endpoint ID:** `bytedance/seedance-2.5/video-extend`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/bytedance%2Fseedance-2.5%2Fvideo-extend/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Seedance 2.5 · Video extend</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Use publicly accessible media URLs; asset:// references are rejected for these endpoints.
* The source video\_url counts toward the 10-video limit, so include at most 9 additional video\_urls. At most 50 media items are accepted across the source video and all reference arrays.
* Videos and audio may be trimmed or padded during preprocessing to fit their respective 30-second total budgets. Output framing follows the source video.
* duration is an integer from 4 to 30 seconds, with default 5.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/bytedance/seedance-2.5/video-extend \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
    "video_url": "https://example.com/input.mp4"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.',
       'video_url': 'https://example.com/input.mp4'}
  )
  result = higgsfield_client.subscribe(
      "bytedance/seedance-2.5/video-extend",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("bytedance/seedance-2.5/video-extend", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
        "video_url": "https://example.com/input.mp4"
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="prompt" type="string" required>
  Write your prompt here
  Minimum characters: `1`.
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `4`.
  Maximum: `30`.
</ParamField>

<ParamField body="video_url" type="string" required>
  Public URL of the source video.
  Format: `uri`.
</ParamField>

<ParamField body="audio_urls" type="array">
  Ordered public audio reference URLs.
  Minimum items: `1`.
  Maximum items: `10`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Minimum items: `1`.
  Maximum items: `30`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="video_urls" type="array">
  Ordered public video reference URLs.
  Minimum items: `1`.
  Maximum items: `10`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="bitrate_mode" type="string" default="high">
  Allowed values: `"standard"`, `"high"`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "required": [
      "prompt",
      "video_url"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "minLength": 1,
        "description": "Write your prompt here"
      },
      "duration": {
        "type": "integer",
        "default": 5,
        "maximum": 30,
        "minimum": 4
      },
      "video_url": {
        "type": "string",
        "format": "uri"
      },
      "audio_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 10,
        "minItems": 1
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 30,
        "minItems": 1
      },
      "resolution": {
        "enum": [
          "480p",
          "720p",
          "1080p"
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
        "maxItems": 10,
        "minItems": 1
      },
      "bitrate_mode": {
        "enum": [
          "standard",
          "high"
        ],
        "type": "string",
        "default": "high"
      },
      "generate_audio": {
        "type": "boolean",
        "default": true
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

- [Seedance 2.5 API](/docs/models/seedance-2-5.md)
- [Seedance 2.5 — Image to video API](/docs/models/seedance-2-5/image-to-video.md)
- [Seedance 2.5 — Reference to video API](/docs/models/seedance-2-5/reference-to-video.md)
- [Seedance 2.5 — Text to video API](/docs/models/seedance-2-5/text-to-video.md)
- [Seedance 2.5 — Video edit API](/docs/models/seedance-2-5/video-edit.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.