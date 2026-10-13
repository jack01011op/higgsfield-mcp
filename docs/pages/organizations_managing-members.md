> ## Documentation Index
> Fetch the complete documentation index at: https://docs.higgsfield.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing members

> Invite members and manage access to your Higgsfield organization.

Organization administrators manage membership from the organization settings in the Higgsfield API dashboard.

## Open organization settings

1. Sign in to the [Higgsfield API dashboard](https://console.higgsfield.ai).
2. Select the organization from the account switcher.
3. Open **Organization settings**.

## Roles

| Role | Access |
| - | - |
| Admin | Manages organization settings and members. |
| Member | Uses the organization workspace without member-management access. |

## Enterprise SSO

Enterprise SSO lets organization members authenticate through your identity provider. SSO configuration is available to organization members with the **Manage SSO** permission.

### Supported identity providers

| Provider | Connection type |
| - | - |
| Okta | SAML |
| Microsoft | SAML |
| Custom provider | Custom SAML |

### Configure a SAML connection

1. Select your organization in the [Higgsfield API dashboard](https://console.higgsfield.ai).
2. Open **Enterprise SSO** and select **Create SAML Connection**.
3. Enter a connection name and the domains that should use SSO.
4. Select your identity provider.
5. Add the Higgsfield **ACS URL** and **Entity ID** to your identity provider.
6. Enter your identity provider metadata or its SSO URL, entity ID, and certificate.
7. Review the attribute mapping, save the connection, and activate it.

Authorized organization members can edit, activate, deactivate, or delete existing SAML connections.

<Note>
  SSO settings are scoped to the currently selected organization.
</Note>


## Related topics

- [Organizations](/docs/organizations.md)
- [Support](/docs/help/support.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.