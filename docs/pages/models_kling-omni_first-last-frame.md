> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Omni — First last frame API

> First last frame with Kling Omni: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling Omni](/docs/models/kling-omni)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/omni/first-last-frame`

**Endpoint ID:** `kling-video/omni/first-last-frame`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fomni%2Ffirst-last-frame/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling Omni · First last frame</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* first\_frame\_url supplies the starting frame; last\_frame\_url is optional. These names differ from the image\_url and last\_image\_url fields on Kling 3.0 image-to-video.
* Keep the top-level prompt within 2,500 characters; longer prompts are truncated.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/omni/first-last-frame \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A slow cinematic camera move around the subject in warm evening light.",
    "first_frame_url": "https://example.com/first-frame.jpg"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A slow cinematic camera move around the subject in warm evening '
                 'light.',
       'first_frame_url': 'https://example.com/first-frame.jpg'}
  )
  result = higgsfield_client.subscribe(
      "kling-video/omni/first-last-frame",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/omni/first-last-frame", {
    input:
      {
        "prompt": "A slow cinematic camera move around the subject in warm evening light.",
        "first_frame_url": "https://example.com/first-frame.jpg"
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
  Allowed values: `5`, `10`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`, `"1:1"`.
</ParamField>

<ParamField body="last_frame_url" type="string">
  Format: `uri`.
</ParamField>

<ParamField body="first_frame_url" type="string" required>
  Format: `uri`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling Omni Playground",
    "required": [
      "prompt",
      "first_frame_url"
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
        "enum": [
          5,
          10
        ],
        "type": "integer",
        "title": "Duration",
        "default": 5
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16",
          "1:1"
        ],
        "type": "string",
        "default": "16:9"
      },
      "last_frame_url": {
        "type": "string",
        "title": "Last frame URL",
        "format": "uri"
      },
      "first_frame_url": {
        "type": "string",
        "title": "First frame URL",
        "format": "uri"
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

- [Kling O3 — First last frame API](/docs/models/kling-o3/first-last-frame.md)
- [Kling Omni API](/docs/models/kling-omni.md)
- [Kling O3 — Image reference API](/docs/models/kling-o3/image-reference.md)
- [Kling O3 API](/docs/models/kling-o3.md)
- [Happy Horse 1.0 — Image to video API](/docs/models/happy-horse-1/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.