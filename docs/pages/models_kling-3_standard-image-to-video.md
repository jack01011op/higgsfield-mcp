> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 3.0 — Standard · Image to video API

> Standard · Image to video with Kling 3.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling 3.0](/docs/models/kling-3)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/v3.0/std/image-to-video`

**Endpoint ID:** `kling-video/v3.0/std/image-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fv3.0%2Fstd%2Fimage-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling 3.0 · Standard · Image to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* image\_url is the first frame; last\_image\_url optionally sets the final frame.
* Always include a non-empty top-level prompt, including when using multi\_prompt. Keep it within 2,500 characters; longer prompts are truncated.
* For custom shots, set multi\_shots to true and provide 1–6 multi\_prompt objects. Each object needs prompt (at most 512 characters) and duration (a positive integer from 1 to 15 seconds).
* Custom-shot durations are summed for generation and billing; the top-level duration does not override that sum. With multi\_shots enabled and no custom shots, the top-level duration is retained.
* Native audio uses sound: on or off and defaults to on.
* elements contains Kling element IDs as decimal strings. Each ID must belong to the account making the request; arbitrary provider IDs are rejected.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/v3.0/std/image-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A slow cinematic tracking shot along a sunlit coastal road.",
    "image_url": "https://example.com/first-frame.jpg"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A slow cinematic tracking shot along a sunlit coastal road.',
       'image_url': 'https://example.com/first-frame.jpg'}
  )
  result = higgsfield_client.subscribe(
      "kling-video/v3.0/std/image-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/v3.0/std/image-to-video", {
    input:
      {
        "prompt": "A slow cinematic tracking shot along a sunlit coastal road.",
        "image_url": "https://example.com/first-frame.jpg"
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="sound" type="string" default="on">
  Enable sound for the output video.
  Allowed values: `"on"`, `"off"`.
</ParamField>

<ParamField body="prompt" type="string">
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `3`.
  Maximum: `15`.
</ParamField>

<ParamField body="elements" type="array">
  Each item: string.
</ParamField>

<ParamField body="cfg_scale" type="number" default="0.5">
  Minimum: `0`.
  Maximum: `1`.
  Multiple of: `0.01`.
</ParamField>

<ParamField body="image_url" type="string" required>
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="multi_shots" type="boolean" default="false">
  See the complete JSON schema below.
</ParamField>

<ParamField body="multi_prompt" type="array">
  Minimum items: `1`.
  Maximum items: `6`.

  <Expandable title="Nested fields">
    <ParamField body="multi_prompt[].prompt" type="string">
      Text instructions for the generation or edit.
      Maximum characters: `512`.
    </ParamField>

    <ParamField body="multi_prompt[].duration" type="integer">
      Requested output duration in seconds.
      Minimum: `1`.
      Maximum: `15`.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="last_image_url" type="string">
  Format: `uri`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling 3.0 Playground",
    "required": [
      "image_url"
    ],
    "properties": {
      "sound": {
        "enum": [
          "on",
          "off"
        ],
        "type": "string",
        "title": "Generate sound",
        "default": "on"
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
        "minimum": 3
      },
      "elements": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "cfg_scale": {
        "type": "number",
        "title": "CFG Scale",
        "default": 0.5,
        "maximum": 1,
        "minimum": 0,
        "multipleOf": 0.01
      },
      "image_url": {
        "type": "string",
        "title": "Image URL",
        "format": "uri"
      },
      "multi_shots": {
        "type": "boolean",
        "default": false
      },
      "multi_prompt": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string",
              "maxLength": 512
            },
            "duration": {
              "type": "integer",
              "maximum": 15,
              "minimum": 1
            }
          }
        },
        "maxItems": 6,
        "minItems": 1
      },
      "last_image_url": {
        "type": "string",
        "title": "Image URL",
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

- [Kling 3.0 Motion Control — Standard API](/docs/models/kling-3-motion-control/std.md)
- [Kling 3.0 — Standard · Text to video API](/docs/models/kling-3/standard-text-to-video.md)
- [Kling 2.5 Turbo — Standard image to video API](/docs/models/kling-2-5-turbo/standard-image-to-video.md)
- [Kling 3.0 — Turbo · Image to video API](/docs/models/kling-3/turbo-image-to-video.md)
- [Kling 3.0 — 4K · Image to video API](/docs/models/kling-3/4k-image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.