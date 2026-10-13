> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hailuo 2.3 — Standard image to video API

> Standard image to video with Hailuo 2.3: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Hailuo 2.3](/docs/models/hailuo-2-3)

**Endpoint:** `POST https://api.higgsfield.ai/minimax/hailuo-2.3/standard/image-to-video`

**Endpoint ID:** `minimax/hailuo-2.3/standard/image-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/minimax%2Fhailuo-2.3%2Fstandard%2Fimage-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Hailuo 2.3 · Standard image to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* This Standard endpoint uses a fixed 768P output resolution; resolution is not a configurable field in the production schema.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/minimax/hailuo-2.3/standard/image-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
    "image_url": "https://example.com/input.jpg"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.',
       'image_url': 'https://example.com/input.jpg'}
  )
  result = higgsfield_client.subscribe(
      "minimax/hailuo-2.3/standard/image-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("minimax/hailuo-2.3/standard/image-to-video", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
        "image_url": "https://example.com/input.jpg"
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

<ParamField body="duration" type="integer" default="6">
  Requested output duration in seconds.
  Allowed values: `6`, `10`.
</ParamField>

<ParamField body="image_url" type="string" required>
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="prompt_optimizer" type="boolean" default="true">
  See the complete JSON schema below.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Minimax Hailuo 2.3 Playground",
    "required": [
      "prompt",
      "image_url"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "description": "Write your prompt here"
      },
      "duration": {
        "enum": [
          6,
          10
        ],
        "type": "integer",
        "title": "Duration",
        "default": 6
      },
      "image_url": {
        "type": "string",
        "title": "Image URL",
        "format": "uri"
      },
      "prompt_optimizer": {
        "type": "boolean",
        "title": "Prompt optimizer",
        "default": true
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

- [Hailuo 2.3 — Standard text to video API](/docs/models/hailuo-2-3/standard-text-to-video.md)
- [Kling 3.0 — Standard · Image to video API](/docs/models/kling-3/standard-image-to-video.md)
- [Kling 2.5 Turbo — Standard image to video API](/docs/models/kling-2-5-turbo/standard-image-to-video.md)
- [Hailuo 2.3 API](/docs/models/hailuo-2-3.md)
- [Video Generation API](/docs/models/video-generation.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.