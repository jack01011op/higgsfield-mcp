> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LTX-2.5 — Text to video pro API

> Text to video pro with LTX-2.5: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← LTX-2.5](/docs/models/ltx-2-5)

**Endpoint:** `POST https://api.higgsfield.ai/lightricks/ltx-2.5/text-to-video/pro`

**Endpoint ID:** `lightricks/ltx-2.5/text-to-video/pro`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/lightricks%2Fltx-2.5%2Ftext-to-video%2Fpro/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>LTX-2.5 · Text to video pro</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* duration is marked required in the schema and has default 6; the API applies this top-level default before validation. The example includes it explicitly.
* Pro supports 720p or 1080p and 24, 25 or 50 fps. Use the Fast endpoint for 2k, 4k or 48 fps.

## Quick start

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/lightricks/ltx-2.5/text-to-video/pro \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
    "duration": 6
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.',
       'duration': 6}
  )
  result = higgsfield_client.subscribe(
      "lightricks/ltx-2.5/text-to-video/pro",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("lightricks/ltx-2.5/text-to-video/pro", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
        "duration": 6
      },
    withPolling: true,
  });

  if (result.status === "completed") {
    console.log(result.video?.url);
  }
  ```
</CodeGroup>

## Input schema

<ParamField body="fps" type="integer" default="25">
  Allowed values: `24`, `25`, `50`.
</ParamField>

<ParamField body="prompt" type="string" required>
  Write your prompt here
  Minimum characters: `2`.
  Maximum characters: `5000`.
</ParamField>

<ParamField body="duration" type="integer" required default="6">
  Requested output duration in seconds.
  Allowed values: `6`, `8`, `10`.
  The server supplies this default when the field is omitted.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output resolution tier.
  Allowed values: `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output width-to-height ratio.
  Allowed values: `"16:9"`, `"9:16"`.
</ParamField>

<ParamField body="generate_audio" type="boolean" default="true">
  Generate audio with the video.
</ParamField>

<ParamField body="camera_movement" type="string">
  Allowed values: `"dolly_in"`, `"dolly_out"`, `"dolly_left"`, `"dolly_right"`, `"jib_up"`, `"jib_down"`, `"static"`, `"focus_shift"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "LTX-2.5 Pro Text to Video Playground",
    "required": [
      "prompt",
      "duration"
    ],
    "properties": {
      "fps": {
        "enum": [
          24,
          25,
          50
        ],
        "type": "integer",
        "title": "Frames per second",
        "default": 25
      },
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "maxLength": 5000,
        "minLength": 2,
        "description": "Write your prompt here"
      },
      "duration": {
        "enum": [
          6,
          8,
          10
        ],
        "type": "integer",
        "title": "Duration",
        "default": 6
      },
      "resolution": {
        "enum": [
          "720p",
          "1080p"
        ],
        "type": "string",
        "title": "Resolution",
        "default": "720p"
      },
      "aspect_ratio": {
        "enum": [
          "16:9",
          "9:16"
        ],
        "type": "string",
        "title": "Aspect ratio",
        "default": "16:9"
      },
      "generate_audio": {
        "type": "boolean",
        "title": "Generate audio",
        "default": true
      },
      "camera_movement": {
        "enum": [
          "dolly_in",
          "dolly_out",
          "dolly_left",
          "dolly_right",
          "jib_up",
          "jib_down",
          "static",
          "focus_shift"
        ],
        "type": "string",
        "title": "Camera movement"
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

- [LTX-2.5 — Image to video pro API](/docs/models/ltx-2-5/image-to-video-pro.md)
- [LTX-2.5 — Text to video fast API](/docs/models/ltx-2-5/text-to-video-fast.md)
- [LTX-2.5 — Image to video fast API](/docs/models/ltx-2-5/image-to-video-fast.md)
- [Kling 2.6 — Pro text to video API](/docs/models/kling-2-6/pro-text-to-video.md)
- [Kling 3.0 — Pro · Text to video API](/docs/models/kling-3/pro-text-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.