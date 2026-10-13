> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 3.0 Motion Control — Pro API

> Pro with Kling 3.0 Motion Control: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Kling 3.0 Motion Control](/docs/models/kling-3-motion-control)

**Endpoint:** `POST https://api.higgsfield.ai/kling-video/v3/motion-control/pro`

**Endpoint ID:** `kling-video/v3/motion-control/pro`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/kling-video%2Fv3%2Fmotion-control%2Fpro/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Kling 3.0 Motion Control · Pro</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Use a motion-reference video from 3 to 30 seconds long. The output duration follows the source video; do not send a separate duration field.
* Use a character image up to 10 MB with each dimension between 300 and 65,536 pixels. Images outside the 0.4–2.5 width-to-height range are adjusted before generation.
* Videos larger than 100 MB are compressed before generation.
* Set character\_orientation to image or video. keep\_original\_sound uses the strings yes and no, with yes as the default.
* The example.com media URLs are placeholders. Replace them with public HTTPS URLs to your own media before submitting.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/kling-video/v3/motion-control/pro \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "image_url": "https://example.com/character.jpg",
    "video_url": "https://example.com/motion-reference.mp4"
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'image_url': 'https://example.com/character.jpg',
       'video_url': 'https://example.com/motion-reference.mp4'}
  )
  result = higgsfield_client.subscribe(
      "kling-video/v3/motion-control/pro",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("kling-video/v3/motion-control/pro", {
    input:
      {
        "image_url": "https://example.com/character.jpg",
        "video_url": "https://example.com/motion-reference.mp4"
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
  Write your prompt here
</ParamField>

<ParamField body="image_url" type="string" required>
  Public URL of the input image.
  Format: `uri`.
</ParamField>

<ParamField body="video_url" type="string" required>
  Public URL of the source video.
  Format: `uri`.
</ParamField>

<ParamField body="keep_original_sound" type="string" default="yes">
  Allowed values: `"yes"`, `"no"`.
</ParamField>

<ParamField body="character_orientation" type="string" default="video">
  Generate the orientation of the characters in the video, which can be selected to match the image or the video
  Allowed values: `"image"`, `"video"`.
</ParamField>

<Accordion title="Complete JSON schema">
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "type": "object",
    "title": "Kling V3 Motion Control Playground",
    "required": [
      "image_url",
      "video_url"
    ],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Prompt",
        "default": "",
        "description": "Write your prompt here"
      },
      "image_url": {
        "type": "string",
        "title": "Image URL",
        "format": "uri"
      },
      "video_url": {
        "type": "string",
        "title": "Video URL",
        "format": "uri"
      },
      "keep_original_sound": {
        "enum": [
          "yes",
          "no"
        ],
        "type": "string",
        "title": "Keep original sound",
        "default": "yes"
      },
      "character_orientation": {
        "enum": [
          "image",
          "video"
        ],
        "type": "string",
        "title": "Character orientation",
        "default": "video",
        "description": "Generate the orientation of the characters in the video, which can be selected to match the image or the video"
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

- [Kling 3.0 Motion Control API](/docs/models/kling-3-motion-control.md)
- [Kling 2.6 Motion Control — Pro API](/docs/models/kling-2-6-motion-control/pro.md)
- [Kling 3.0 Motion Control — Standard API](/docs/models/kling-3-motion-control/std.md)
- [Kling 2.6 Motion Control API](/docs/models/kling-2-6-motion-control.md)
- [Kling 2.6 Motion Control — Standard API](/docs/models/kling-2-6-motion-control/std.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.