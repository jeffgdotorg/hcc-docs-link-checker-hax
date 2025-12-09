# hcc-docs-link-checker-hax
Hackathon project for checking doc links for services hosted on @RedHatInsights / (HCC)

## Status
At demo time, this project is still pretty rough, but it illustrates what a common tool might look like that provides the flexibility to check docs URLs for a variety of behaviors across tenants.

### Working (by hackathon standards)
- GET method and HEAD method
- Validate HTTP response code against a specified range of allowed values
- Validate `Content-type` and `Location` response headers as a prefix match for an allowed value
- Validate body (for GET requests) for absence of a failure substring and/or presence of a success substring

### Still TODO
- Detect autoscroll suffixes on GET URLs (e.g. `https://example.com/foo#bar`) and automagically verify that a corresponding `<a name="bar">` or `<section id="bar">` when appropriate
- Detect query parms on GET URLs and handle appropriately (currently such URLs will most likely fail spectacularly)
- Convert config format from JSON to YAML
- Tighten up results format and provide flexible representation (JSON, YAML, CSV...)
- Include collection- and config-level metadata in each result
- Map snake_case to camelCase when marshaling JSON
- Refactor to be more Pythonic
