# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Security Considerations for 3D CAD / STL Parsing

`cad-mesh-analyzer` parses untrusted 3D geometry files (ASCII/Binary STL, STEP, IGES). To support OpenAI Codex Security guidelines and maintain memory safety:

1. **Memory Safety & Bounds Checking:** All file parsing enforces strict memory limits and header size checks to prevent buffer overflow vulnerabilities when processing large CAD assemblies.
2. **Untrusted Input Handling:** Malformed STL headers or unexpected binary byte counts trigger safe validation errors rather than crash conditions.
3. **Reporting a Vulnerability:** Please report security vulnerabilities via GitHub Security Advisories or by emailing the maintainer directly.
