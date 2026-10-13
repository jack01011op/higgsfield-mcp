> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Omni — Video edit API

> Video edit with Kling Omni: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling Omni](/docs/models/kling-omni)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/omni/video-edit`

**Endpoint ID:** `kling-video/omni/video-edit`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fomni%2Fvideo-edit/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling Omni · Video edit</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Supply exactly one source video from 3 to 10 seconds long and no larger than 200 MB. Duration is derived from the video; do not send a separate duration field.
* You may also supply up to four image\_urls and up to four elements.
* Keep the top-level prompt within 2,500 characters; longer prompts are truncated.
* elements contains Kling element IDs as decimal strings. Each ID must belong to the account making the request; arbitrary provider IDs are rejected.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/omni/video-edit \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "Change the background to a sunlit garden while preserving the subject and motion.",
    "video_urls": [
      "https://example.com/source-video.mp4"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'Change the background to a sunlit garden while preserving the '
                 'subject and motion.',
       'video_urls': ['https://example.com/source-video.mp4']}
  )
  result = higgsfield_client.subscribe(
      "kling-video/omni/video-edit",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/omni/video-edit", {
    input:
      {
        "prompt": "Change the background to a sunlit garden while preserving the subject and motion.",
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

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling Omni Playground",
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

- [Kling Omni API](/docs/models/kling-omni.md)
- [Kling Omni — Video reference API](/docs/models/kling-omni/video-reference.md)
- [Kling Omni — Image reference API](/docs/models/kling-omni/image-reference.md)
- [Kling Omni — First last frame API](/docs/models/kling-omni/first-last-frame.md)
- [Kling O3 — Video edit API](/docs/models/kling-o3/video-edit.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.