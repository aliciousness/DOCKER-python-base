# Copilot Instructions for DOCKER-python-base

## Project Overview

This repository maintains Docker base images for Python development environments. The images are built on official Python images with additional developer tools, zsh shell configuration, and oh-my-zsh enhancements.

**Key Technologies:**
- Docker (multi-platform: amd64, arm64)
- Python 3.11, 3.12, 3.13
- Debian-based images (Bookworm and Trixie variants)
- Zsh with oh-my-zsh, Powerlevel10k theme
- GitHub Actions for CI/CD

## Repository Structure

```
.
├── 3.11/
│   ├── bookworm/         # Full Debian Bookworm image for Python 3.11
│   └── bookworm-slim/    # Slim variant for Python 3.11
├── 3.12/
│   ├── bookworm/         # Full Debian Bookworm image for Python 3.12
│   └── bookworm-slim/    # Slim variant for Python 3.12
├── 3.13/
│   ├── trixie/           # Full Debian Trixie image for Python 3.13
│   └── trixie-slim/      # Slim variant for Python 3.13
├── scripts/
│   └── entrypoint.sh     # Container entrypoint script
└── .github/
    └── workflows/        # GitHub Actions workflows
```

## Docker Image Variants

### Python Version Support
- **Python 3.11**: bookworm, bookworm-slim
- **Python 3.12**: bookworm, bookworm-slim
- **Python 3.13**: trixie, trixie-slim

### Variant Types
- **Full images** (`bookworm`, `trixie`): Include full Debian packages
- **Slim images** (`bookworm-slim`, `trixie-slim`): Minimal footprint for production

### Latest Tag
The `latest` tag points to: `3.13-trixie-slim`

## Build and Testing

### Building Docker Images Locally

```bash
# Build a specific variant
docker build -t python-base:3.12-bookworm-slim \
  --build-arg IMAGE_VERSION=local \
  -f 3.12/bookworm-slim/Dockerfile .

# Test the image
docker run --rm -it python-base:3.12-bookworm-slim zsh
```

### Testing the Entrypoint Script

```bash
# Test with RECREATE_REQUIREMENTS
docker run --rm \
  -e RECREATE_REQUIREMENTS=true \
  -e KEEP_ALIVE=false \
  python-base:3.12-bookworm-slim

# Test with custom command
docker run --rm \
  -e KEEP_ALIVE=false \
  python-base:3.12-bookworm-slim \
  python --version
```

## Dockerfile Guidelines

### Structure
Each Dockerfile follows this pattern:
1. Base FROM statement with official Python image
2. Metadata (LABEL, ARG, ENV)
3. System package installation
4. CA certificate setup
5. Zsh and oh-my-zsh installation
6. Entrypoint script setup

### Key Features in Images
- **Timezone**: Set to UTC by default
- **Shell**: Zsh with oh-my-zsh and Powerlevel10k theme
- **Plugins**: zsh-syntax-highlighting pre-installed
- **Tools**: curl, git, vim, wget, nmap, iputils-ping
- **Development**: gcc, libc6-dev, libpq-dev for building Python packages
- **Entrypoint**: Custom script that handles requirements.txt generation and container lifecycle

## Coding Standards

### Dockerfile Best Practices
- Use multi-stage builds where beneficial
- Minimize layers by combining RUN commands
- Clean apt cache to reduce image size
- Pin versions for reproducible builds when critical
- Use `--no-install-recommends` flag with apt-get
- Set `DEBIAN_FRONTEND=noninteractive` to avoid interactive prompts

### Shell Scripts
- Use POSIX-compliant shell syntax (`#!/bin/sh`)
- Include descriptive comments
- Validate environment variables before use
- Provide clear error messages

### Entrypoint Script
- The entrypoint script at `scripts/entrypoint.sh` provides:
  - Optional requirements.txt generation via `RECREATE_REQUIREMENTS` env var
  - Command execution support via `"$@"`
  - Keep-alive functionality via `KEEP_ALIVE` env var

## GitHub Actions Workflows

### Release Workflow (`release.yml`)
Triggered on GitHub release creation:
- Builds all Python version and variant combinations
- Pushes multi-platform images (amd64, arm64) to Docker Hub
- Tags images appropriately based on version and variant
- Uses matrix strategy to build all combinations in parallel
- Triggers badge update workflow after completion

### Excluded Combinations
Matrix excludes invalid combinations:
- Python 3.11: No trixie variants (only bookworm)
- Python 3.12: No trixie variants (only bookworm)
- Python 3.13: No bookworm variants (only trixie)

### Secrets Required
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_TOKEN`: Docker Hub access token
- `WORKFLOW_PAT`: GitHub PAT for triggering other workflows

## Image Tagging Strategy

Each release creates multiple tags:
- Version + variant: `v0.3.6-3.12-bookworm-slim`
- Variant tag: `3.12` (for slim) or `3.12-debian` (for full)
- Version tag: `v0.3.6` (for latest variant only)
- `latest` tag (for latest variant only)

## Making Changes

### Adding a New Python Version
1. Create directory structure: `<version>/<variant>/Dockerfile`
2. Copy and adapt Dockerfile from similar variant
3. Update `release.yml` workflow matrix:
   - Add version to `python-version` matrix
   - Add appropriate exclude rules
   - Update `LATEST` env var if this becomes the new latest

### Modifying the Entrypoint
1. Edit `scripts/entrypoint.sh`
2. Ensure POSIX compatibility (test with `/bin/sh`)
3. Document any new environment variables in Dockerfiles and README
4. Test with both `KEEP_ALIVE=true` and `KEEP_ALIVE=false`

### Updating Base Images
When updating Python or Debian versions:
1. Update FROM statements in Dockerfiles
2. Test that all tools still install correctly
3. Verify oh-my-zsh and plugins work
4. Check CA certificate installation
5. Test entrypoint script functionality

## Copilot Agent Guidelines

### When Modifying Dockerfiles
- Always maintain consistency across all variants
- If changing one Dockerfile, consider if other variants need the same change
- Test locally before committing
- Ensure changes don't significantly increase image size
- Verify multi-platform builds work (amd64 and arm64)

### When Working with Workflows
- Use matrix strategy for parallel builds
- Maintain the exclude rules carefully
- Test workflow changes with workflow_dispatch when possible
- Be cautious with secrets - never log or expose them

### Documentation Updates
- Update README.md when adding features or changing behavior
- Keep version tags in README.md synchronized with actual releases
- Document any new environment variables or build arguments

### Security Considerations
- Keep base images updated
- Review any new packages being installed
- Validate CA certificate URLs before use
- Don't add unnecessary tools that increase attack surface

## Common Tasks

### Test a Dockerfile change locally
```bash
docker build -t test-image -f 3.12/bookworm-slim/Dockerfile .
docker run --rm -it test-image zsh -c "python --version && which zsh"
```

### Validate entrypoint changes
```bash
docker run --rm -e RECREATE_REQUIREMENTS=true -e KEEP_ALIVE=false \
  -v $(pwd):/test test-image
```

### Check image size
```bash
docker images | grep python-base
```

## Helpful Commands

```bash
# List all Dockerfiles
find . -name "Dockerfile" -type f

# Check shell script syntax
shellcheck scripts/entrypoint.sh

# View Docker image layers
docker history python-base:latest

# Test multi-platform build (requires buildx)
docker buildx build --platform linux/amd64,linux/arm64 \
  -f 3.12/bookworm-slim/Dockerfile .
```

## Repository Conventions

- Keep all Dockerfiles as similar as possible, differing only in base image
- Use consistent formatting and ordering in Dockerfiles
- Maintain the same set of tools across all variants
- Keep entrypoint.sh simple and focused
- Test changes locally before pushing
- Update documentation alongside code changes
