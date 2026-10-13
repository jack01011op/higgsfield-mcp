> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 2.0 — Reference to video API

> Reference to video with Seedance 2.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Seedance 2.0](/docs/models/seedance-2)

**Endpoint:** `POST https://api.higgsfield.ai/bytedance/seedance-2.0/reference-to-video`

**Endpoint ID:** `bytedance/seedance-2.0/reference-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/bytedance%2Fseedance-2.0%2Freference-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Seedance 2.0 · Reference to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Use publicly accessible media URLs; asset:// references are rejected for these endpoints.
* Provide a nonempty image\_urls or video\_urls array. Audio alone does not satisfy the reference requirement. Do not mix reference arrays with image\_url, end\_image\_url or video\_url.
* Reference videos may be resized, transcoded and trimmed to 15 seconds each. Reference audio is normalized to 2–15 seconds per file and at most 15 seconds total.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/bytedance/seedance-2.0/reference-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "image_urls": [
      "https://example.com/input.jpg"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'image_urls': ['https://example.com/input.jpg']}
  )
  result = higgsfield_client.subscribe(
      "bytedance/seedance-2.0/reference-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("bytedance/seedance-2.0/reference-to-video", {
    input:
      {
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

<ParamField body="prompt" type="string">
  Write your prompt here
  Minimum characters: `1`.
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `4`.
  Maximum: `15`.
</ParamField>

<ParamField body="audio_urls" type="array">
  Ordered public audio reference URLs.
  Minimum items: `1`.
  Maximum items: `3`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Minimum items: `1`.
  Maximum items: `9`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`, `"4k"`.
</ParamField>

<ParamField body="video_urls" type="array">
  Ordered public video reference URLs.
  Minimum items: `1`.
  Maximum items: `3`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, `"9:16"`, `"21:9"`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "if": {
      "required": [
        "image_urls"
      ]
    },
    "else": {
      "required": [
        "video_urls"
      ]
    },
    "type": "object",
    "required": [],
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
      "audio_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 3,
        "minItems": 1
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 9,
        "minItems": 1
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
      "video_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "maxItems": 3,
        "minItems": 1
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
- [Seedance 2.0 — Image to video API](/docs/models/seedance-2/image-to-video.md)
- [Seedance 2.0 — Text to video API](/docs/models/seedance-2/text-to-video.md)
- [Seedance 2.5 — Reference to video API](/docs/models/seedance-2-5/reference-to-video.md)
- [Seedance 2.5 — Image to video API](/docs/models/seedance-2-5/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.