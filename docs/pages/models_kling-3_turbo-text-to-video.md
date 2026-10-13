> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 3.0 — Turbo · Text to video API

> Turbo · Text to video with Kling 3.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling 3.0](/docs/models/kling-3)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/v3.0-turbo/text-to-video`

**Endpoint ID:** `kling-video/v3.0-turbo/text-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fv3.0-turbo%2Ftext-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling 3.0 · Turbo · Text to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* duration accepts integers from 3 to 15 seconds. resolution accepts 720p or 1080p and defaults to 720p.
* This endpoint has no sound, multi\_shots, elements, or last-frame field.
* aspect\_ratio accepts 16:9, 9:16, or 1:1 and defaults to 16:9.
* Keep prompt within 3,072 characters; longer prompts are truncated.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/v3.0-turbo/text-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A slow cinematic tracking shot along a sunlit coastal road."
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A slow cinematic tracking shot along a sunlit coastal road.'}
  )
  result = higgsfield_client.subscribe(
      "kling-video/v3.0-turbo/text-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/v3.0-turbo/text-to-video", {
    input:
      {
        "prompt": "A slow cinematic tracking shot along a sunlit coastal road."
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
  Minimum: `3`.
  Maximum: `15`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`, `"1:1"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling 3.0 Turbo",
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
        "minimum": 3
      },
      "resolution": {
        "enum": [
          "720p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "720p"
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16",
          "1:1"
        ],
        "type": "string",
        "title": "Aspect ratio",
        "default": "16:9"
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

- [Kling 3.0 — Turbo · Image to video API](/docs/models/kling-3/turbo-image-to-video.md)
- [Kling 2.5 Turbo — Pro text to video API](/docs/models/kling-2-5-turbo/pro-text-to-video.md)
- [Kling 3.0 — Standard · Text to video API](/docs/models/kling-3/standard-text-to-video.md)
- [Kling 3.0 — 4K · Text to video API](/docs/models/kling-3/4k-text-to-video.md)
- [Kling 3.0 — Pro · Text to video API](/docs/models/kling-3/pro-text-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.