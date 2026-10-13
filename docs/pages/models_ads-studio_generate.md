> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ads Studio — Generate ads API

> Generate ads with Ads Studio: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Ads Studio](/docs/models/ads-studio)

**Endpoint:** `POST https://api.higgsfield.ai/higgsfield/ads-studio/v1.0`

**Endpoint ID:** `higgsfield/ads-studio/v1.0`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/higgsfield%2Fads-studio%2Fv1.0/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Ads Studio · Generate ads</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Submit one request with your brief. Ad concepts are prepared automatically, then rendered as images; no separate preparation or generate call is required.
* batch\_size selects 1–8 ad concepts. Each concept produces one image, so a fully successful batch returns batch\_size images.
* Rendering uses GPT Image 2.5 Flare with fixed 2k resolution and high quality. Exact dimensions depend on aspect\_ratio. quality, resolution, renderer and fallback model are not public inputs.
* All outputs in a batch use the requested aspect\_ratio. Omitting it selects 1:1. The value auto is not supported.
* Set HF\_API\_KEY\_ID and HF\_API\_KEY\_SECRET to your API credentials. Set a unique IDEMPOTENCY\_KEY for each intended generation; reuse it only when retrying that same request.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/higgsfield/ads-studio/v1.0 \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "Create two distinct ads for a fictional herbal tea called Quiet Evening. Use a green tea tin, warm light and the headline Make time for yourself. No people.",
    "target_audience": "Busy professionals looking for a relaxing evening ritual",
    "niche": "Herbal tea",
    "language": "en",
    "aspect_ratio": "9:16",
    "batch_size": 2
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'Create two distinct ads for a fictional herbal tea called Quiet '
                 'Evening. Use a green tea tin, warm light and the headline Make '
                 'time for yourself. No people.',
       'target_audience': 'Busy professionals looking for a relaxing evening ritual',
       'niche': 'Herbal tea',
       'language': 'en',
       'aspect_ratio': '9:16',
       'batch_size': 2}
  )
  result = higgsfield_client.subscribe(
      "higgsfield/ads-studio/v1.0",
      arguments=arguments,
  )
  print(result["images"][0]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("higgsfield/ads-studio/v1.0", {
    input:
      {
        "prompt": "Create two distinct ads for a fictional herbal tea called Quiet Evening. Use a green tea tin, warm light and the headline Make time for yourself. No people.",
        "target_audience": "Busy professionals looking for a relaxing evening ritual",
        "niche": "Herbal tea",
        "language": "en",
        "aspect_ratio": "9:16",
        "batch_size": 2
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.images?.[0]?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="niche" type="string" default="">
  Optional product category or business niche used to guide ad concepts.
  Maximum characters: `1000`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Required marketing brief describing the product or service, desired message and visual direction. Must contain non-whitespace text.
  Minimum characters: `1`.
  Maximum characters: `8000`.
  Pattern: `\S`.
</ParamField>

<ParamField body="language" type="string" default="">
  Optional language guidance for ad copy, for example en or ru. This is free text, not a fixed language-code enum.
  Maximum characters: `80`.
</ParamField>

<ParamField body="batch_size" type="integer" default="1">
  Number of ad concepts and requested output images. Billing is summed across the rendered images.
  Minimum: `1`.
  Maximum: `8`.
</ParamField>

<ParamField body="image_urls" type="array" default="[]">
  Optional product or visual reference images. Supply up to 10 directly downloadable HTTP(S) URLs. Omit or send \[] for text-only generation.
  Maximum items: `10`.
  Each item: string. Minimum characters: `1`. Maximum characters: `8192`. Pattern: `^https?://`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="1:1">
  Output width-to-height ratio shared by every image in the batch.
  Allowed values: `"1:1"`, `"4:5"`, `"5:4"`, `"16:9"`, `"9:16"`, `"4:3"`, `"3:4"`, `"21:9"`, `"3:2"`, `"2:3"`, `"2:1"`, `"1:2"`, `"3:1"`, `"1:3"`.
</ParamField>

<ParamField body="target_audience" type="string" default="">
  Optional description of the intended audience, such as interests, needs or use cases.
  Maximum characters: `2000`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "required": [
      "prompt"
    ],
    "properties": {
      "niche": {
        "type": "string",
        "default": "",
        "maxLength": 1000
      },
      "prompt": {
        "type": "string",
        "pattern": "\\S",
        "maxLength": 8000,
        "minLength": 1
      },
      "language": {
        "type": "string",
        "default": "",
        "maxLength": 80
      },
      "batch_size": {
        "type": "integer",
        "default": 1,
        "maximum": 8,
        "minimum": 1
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "pattern": "^https?://",
          "maxLength": 8192,
          "minLength": 1
        },
        "default": [],
        "maxItems": 10
      },
      "aspect_ratio": {
        "enum": [
          "1:1",
          "4:5",
          "5:4",
          "16:9",
          "9:16",
          "4:3",
          "3:4",
          "21:9",
          "3:2",
          "2:3",
          "2:1",
          "1:2",
          "3:1",
          "1:3"
        ],
        "type": "string",
        "default": "1:1"
      },
      "target_audience": {
        "type": "string",
        "default": "",
        "maxLength": 2000
      }
    },
    "additionalProperties": false
  }
  ```
</Accordion>

## Product references

Omit `image_urls` for text-only generation. To guide the ad with your product, send direct image URLs that the service can download without browser cookies or custom authentication headers. An unexpired signed HTTPS URL is suitable. Keep the URLs valid while the request is being processed.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "prompt": "Create three distinct premium perfume ads. Preserve the bottle and label. Use the headline Leave a lasting note.",
  "image_urls": ["https://example.com/product.png"],
  "target_audience": "People looking for a distinctive gift",
  "niche": "Fragrance",
  "language": "en",
  "aspect_ratio": "4:5",
  "batch_size": 3
}
```

Reference images guide generation; exact preservation of a product, label or text is not guaranteed. Supported oversized references are normalized before rendering. The output remains a PNG at the selected aspect ratio.

## Pricing

**Illustrative estimate: approximately \$0.084 per image.** This is a budgeting example, not a fixed charge or maximum price. Actual cost varies with the aspect ratio, prepared prompt, reference images and measured token usage. Consult the current model pricing in the Playground before submitting work.

| Token category | USD per 1 million tokens |
| - | -: |
| Text input | \$5.00 |
| Cached text input | \$1.25 |
| Text output | \$10.00 |
| Image input | \$8.00 |
| Cached image input | \$2.00 |
| Image output | \$30.00 |

The initial charge is an estimate reconciled to actual rendering usage on completion, with standard credit rounding. Cached input is charged at the cached rate instead of being counted again as uncached input. Ad concept preparation is not billed separately.

For a batch, the final price is the **sum of the actual image charges**. Do not multiply aggregated batch token usage by `batch_size` again. Three images at the illustrative estimate would budget approximately \$0.252; the actual total can differ.

## Check request status

Use the returned `status_url` with the same API credentials. Set `REQUEST_ID` to the identifier returned when you submit the request:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --request GET \
  --url "https://api.higgsfield.ai/requests/${REQUEST_ID}/status" \
  --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}"
```

Follow the shared [polling guidance](/docs/concepts/polling). A request handle confirms acceptance, not successful image generation. Stop polling on `completed`, `failed`, `nsfw`, or `canceled`, and inspect the returned outputs and errors.

## Response

Submission returns one request handle for the entire batch:

```json Accepted theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "status": "queued",
  "request_id": "REQUEST_ID",
  "status_url": "https://api.higgsfield.ai/requests/REQUEST_ID/status",
  "cancel_url": "https://api.higgsfield.ai/requests/REQUEST_ID/cancel"
}
```

A fully successful two-image batch returns two indexed images:

```json Completed theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "request_id": "REQUEST_ID",
  "status_url": "https://api.higgsfield.ai/requests/REQUEST_ID/status",
  "cancel_url": "https://api.higgsfield.ai/requests/REQUEST_ID/cancel",
  "status": "completed",
  "images": [
    {"index": 0, "url": "https://example.com/ad-1.png"},
    {"index": 1, "url": "https://example.com/ad-2.png"}
  ],
  "errors": []
}
```

Process every returned image rather than only `images[0]`. Use its zero-based `index` to identify its batch slot and inspect `errors` for unsuccessful slots. After `subscribe` returns, extend the Python quick start with:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
for image in result.get("images", []):
    print(image["index"], image["url"])
for error in result.get("errors", []):
    print(error)
```

See [idempotent requests](/docs/concepts/idempotency), [polling](/docs/concepts/polling), [request errors](/docs/concepts/errors) and [authentication](/docs/authentication) for shared request handling.


## Related topics

- [Ads Studio API](/docs/models/ads-studio.md)
- [Cinema Studio 4.0 — Generate API](/docs/models/cinema-studio-4/generate.md)
- [Model API Reference](/docs/models.md)
- [Image Generation API](/docs/models/image-generation.md)
- [Marketing Studio Image API](/docs/models/marketing-studio-image.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.