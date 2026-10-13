> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 3.0 Prime — Text to video API

> Text to video with Wan 3.0 Prime: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Wan 3.0 Prime](/docs/models/wan-3-prime)

**Endpoint:** `POST https://api.higgsfield.ai/alibaba/wan-3.0-prime/text-to-video`

**Endpoint ID:** `alibaba/wan-3.0-prime/text-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/alibaba%2Fwan-3.0-prime%2Ftext-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Wan 3.0 Prime · Text to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* This endpoint generates from text; use the separate image or reference endpoint for media inputs.
* The schema accepts seed=0, but the current implementation only forwards a nonzero seed.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/alibaba/wan-3.0-prime/text-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement."
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.'}
  )
  result = higgsfield_client.subscribe(
      "alibaba/wan-3.0-prime/text-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("alibaba/wan-3.0-prime/text-to-video", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement."
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
  Minimum: `0`.
  Maximum: `2147483647`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  2-30 seconds.
  Minimum: `2`.
  Maximum: `30`.
</ParamField>

<ParamField body="resolution" type="string" default="1080p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="adaptive">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, `"9:16"`, `"adaptive"`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<ParamField body="enable_thinking" type="boolean" default="false">
  Enable model reasoning.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Wan 3.0 Prime Text to Video",
    "required": [
      "prompt"
    ],
    "properties": {
      "seed": {
        "type": "integer",
        "title": "Seed",
        "maximum": 2147483647,
        "minimum": 0
      },
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "description": "Write your prompt here"
      },
      "duration": {
        "type": "integer",
        "title": "Duration (sec)",
        "default": 5,
        "maximum": 30,
        "minimum": 2,
        "description": "2-30 seconds."
      },
      "resolution": {
        "enum": [
          "480p",
          "720p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "1080p"
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "4:3",
          "1:1",
          "3:4",
          "9:16",
          "adaptive"
        ],
        "type": "string",
        "title": "Aspect Ratio",
        "default": "adaptive"
      },
      "generate_audio": {
        "type": "boolean",
        "title": "Sound",
        "default": true
      },
      "enable_thinking": {
        "type": "boolean",
        "title": "Deep Thinking",
        "default": false
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

- [Wan 3.0 Prime API](/docs/models/wan-3-prime.md)
- [Wan 3.0 Prime — Image to video API](/docs/models/wan-3-prime/image-to-video.md)
- [Wan 3.0 Prime — Reference to video API](/docs/models/wan-3-prime/reference-to-video.md)
- [Wan 3.0 — Text to video API](/docs/models/wan-3/text-to-video.md)
- [Wan 3.0 — Image to video API](/docs/models/wan-3/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.