> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling O3 — Video reference API

> Video reference with Kling O3: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling O3](/docs/models/kling-o3)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/o3/video-reference`

**Endpoint ID:** `kling-video/o3/video-reference`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fo3%2Fvideo-reference/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling O3 · Video reference</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Supply exactly one video reference. duration controls the generated clip and accepts integer values from 3 to 10 seconds.
* You may also supply up to four image\_urls and up to four elements.
* Keep the top-level prompt within 2,500 characters; longer prompts are truncated.
* elements contains Kling element IDs as decimal strings. Each ID must belong to the account making the request; arbitrary provider IDs are rejected.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/o3/video-reference \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A slow cinematic camera move around the subject in warm evening light.",
    "video_urls": [
      "https://example.com/source-video.mp4"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A slow cinematic camera move around the subject in warm evening '
                 'light.',
       'video_urls': ['https://example.com/source-video.mp4']}
  )
  result = higgsfield_client.subscribe(
      "kling-video/o3/video-reference",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/o3/video-reference", {
    input:
      {
        "prompt": "A slow cinematic camera move around the subject in warm evening light.",
        "video_urls": [
          "https://example.com/source-video.mp4"
        ]
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="mode" type="string" default="pro">
  Allowed values: `"std"`, `"pro"`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `3`.
  Maximum: `10`.
</ParamField>

<ParamField body="elements" type="array">
  Minimum items: `0`.
  Maximum items: `4`.
  Each item: string.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Minimum items: `0`.
  Maximum items: `4`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="video_urls" type="array" required>
  Ordered public video reference URLs.
  Minimum items: `1`.
  Maximum items: `1`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="aspect_ratio" type="string">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`, `"1:1"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling O3 Playground",
    "required": [
      "prompt",
      "video_urls"
    ],
    "properties": {
      "mode": {
        "enum": [
          "std",
          "pro"
        ],
        "type": "string",
        "default": "pro"
      },
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "description": "Write your prompt here"
      },
      "duration": {
        "type": "integer",
        "title": "Duration",
        "default": 5,
        "maximum": 10,
        "minimum": 3
      },
      "elements": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "maxItems": 4,
        "minItems": 0
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "title": "Image URL",
          "format": "uri"
        },
        "maxItems": 4,
        "minItems": 0
      },
      "video_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "title": "Video URL",
          "format": "uri"
        },
        "maxItems": 1,
        "minItems": 1
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16",
          "1:1"
        ],
        "type": "string"
      }
    }
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

- [Kling O3 API](/docs/models/kling-o3.md)
- [Kling O3 — Video edit API](/docs/models/kling-o3/video-edit.md)
- [Kling O3 — Image reference API](/docs/models/kling-o3/image-reference.md)
- [Kling O3 — First last frame API](/docs/models/kling-o3/first-last-frame.md)
- [Kling Omni — Video reference API](/docs/models/kling-omni/video-reference.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.