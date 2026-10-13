> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 3.0 Prime — Reference to video API

> Reference to video with Wan 3.0 Prime: request parameters, examples and response handling.

<div className="models-color-scope" aria-hidden="true" />

[← Wan 3.0 Prime](/docs/models/wan-3-prime)

**Endpoint:** `POST https://api.higgsfield.ai/alibaba/wan-3.0-prime/reference-to-video`

**Endpoint ID:** `alibaba/wan-3.0-prime/reference-to-video`

<a className="model-playground-card" href="https://console.higgsfield.ai/models/alibaba%2Fwan-3.0-prime%2Freference-to-video/playground" target="_blank" rel="noreferrer">
  <span className="model-playground-icon">▶</span>
  <span className="model-playground-copy"><span className="model-playground-title">Open API Playground</span><span>Wan 3.0 Prime · Reference to video</span></span>
  <span className="model-card-arrow">↗</span>
</a>

## Usage notes

* Reference media are optional in the stored schema: only prompt is required. The example includes an image to demonstrate reference mode.
* Send either file\_url or link\_url. A document or web-page reference automatically enables thinking; when both are sent, file\_url takes precedence.
* Reference video clips must be 1–30 seconds each and total at most 30 seconds. Reference audio must be WAV or MP3 and total at most 30 seconds, as specified in the production schema.
* The schema accepts seed=0, but the current implementation only forwards a nonzero seed.

## Quick start

Replace the example media URLs with publicly accessible URLs for your own files before submitting.

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl --request POST \
    --url https://api.higgsfield.ai/alibaba/wan-3.0-prime/reference-to-video \
    --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
    --header "Content-Type: application/json" \
    --header "Idempotency-Key: ${IDEMPOTENCY_KEY}" \
    --data '{
    "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
    "image_urls": [
      "https://example.com/input.jpg"
    ]
  }'
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import higgsfield_client

  arguments = (
      {'prompt': 'A cinematic wide shot of ocean waves at sunset, with gentle camera '
                 'movement.',
       'image_urls': ['https://example.com/input.jpg']}
  )
  result = higgsfield_client.subscribe(
      "alibaba/wan-3.0-prime/reference-to-video",
      arguments=arguments,
  )
  print(result["video"]["url"])
  ```

  ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { config, higgsfield } from "@higgsfield/client/v2";

  config({ credentials: process.env.HF_CREDENTIALS });

  const result = await higgsfield.subscribe("alibaba/wan-3.0-prime/reference-to-video", {
    input:
      {
        "prompt": "A cinematic wide shot of ocean waves at sunset, with gentle camera movement.",
        "image_urls": [
          "https://example.com/input.jpg"
        ]
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

<ParamField body="file_url" type="string">
  One document (docx/xlsx/pptx/pdf/md). Forces deep thinking.
  Format: `uri`.
</ParamField>

<ParamField body="link_url" type="string">
  One public page. Forces deep thinking. Not combinable with file\_url.
  Format: `uri`.
</ParamField>

<ParamField body="audio_urls" type="array">
  Up to 5 files, 30s total. WAV or MP3.
  Maximum items: `5`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="image_urls" type="array">
  Ordered public image reference URLs.
  Maximum items: `10`.
  Each item: string. Format: `uri`.
</ParamField>

<ParamField body="resolution" type="string" default="1080p">
  Output resolution tier.
  Allowed values: `"480p"`, `"720p"`, `"1080p"`.
</ParamField>

<ParamField body="video_urls" type="array">
  Up to 5 clips, 30s total, each 1-30s.
  Maximum items: `5`.
  Each item: string. Format: `uri`.
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
    "title": "Wan 3.0 Prime Reference to Video",
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
      "file_url": {
        "type": "string",
        "title": "Reference Document",
        "format": "uri",
        "description": "One document (docx/xlsx/pptx/pdf/md). Forces deep thinking."
      },
      "link_url": {
        "type": "string",
        "title": "Reference Web Page",
        "format": "uri",
        "description": "One public page. Forces deep thinking. Not combinable with file_url."
      },
      "audio_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "title": "Reference Audio",
        "maxItems": 5,
        "description": "Up to 5 files, 30s total. WAV or MP3."
      },
      "image_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "title": "Reference Images",
        "maxItems": 10
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
      "video_urls": {
        "type": "array",
        "items": {
          "type": "string",
          "format": "uri"
        },
        "title": "Reference Videos",
        "maxItems": 5,
        "description": "Up to 5 clips, 30s total, each 1-30s."
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
- [Wan 3.0 Prime — Text to video API](/docs/models/wan-3-prime/text-to-video.md)
- [Wan 3.0 — Reference to video API](/docs/models/wan-3/reference-to-video.md)
- [Wan 3.0 — Image to video API](/docs/models/wan-3/image-to-video.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.