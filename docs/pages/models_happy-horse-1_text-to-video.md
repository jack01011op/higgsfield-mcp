> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Happy Horse 1.0 — Text to video API

> Text to video with Happy Horse 1.0: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Happy Horse 1.0](/docs/models/happy-horse-1)

**Endpoint:** `POST https://api.higgsfield.ai/alibaba/happy-horse/text-to-video`

**Endpoint ID:** `alibaba/happy-horse/text-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/alibaba%2Fhappy-horse%2Ftext-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Happy Horse 1.0 · Text to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* The prompt must contain text; an empty string is rejected during submission.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/alibaba/happy-horse/text-to-video \
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
      "alibaba/happy-horse/text-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("alibaba/happy-horse/text-to-video", {
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
  Minimum: `1`.
  Maximum: `2147483646`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Write your prompt here
</ParamField>

<ParamField body="duration" type="integer" default="5">
  Requested output duration in seconds.
  Minimum: `3`.
  Maximum: `15`.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Happy Horse",
    "required": [
      "prompt"
    ],
    "properties": {
      "seed": {
        "type": "integer",
        "maximum": 2147483646,
        "minimum": 1
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
      "resolution": {
        "enum": [
          "720p",
          "1080p"
        ],
        "type": "string",
        "default": "720p"
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16",
          "1:1",
          "4:3",
          "3:4"
        ],
        "type": "string",
        "title": "Aspect Ratio",
        "default": "16:9"
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

- [Happy Horse 1.0 API](/docs/models/happy-horse-1.md)
- [Happy Horse 1.0 — Image to video API](/docs/models/happy-horse-1/image-to-video.md)
- [Happy Horse 1.0 — Reference to video API](/docs/models/happy-horse-1/reference-to-video.md)
- [HappyHorse 1.1 — Text to video API](/docs/models/happy-horse-1-1/text-to-video.md)
- [HappyHorse 1.1 — Image to video API](/docs/models/happy-horse-1-1/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.