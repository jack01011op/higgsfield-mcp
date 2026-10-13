> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Genjutsu — Object swap API

> Object swap with Genjutsu: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Genjutsu](/docs/models/genjutsu)

**Endpoint:** `POST https://api.higgsfield.ai/higgsfield/genjutsu/object-swap/v1.0`

**Endpoint ID:** `higgsfield/genjutsu/object-swap/v1.0`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/higgsfield%2Fgenjutsu%2Fobject-swap%2Fv1.0/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Genjutsu · Object swap</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Use higgsfield/genjutsu/object-swap/v1.0 for new integrations. The legacy endpoint higgsfiled/genjutsu/object-swap/v1.0 remains callable for existing clients but is hidden from model discovery.
* The source video must be at least 4 seconds. Videos longer than 30 seconds are trimmed to 30 seconds; output duration follows the prepared source video.
* Provide 1–8 image references. The prompt is optional and defaults to an empty string.
* The source video must contain at least 409,600 pixels per frame (width × height).

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/higgsfield/genjutsu/object-swap/v1.0 \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "video_url": "https://example.com/input.mp4",
    "image_urls": [
      "https://example.com/input.jpg"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'video_url': 'https://example.com/input.mp4',
       'image_urls': ['https://example.com/input.jpg']}
  )
  result = higgsfield_client.subscribe(
      "higgsfield/genjutsu/object-swap/v1.0",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("higgsfield/genjutsu/object-swap/v1.0", {
    input:
      {
        "video_url": "https://example.com/input.mp4",
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

<ParamField body="prompt" type="string" default="">
  Text instructions for the generation or edit.
  Maximum characters: `10000`.
</ParamField>

<ParamField body="video_url" type="string" required>
  Public URL of the source video.
  Minimum characters: `1`.
  Maximum characters: `2083`.
  Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array" required>
  Ordered public image reference URLs.
  Minimum items: `1`.
  Maximum items: `8`.
  Each item: string. Minimum characters: `1`. Maximum characters: `2083`. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"480p"`, `"1080p"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "ObjectSwapParams",
    "required": [
      "video_url",
      "image_urls"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "default": "",
        "maxLength": 10000
      },
      "video_url": {
        "type": "string",
        "title": "Video Url",
        "format": "uri",
        "maxLength": 2083,
        "minLength": 1
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri",
          "maxLength": 2083,
          "minLength": 1
        },
        "title": "Image Urls",
        "maxItems": 8,
        "minItems": 1
      },
      "resolution": {
        "enum": [
          "720p",
          "480p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "720p"
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

- [Genjutsu API](/docs/models/genjutsu.md)
- [Genjutsu — Restyle API](/docs/models/genjutsu/restyle.md)
- [Genjutsu — Motion transfer API](/docs/models/genjutsu/motion-transfer.md)
- [Model API Reference](/docs/models.md)
- [Higgsfield API](/docs/index.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.