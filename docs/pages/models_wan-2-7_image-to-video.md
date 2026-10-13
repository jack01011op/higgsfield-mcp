> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.7 — Image to video API

> Image to video with Wan 2.7: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Wan 2.7](/docs/models/wan-2-7)

**Endpoint:** `POST https://api.higgsfield.ai/wan/v2.7/image-to-video`

**Endpoint ID:** `wan/v2.7/image-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/wan%2Fv2.7%2Fimage-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Wan 2.7 · Image to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* The prompt is optional. end\_image\_url supplies a last frame, and audio\_url can supply driving audio.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/wan/v2.7/image-to-video \
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
      "wan/v2.7/image-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("wan/v2.7/image-to-video", {
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

<ParamField body="seed" type="integer">
  Seed used to control generation randomness.
  Minimum: `1`.
  Maximum: `2147483646`.
</ParamField>

<ParamField body="prompt" type="string">
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `2`.
  Maximum: `15`.
</ParamField>

<ParamField body="audio_url" type="string">
  Public URL of the audio reference.
  Format: `uri`.
</ParamField>

<ParamField body="image_url" type="string" required>
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="end_image_url" type="string">
  Format: `uri`.
</ParamField>

<ParamField body="prompt_extend" type="boolean" default="false">
  Enable prompt expansion.
</ParamField>

<ParamField body="negative_prompt" type="string" default="">
  Content or visual features to avoid.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Wan 2.6 Playground",
    "required": [
      "image_url"
    ],
    "properties": {
      "seed": {
        "type": "integer",
        "maximum": 2147483646,
        "minimum": 1
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
        "maximum": 15,
        "minimum": 2
      },
      "audio_url": {
        "type": "string",
        "title": "Audio URL",
        "format": "uri"
      },
      "image_url": {
        "type": "string",
        "title": "Image URL",
        "format": "uri"
      },
      "resolution": {
        "enum": [
          "720p",
          "1080p"
        ],
        "type": "string",
        "default": "720p"
      },
      "end_image_url": {
        "type": "string",
        "title": "Image URL",
        "format": "uri"
      },
      "prompt_extend": {
        "type": "boolean",
        "default": false
      },
      "negative_prompt": {
        "type": "string",
        "title": "Negative prompt",
        "default": ""
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

- [Wan 2.7 API](/docs/models/wan-2-7.md)
- [Wan 2.7 — Reference to video API](/docs/models/wan-2-7/reference-to-video.md)
- [Wan 2.7 — Text to video API](/docs/models/wan-2-7/text-to-video.md)
- [Wan 2.6 — Image to video API](/docs/models/wan-2-6/image-to-video.md)
- [Wan 3.0 — Image to video API](/docs/models/wan-3/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.