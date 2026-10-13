> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax H3 — Text to video API

> Text to video with MiniMax H3: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← MiniMax H3](/docs/models/minimax-h3)

**Endpoint:** `POST https://api.higgsfield.ai/minimax/h3/text-to-video`

**Endpoint ID:** `minimax/h3/text-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/minimax%2Fh3%2Ftext-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>MiniMax H3 · Text to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Resolution is fixed to the case-sensitive schema value "2K". The prompt must contain non-whitespace text; the current provider serializer uses only its first 7,000 characters.
* For text-only requests, aspect\_ratio="auto" or "adaptive" resolves to 16:9.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/minimax/h3/text-to-video \
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
      "minimax/h3/text-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("minimax/h3/text-to-video", {
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

<ParamField body="prompt" type="string" required>
  Write your prompt here
  Minimum characters: `1`.
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `5`.
  Maximum: `15`.
</ParamField>

<ParamField body="resolution" type="string" default="2K">
  Output resolution tier.
  Allowed values: `"2K"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="auto">
  Output width-to-height ratio.
  Allowed values: `"auto"`, `"adaptive"`, `"21:9"`, `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, `"9:16"`.
</ParamField>

<ParamField body="aigc_watermark" type="boolean" default="false">
  See the complete JSON schema below.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "MiniMax H3 Text to Video Playground",
    "required": [
      "prompt"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "minLength": 1,
        "description": "Write your prompt here"
      },
      "duration": {
        "type": "integer",
        "title": "Duration",
        "default": 5,
        "maximum": 15,
        "minimum": 5
      },
      "resolution": {
        "enum": [
          "2K"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "2K"
      },
      "aspect_ratio": {
        "enum": [
          "auto",
          "adaptive",
          "21:9",
          "16:9",
          "4:3",
          "1:1",
          "3:4",
          "9:16"
        ],
        "type": "string",
        "title": "Aspect ratio",
        "default": "auto"
      },
      "aigc_watermark": {
        "type": "boolean",
        "title": "AIGC watermark",
        "default": false
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

- [MiniMax H3 API](/docs/models/minimax-h3.md)
- [MiniMax H3 — Image to video API](/docs/models/minimax-h3/image-to-video.md)
- [MiniMax H3 — Reference to video API](/docs/models/minimax-h3/reference-to-video.md)
- [Video Generation API](/docs/models/video-generation.md)
- [Model API Reference](/docs/models.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.