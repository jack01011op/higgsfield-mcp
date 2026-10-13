> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Video 1.5 — Reference to video API

> Reference to video with Grok Imagine Video 1.5: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Grok Imagine Video 1.5](/docs/models/grok-video-1-5)

**Endpoint:** `POST https://api.higgsfield.ai/xai/grok-imagine-video/v1.5/reference-to-video`

**Endpoint ID:** `xai/grok-imagine-video/v1.5/reference-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/xai%2Fgrok-imagine-video%2Fv1.5%2Freference-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Grok Imagine Video 1.5 · Reference to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* This endpoint also accepts text-only requests or one first-frame image. Choose either image\_url or reference media (image\_urls/audio\_url); do not combine these modes.
* When image\_urls or audio\_url is provided, resolution must be 480p or 720p. The shared schema also lists 1080p, which is rejected in reference mode.
* Input images must decode as JPEG, PNG, WebP or GIF; SVG and XML are unsupported.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/xai/grok-imagine-video/v1.5/reference-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
    "image_urls": [
      "https://example.com/input.jpg"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.',
       'image_urls': ['https://example.com/input.jpg']}
  )
  result = higgsfield_client.subscribe(
      "xai/grok-imagine-video/v1.5/reference-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("xai/grok-imagine-video/v1.5/reference-to-video", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
        "image_urls": [
          "https://example.com/input.jpg"
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

<ParamField body="prompt" type="string" required>
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `1`.
  Maximum: `15`.
</ParamField>

<ParamField body="audio_url" type="string">
  Public URL of the audio reference.
  Format: `uri`.
</ParamField>

<ParamField body="image_url" type="string">
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Minimum items: `0`.
  Maximum items: `7`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="480p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="auto">
  Output width-to-height ratio.
  Allowed values: `"auto"`, `"1:1"`, `"16:9"`, `"9:16"`, `"4:3"`, `"3:4"`, `"3:2"`, `"2:3"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Grok Imagine Video 1.5 Reference Playground",
    "required": [
      "prompt"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "description": "Write your prompt here"
      },
      "duration": {
        "type": "integer",
        "title": "Duration",
        "default": 5,
        "maximum": 15,
        "minimum": 1
      },
      "audio_url": {
        "type": "string",
        "title": "Reference audio",
        "format": "uri"
      },
      "image_url": {
        "type": "string",
        "title": "First-frame image",
        "format": "uri"
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "title": "Image",
          "format": "uri"
        },
        "title": "Reference images",
        "maxItems": 7,
        "minItems": 0
      },
      "resolution": {
        "enum": [
          "480p",
          "720p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "480p"
      },
      "aspect_ratio": {
        "enum": [
          "auto",
          "1:1",
          "16:9",
          "9:16",
          "4:3",
          "3:4",
          "3:2",
          "2:3"
        ],
        "type": "string",
        "default": "auto"
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

- [Grok Imagine Video 1.5 API](/docs/models/grok-video-1-5.md)
- [Kling O3 — Video reference API](/docs/models/kling-o3/video-reference.md)
- [Kling Omni — Video reference API](/docs/models/kling-omni/video-reference.md)
- [Seedance 2.5 — Reference to video API](/docs/models/seedance-2-5/reference-to-video.md)
- [Wan 2.6 — Reference to video API](/docs/models/wan-2-6/reference-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.