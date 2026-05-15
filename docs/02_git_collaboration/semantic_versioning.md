# Semantic Versioning (SemVer)

When delivering software, especially libraries or APIs consumed by other teams, communicating the nature of changes in a release is critical. **Semantic Versioning (SemVer)** is the industry standard for version numbers.

## Format: MAJOR.MINOR.PATCH

A version number is composed of three digits separated by dots: `v1.2.3`

1. **MAJOR version** (`1.x.x`): Incremented when you make **incompatible API changes** or breaking changes. If a user upgrades a major version, they will likely need to change their own code.
2. **MINOR version** (`x.2.x`): Incremented when you **add functionality in a backward-compatible manner**. A user can upgrade a minor version without their code breaking.
3. **PATCH version** (`x.x.3`): Incremented when you make **backward-compatible bug fixes**. 

## Pre-releases and Build Metadata

SemVer also supports pre-release tags and build metadata.
- **Pre-release**: Indicated by appending a hyphen and a series of dot-separated identifiers. Examples: `v1.0.0-alpha`, `v1.0.0-beta.1`, `v1.0.0-rc.1` (Release Candidate). Pre-releases have a lower precedence than the associated normal version.
- **Build Metadata**: Indicated by appending a plus sign and identifiers. Example: `v1.0.0+20130313144700`.

## Initial Development Phase

Version `0.x.y` is considered the initial development phase. Anything MAY change at any time. The public API should not be considered stable.
- `0.1.0` is usually the first public release.
- When you are ready for the API to be considered stable and locked, you release `1.0.0`.

## Why is SemVer important for DevOps?
In CI/CD pipelines, package managers (like `npm`, `pip`, `maven`) rely heavily on SemVer to automatically resolve dependencies. If you configure a package manager to accept `^1.2.0`, it will automatically download any `1.x.x` update, but will stop before `2.0.0` to protect you from breaking changes. Violating SemVer guarantees will break users' CI pipelines.
