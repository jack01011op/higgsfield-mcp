> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 2.0 — Image to video API

> Image to video with Seedance 2.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Seedance 2.0](/docs/models/seedance-2)

**Endpoint:** `POST https://api.higgsfield.ai/bytedance/seedance-2.0/image-to-video`

**Endpoint ID:** `bytedance/seedance-2.0/image-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/bytedance%2Fseedance-2.0%2Fimage-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Seedance 2.0 · Image to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Use publicly accessible media URLs; asset:// references are rejected for these endpoints.
* The prompt is optional. Output framing follows image\_url; end\_image\_url is the optional last frame.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/bytedance/seedance-2.0/image-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "image_url": "https://example.com/input.jpg"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'image_url': 'https://example.com/input.jpg'}
  )
  result = higgsfield_client.subscribe(
      "bytedance/seedance-2.0/image-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("bytedance/seedance-2.0/image-to-video", {
    input:
      {
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

<ParamField body="prompt" type="string">
  Write your prompt here
  Minimum characters: `1`.
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `4`.
  Maximum: `15`.
</ParamField>

<ParamField body="image_url" type="string" required>
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`, `"4k"`.
</ParamField>

<ParamField body="end_image_url" type="string">
  Format: `uri`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "required": [
      "image_url"
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
        "maximum": 15,
        "minimum": 4
      },
      "image_url": {
        "type": "string",
        "format": "uri"
      },
      "resolution": {
        "enum": [
          "480p",
          "720p",
          "1080p",
          "4k"
        ],
        "type": "string",
        "default": "720p"
      },
      "end_image_url": {
        "type": "string",
        "format": "uri"
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

- [Seedance 2.0 API](/docs/models/seedance-2.md)
- [Seedance 2.0 — Reference to video API](/docs/models/seedance-2/reference-to-video.md)
- [Seedance 2.0 — Text to video API](/docs/models/seedance-2/text-to-video.md)
- [Grok Image 2.0 API](/docs/models/grok-image-2.md)
- [Grok Image 2.0 — Generate and edit API](/docs/models/grok-image-2/generate-and-edit.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.