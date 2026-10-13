> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z-Image Turbo — Generate API

> Generate with Z-Image Turbo: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Z-Image Turbo](/docs/models/z-image-turbo)

**Endpoint:** `POST https://api.higgsfield.ai/z-image/turbo`

**Endpoint ID:** `z-image/turbo`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/z-image%2Fturbo/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Z-Image Turbo · Generate</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Text-to-image only. prompt must contain non-whitespace text and at most 800 characters.
* prompt\_extend defaults to false; enabling it uses the enhanced pricing tier.
* The schema accepts 1k and 2k tiers, ten aspect ratios, and an optional integer seed from 0 to 2147483647.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/z-image/turbo \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A ceramic vase on a wooden table beside a sunlit window, soft natural shadows, editorial photograph.",
    "resolution": "1k",
    "aspect_ratio": "1:1",
    "prompt_extend": false
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A ceramic vase on a wooden table beside a sunlit window, soft '
                 'natural shadows, editorial photograph.',
       'resolution': '1k',
       'aspect_ratio': '1:1',
       'prompt_extend': False}
  )
  result = higgsfield_client.subscribe(
      "z-image/turbo",
      arguments=arguments,
  )
  print(result["images"][0]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("z-image/turbo", {
    input:
      {
        "prompt": "A ceramic vase on a wooden table beside a sunlit window, soft natural shadows, editorial photograph.",
        "resolution": "1k",
        "aspect_ratio": "1:1",
        "prompt_extend": false
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.images?.[0]?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="seed" type="integer">
  Optional random seed for similar, reproducible results.
  Minimum: `0`.
  Maximum: `2147483647`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Positive prompt describing the desired content, style, and composition.
  Minimum characters: `1`.
  Maximum characters: `800`.
</ParamField>

<ParamField body="resolution" type="string" default="1k">
  Output resolution tier. Both tiers produce PNG images.
  Allowed values: `"1k"`, `"2k"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="1:1">
  Output aspect ratio. Exact provider-recommended dimensions are selected automatically.
  Allowed values: `"1:1"`, `"2:3"`, `"3:2"`, `"3:4"`, `"4:3"`, `"7:9"`, `"9:7"`, `"9:16"`, `"16:9"`, `"21:9"`.
</ParamField>

<ParamField body="prompt_extend" type="boolean" default="false">
  Rewrite and reason over the prompt before generation; this uses the enhanced price tier.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Z-Image Turbo",
    "required": [
      "prompt"
    ],
    "properties": {
      "seed": {
        "type": "integer",
        "maximum": 2147483647,
        "minimum": 0,
        "description": "Optional random seed for similar, reproducible results."
      },
      "prompt": {
        "type": "string",
        "maxLength": 800,
        "minLength": 1,
        "description": "Positive prompt describing the desired content, style, and composition."
      },
      "resolution": {
        "enum": [
          "1k",
          "2k"
        ],
        "type": "string",
        "default": "1k",
        "description": "Output resolution tier. Both tiers produce PNG images."
      },
      "aspect_ratio": {
        "enum": [
          "1:1",
          "2:3",
          "3:2",
          "3:4",
          "4:3",
          "7:9",
          "9:7",
          "9:16",
          "16:9",
          "21:9"
        ],
        "type": "string",
        "default": "1:1",
        "description": "Output aspect ratio. Exact provider-recommended dimensions are selected automatically."
      },
      "prompt_extend": {
        "type": "boolean",
        "default": false,
        "description": "Rewrite and reason over the prompt before generation; this uses the enhanced price tier."
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
  "images": [
    {
      "url": "https://example.com/output.png"
    }
  ]
}
```

See [idempotent requests](/docs/concepts/idempotency), [polling](/docs/concepts/polling), [request errors](/docs/concepts/errors) and [authentication](/docs/authentication) for shared request handling.


## Related topics

- [Z-Image Turbo API](/docs/models/z-image-turbo.md)
- [Kling 3.0 — Turbo · Image to video API](/docs/models/kling-3/turbo-image-to-video.md)
- [Kling 2.5 Turbo — Pro image to video API](/docs/models/kling-2-5-turbo/pro-image-to-video.md)
- [Kling 2.5 Turbo — Standard image to video API](/docs/models/kling-2-5-turbo/standard-image-to-video.md)
- [Grok Image 2.0 — Generate and edit API](/docs/models/grok-image-2/generate-and-edit.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.