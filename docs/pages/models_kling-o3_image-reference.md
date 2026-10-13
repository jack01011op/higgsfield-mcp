> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling O3 — Image reference API

> Image reference with Kling O3: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling O3](/docs/models/kling-o3)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/o3/image-reference`

**Endpoint ID:** `kling-video/o3/image-reference`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fo3%2Fimage-reference/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling O3 · Image reference</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Supply image\_urls for visual references. Reference images are optional in the schema.
* For a single shot, set multi\_shots to false and provide prompt. For multiple shots, set multi\_shots to true and provide 1–6 multi\_prompt objects, each containing prompt and a positive integer duration.
* Always include a non-empty top-level prompt, including when using multi\_prompt.
* Each shot prompt is limited to 512 characters. Custom-shot durations are summed for generation and billing; the top-level duration does not override that sum.
* Native audio uses sound: on or off and defaults to off.
* A multi\_prompt shot must last at least 1 second; zero-second shots are rejected even though the schema permits zero.
* When multi\_shots is true, multi\_prompt is required even with shot\_type set to intelligent.
* Keep the top-level prompt within 2,500 characters; longer prompts are truncated.
* elements contains Kling element IDs as decimal strings. Each ID must belong to the account making the request; arbitrary provider IDs are rejected.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/o3/image-reference \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A slow cinematic camera move around the subject in warm evening light.",
    "image_urls": [
      "https://example.com/reference-image.jpg"
    ],
    "multi_shots": false
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A slow cinematic camera move around the subject in warm evening '
                 'light.',
       'image_urls': ['https://example.com/reference-image.jpg'],
       'multi_shots': False}
  )
  result = higgsfield_client.subscribe(
      "kling-video/o3/image-reference",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/o3/image-reference", {
    input:
      {
        "prompt": "A slow cinematic camera move around the subject in warm evening light.",
        "image_urls": [
          "https://example.com/reference-image.jpg"
        ],
        "multi_shots": false
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="mode" type="string" default="std">
  Allowed values: `"std"`, `"pro"`, `"4k"`.
</ParamField>

<ParamField body="sound" type="string" default="off">
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

<ParamField body="shot_type" type="string" default="customize">
  Allowed values: `"customize"`, `"intelligent"`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="multi_shots" type="boolean" default="false">
  See the complete JSON schema below.
</ParamField>

<ParamField body="aspect_ratio" type="string">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`, `"1:1"`.
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
      Minimum: `0`.
      Maximum: `15`.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="last_frame_url" type="string">
  Format: `uri`.
</ParamField>

<ParamField body="first_frame_url" type="string">
  Format: `uri`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "if": {
      "properties": {
        "multi_shots": {
          "const": true
        }
      }
    },
    "else": {
      "required": [
        "prompt"
      ]
    },
    "then": {
      "required": [
        "multi_prompt"
      ]
    },
    "type": "object",
    "title": "Kling Omni Playground",
    "properties": {
      "mode": {
        "enum": [
          "std",
          "pro",
          "4k"
        ],
        "type": "string",
        "default": "std"
      },
      "sound": {
        "enum": [
          "on",
          "off"
        ],
        "type": "string",
        "default": "off"
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
      "shot_type": {
        "enum": [
          "customize",
          "intelligent"
        ],
        "type": "string",
        "default": "customize"
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "title": "Image URL",
          "format": "uri"
        }
      },
      "multi_shots": {
        "type": "boolean",
        "default": false
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16",
          "1:1"
        ],
        "type": "string"
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
              "minimum": 0
            }
          }
        },
        "maxItems": 6,
        "minItems": 1
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

- [Kling O3 API](/docs/models/kling-o3.md)
- [Kling O3 — Video reference API](/docs/models/kling-o3/video-reference.md)
- [Kling O3 — Video edit API](/docs/models/kling-o3/video-edit.md)
- [Kling O3 — First last frame API](/docs/models/kling-o3/first-last-frame.md)
- [Kling Omni — Image reference API](/docs/models/kling-omni/image-reference.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.