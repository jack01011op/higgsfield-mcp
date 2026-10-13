> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SOUL Cinema — Text to image API

> Text to image with SOUL Cinema: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← SOUL Cinema](/docs/models/soul-cinema)

**Endpoint:** `POST https://api.higgsfield.ai/higgsfield-ai/soul/cinema`

**Endpoint ID:** `higgsfield-ai/soul/cinema`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/higgsfield-ai%2Fsoul%2Fcinema/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>SOUL Cinema · Text to image</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* batch\_size is 1 or 4 only. A custom\_reference\_id must belong to the calling account and have completed training.
* aspect\_ratio defaults to 1:1 and enhance\_prompt defaults to false. seed defaults to a random integer from 1 to 1000000; explicit null is invalid.
* Providing a custom\_reference\_id enables prompt enhancement for the character reference, even if enhance\_prompt is false.
* Cinema uses a fixed style; client-supplied style\_id is ignored.
* This model may be absent from model discovery; authorized requests can use the endpoint ID directly.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/higgsfield-ai/soul/cinema \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A ceramic vase on a wooden table beside a sunlit window, soft natural shadows, editorial photograph.",
    "resolution": "720p",
    "aspect_ratio": "1:1",
    "enhance_prompt": true,
    "batch_size": 1
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A ceramic vase on a wooden table beside a sunlit window, soft '
                 'natural shadows, editorial photograph.',
       'resolution': '720p',
       'aspect_ratio': '1:1',
       'enhance_prompt': True,
       'batch_size': 1}
  )
  result = higgsfield_client.subscribe(
      "higgsfield-ai/soul/cinema",
      arguments=arguments,
  )
  print(result["images"][0]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("higgsfield-ai/soul/cinema", {
    input:
      {
        "prompt": "A ceramic vase on a wooden table beside a sunlit window, soft natural shadows, editorial photograph.",
        "resolution": "720p",
        "aspect_ratio": "1:1",
        "enhance_prompt": true,
        "batch_size": 1
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.images?.[0]?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="prompt" type="string" required>
  Text instructions for the generation or edit.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="1:1">
  Output width-to-height ratio.
  Allowed values: `"9:16"`, `"16:9"`, `"4:3"`, `"3:4"`, `"1:1"`, `"2:3"`, `"3:2"`.
</ParamField>

<ParamField body="enhance_prompt" type="boolean" default="false">
  Enable prompt enhancement. Providing custom\_reference\_id enables enhancement even when this field is false.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="custom_reference_id" type="string | null">
  Identifier of a completed character reference owned by your account.
  Format: `uuid`.
  Omit this field to use the server default; `null` is accepted only when included in the field type.
</ParamField>

<ParamField body="custom_reference_strength" type="number" default="1.0">
  Strength of the character reference.
  Minimum: `0`.
  Maximum: `1`.
</ParamField>

<ParamField body="seed" type="integer">
  Seed used to control generation randomness.
  Minimum: `1`.
  Maximum: `1000000`.
</ParamField>

<ParamField body="batch_size" type="integer" default="1">
  Number of output images.
  Allowed values: `1`, `4`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "properties": {
      "prompt": {
        "title": "Prompt",
        "type": "string"
      },
      "aspect_ratio": {
        "default": "1:1",
        "enum": [
          "9:16",
          "16:9",
          "4:3",
          "3:4",
          "1:1",
          "2:3",
          "3:2"
        ],
        "title": "Aspect Ratio",
        "type": "string"
      },
      "enhance_prompt": {
        "default": false,
        "title": "Enhance Prompt",
        "type": "boolean"
      },
      "resolution": {
        "default": "720p",
        "enum": [
          "720p",
          "1080p"
        ],
        "title": "Resolution",
        "type": "string"
      },
      "custom_reference_id": {
        "anyOf": [
          {
            "format": "uuid",
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "default": null,
        "title": "Custom Reference Id"
      },
      "custom_reference_strength": {
        "default": 1.0,
        "maximum": 1,
        "minimum": 0,
        "title": "Custom Reference Strength",
        "type": "number"
      },
      "seed": {
        "maximum": 1000000,
        "minimum": 1,
        "title": "Seed",
        "type": "integer"
      },
      "batch_size": {
        "default": 1,
        "enum": [
          1,
          4
        ],
        "title": "Batch Size",
        "type": "integer"
      }
    },
    "required": [
      "prompt"
    ],
    "title": "SoulCinemaParamsSchema",
    "type": "object"
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

- [SOUL Cinema API](/docs/models/soul-cinema.md)
- [SOUL — Text to image API](/docs/models/soul-standard/generate.md)
- [SOUL V2 — Text to image API](/docs/models/soul-2/generate.md)
- [Qwen Image 3 — Text to image API](/docs/models/qwen-image-3/text-to-image.md)
- [Recraft V4.1 — Text to image API](/docs/models/recraft-v4-1/text-to-image.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.