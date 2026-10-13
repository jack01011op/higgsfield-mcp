> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

> Receive terminal generation results without continuous polling.

Pass an HTTPS endpoint in the `hf_webhook` query parameter when submitting generation. Higgsfield sends one or more HTTP `POST` deliveries after the request reaches `completed`, `failed`, or `nsfw`.

## Configure a webhook

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --request POST \
  --url "https://api.higgsfield.ai/higgsfield-ai/soul/v2/standard?hf_webhook=https%3A%2F%2Fexample.com%2Fwebhooks%2Fhiggsfield" \
  --header "Authorization: Key ${HF_API_KEY_ID}:${HF_API_KEY_SECRET}" \
  --header "Content-Type: application/json" \
  --data '{
    "prompt": "Editorial portrait in soft daylight"
  }'
```

Your endpoint must be publicly reachable over HTTPS, accept a JSON request body, and respond within ten seconds.

## Payload envelope

All deliveries use the same top-level envelope. Successful output is nested in `payload`.

<CodeGroup>
  ```json Completed image theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "request_id": "9417a243-e457-4075-895b-b68f3cda5303",
    "status": "completed",
    "error": null,
    "payload": {
      "images": [
        {
          "url": "https://cdn.example.com/generated-image.jpg",
          "content_type": "image/jpeg"
        }
      ]
    }
  }
  ```

  ```json Completed video theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "request_id": "9417a243-e457-4075-895b-b68f3cda5303",
    "status": "completed",
    "error": null,
    "payload": {
      "video": {
        "url": "https://cdn.example.com/generated-video.mp4",
        "content_type": "video/mp4"
      }
    }
  }
  ```

  ```json Failed theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "request_id": "9417a243-e457-4075-895b-b68f3cda5303",
    "status": "failed",
    "error": "Generation failed",
    "payload": null
  }
  ```

  ```json NSFW theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "request_id": "9417a243-e457-4075-895b-b68f3cda5303",
    "status": "nsfw",
    "error": null,
    "payload": null
  }
  ```
</CodeGroup>

Audio responses contain `payload.audio`. Some video and 3D operations can also include `zip`, `mov`, `jsx`, `fbx`, or `ply` artifacts.

## Delivery and retries

* Return any `2xx` response after durably recording the event.
* Network failures and `5xx` responses are retried for up to two hours.
* `4xx` responses are treated as permanent and are not retried.
* Duplicate deliveries are possible. Deduplicate by `request_id` and terminal `status`.
* If delivery fails permanently, retrieve the result through the authenticated status endpoint.

Reject request bodies that do not match the documented envelope, but acknowledge valid duplicate deliveries with `2xx`.


## Related topics

- [How the API works](/docs/how-to/introduction.md)
- [Quickstart](/docs/quickstart.md)
- [Cinema Studio 4.0 — Generate API](/docs/models/cinema-studio-4/generate.md)
- [Genjutsu — Motion transfer API](/docs/models/genjutsu/motion-transfer.md)
- [Genjutsu — Object swap API](/docs/models/genjutsu/object-swap.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.