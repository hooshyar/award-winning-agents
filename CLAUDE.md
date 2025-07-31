# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Award-Winning Development Team Agents** system - a comprehensive Claude Code agent framework for building award-winning Flutter apps and creative web applications. The system provides 14 specialized agents with advanced MCP server integration and automated quality gates.

## Key Development Commands

### Flutter Development
```bash
# Create new Flutter project with award-winning architecture
/flutter-new [project-name]

# Implement complete Flutter feature with quality gates  
/flutter-feature [feature-name]

# Comprehensive Flutter app performance optimization
/flutter-optimize

# Run comprehensive Flutter testing suite with reporting
/flutter-test-all

# Complete Flutter app quality and security audit
/flutter-audit

# Automated Flutter app release with quality gates
/flutter-release [version]

# Platform-specific commands
/flutter-ios [task]
/flutter-android [task]
```

### Web Development
```bash
# Create award-winning creative web experiences
/web-creative [project-type]

# Build advanced UI components with design system integration
/web-component [component-name]

# Comprehensive web performance optimization
/web-optimize [optimization-type]

# Complete web application quality and compliance audit
/web-audit

# Automated web application deployment with quality gates
/web-deploy [environment]

# Progressive Web App implementation
/web-pwa [feature]
```

### Backend Consultation Commands
```bash
# Collaborative backend technology consultation
/consult --backend-strategy

# Technology stack recommendations (Firebase vs custom, SQL vs NoSQL)
/recommend --technology-stack

# Progressive architecture planning from MVP to scale
/plan --backend-architecture
```

### Quality & Security Commands
```bash
# Comprehensive security assessment
/analyze --security-audit

# Accessibility audit and implementation  
/web-accessibility [scope]

# Cross-browser testing
/test --cross-browser

# Security hardening improvements
/improve --security-hardening
```

### Workflow Optimization Commands
```bash
# Context Management
/context --restore              # Restore project context and current state
/status --comprehensive         # Multi-dimensional project status analysis
/memory --update               # Update context database with current state

# Documentation Intelligence
/docs --strategic-review       # Intelligent documentation audit and optimization
/docs --sync-update           # Cross-platform documentation synchronization  
/docs --smart-generate        # Context-aware documentation generation

# Research & Solutions
/research --solution-find     # Find current solutions for technical problems
/research --technology-eval   # In-depth technology evaluation and comparison
/research --implementation-guide # Step-by-step implementation guidance

# Strategic Testing
/test --strategic-plan        # Intelligent testing strategy development
/test --coverage-optimize     # Smart test coverage with redundancy elimination
/test --integration-design    # Cross-platform integration testing strategy

# Problem Prevention
/prevent --context-loss       # Prevent context loss between sessions
/prevent --doc-drift         # Prevent documentation inconsistency
/prevent --over-testing      # Prevent testing waste and redundancy
/prevent --research-gaps     # Prevent knowledge gaps and outdated solutions

# Emergency Recovery
/recover --project-context   # Emergency context recovery and restoration
/recover --documentation     # Emergency documentation recovery
```

## Architecture & Patterns

### Complete AI Software Engineering Team (13 Agents)

The system implements a comprehensive software engineering team with specialized workflow optimization agents to solve common Claude Code issues:

**Management Layer (2 Agents):**
- `product-manager`: Strategic planning, requirements definition, feature prioritization, stakeholder communication
- `project-manager`: Sprint planning, progress tracking, dependency management, team facilitation

**Technical Layer (7 Agents):**
- `tech-lead-architect`: System design, technology decisions, coding standards, technical leadership
- `frontend-specialist`: Web UI/UX implementation, responsive design, client-side performance optimization
- `flutter-mobile-development`: Cross-platform mobile apps, native-like experiences, mobile-specific features
- `backend-specialist`: Backend consultation, technology selection, collaborative architecture decisions
- `devops-engineer`: CI/CD pipelines, cloud infrastructure, deployment automation, monitoring
- `qa-testing-specialist`: Automated testing across web and mobile, code quality analysis, cross-platform validation
- `integration-coordinator`: Cross-agent coordination, knowledge sharing, documentation management, system integration

**Workflow Optimization Layer (4 Problem-Solving Agents):**
- `context-manager`: Project memory specialist, session continuity, context preservation across sessions
- `documentation-coordinator`: Intelligent documentation strategy, prevents over/under-documentation, maintains currency
- `research-specialist`: Web research expert, finds current solutions, validates implementation approaches
- `testing-strategy-coordinator`: Smart test coverage decisions, prevents over/under-testing, focuses on crucial features

**Enhanced Team Capabilities:**
- **Context Continuity**: Never lose project context between sessions
- **Strategic Documentation**: Right amount of docs, always current, never duplicate
- **Current Solutions**: Always research latest approaches and validate implementations
- **Smart Testing**: Strategic test coverage focused on crucial features with integration testing when needed
- **Multi-platform development**: Simultaneous web and mobile app development
- **Shared backend**: APIs designed to serve both web and mobile clients
- **Coordinated releases**: Synchronized deployment pipelines for web and mobile

### MCP Server Stack
The system integrates with 10+ MCP servers for comprehensive development support:

**Core Development:**
- `flutter-tools`: Flutter SDK integration, hot reload, mobile development
- `github`: Version control, CI/CD workflows, issue management  
- `figma`: Design system integration, design-to-code workflows
- `playwright`: E2E testing, performance monitoring, accessibility validation

**Team Collaboration:**
- `slack`: Team communication, automated notifications, workflow integration
- `linear`: Project management, issue tracking, sprint planning
- `sentry`: Error monitoring, performance tracking, debugging support

**Specialized Tools:**
- `firebase`: Backend services, authentication, analytics
- `web-fetch`: Documentation lookup, research, external content
- `apidog`: API documentation, testing, code generation

### Quality Standards Framework

**Performance Budgets:**
- **Flutter**: <2s startup, 60fps UI, <100MB memory, <50MB APK
- **Web**: >95 Lighthouse, Green Core Web Vitals, <500KB initial bundle
- **Quality**: >90% test coverage, WCAG 2.1 AA+, OWASP compliance

**Automated Quality Gates:**
1. Code Review: AI-assisted analysis with security and performance checks
2. Testing: Unit, integration, E2E, and accessibility testing
3. Security: Vulnerability scanning and compliance validation
4. Performance: Automated performance testing and monitoring
5. Accessibility: WCAG compliance verification and user testing

### Project Structure Standards

**Flutter Projects:**
```
award_flutter_app/
├── lib/
│   ├── core/           # Core utilities and constants
│   ├── features/       # Feature-based architecture
│   ├── shared/         # Shared components and services
│   └── main.dart
├── test/               # Unit and widget tests
├── integration_test/   # Integration tests
└── platform/          # Platform-specific code
```

**Web Projects:**
```
award_web_app/
├── src/
│   ├── components/     # Reusable UI components
│   ├── features/       # Feature-based modules
│   ├── services/       # API and business logic
│   ├── styles/         # Design system
│   └── utils/          # Utilities
├── tests/              # Test files
└── docs/               # Documentation
```

## Development Workflow

### Agent Auto-Activation
The 9-agent team automatically activates based on context and keywords:

**Management Layer:**
- **Product Manager**: Keywords like "product strategy", "requirements", "roadmap", "business value"
- **Project Manager**: Keywords like "sprint planning", "coordination", "timeline", "delivery"

**Technical Layer:**
- **Tech Lead Architect**: Keywords like "architecture", "system design", "technical leadership", "scalability"
- **Frontend Specialist**: Keywords like "frontend", "UI", "responsive design", "web development"
- **Flutter Mobile Development**: Keywords like "mobile", "Flutter", "iOS", "Android", "cross-platform"
- **Backend Specialist**: Keywords like "backend consultation", "database choice", "Firebase vs custom", "SQL vs NoSQL"
- **DevOps Engineer**: Keywords like "deploy", "infrastructure", "automation", "CI/CD"
- **QA/Testing Specialist**: Keywords like "testing", "quality assurance", "validation", "automation"
- **Integration Coordinator**: Keywords like "integration", "coordination", "cross-platform", "documentation"

**Workflow Optimization Layer:**
- **Context Manager**: Keywords like "where were we", "project status", "current state", "context"
- **Documentation Coordinator**: Keywords like "documentation", "README", "docs", "wiki", "update docs"
- **Research Specialist**: Keywords like "how to", "best way", "current solution", "latest", "research"
- **Testing Strategy Coordinator**: Keywords like "testing strategy", "test coverage", "crucial tests", "integration testing"

### Default Flags & Configuration
The system uses intelligent flag auto-activation:
- `--validate`: Always enabled for quality gates
- `--uc`: Auto-enabled when context usage >75%
- `--c7`: Auto-enabled for documentation and best practices
- `--magic`: Auto-enabled for UI component generation
- `--seq`: Auto-enabled for complex analysis
- `--safe-mode`: Auto-enabled for production deployments

### Quality Philosophy
**"Evidence-based excellence | User-centered design | Performance by default | Security first"**

Every agent follows award-winning standards with:
- Evidence-based decision making with metrics validation
- User experience prioritized over technical complexity
- Performance budgets built into every feature
- Security-by-design with zero-trust principles
- Accessibility-first development (WCAG 2.1 AA+ minimum)

## Environment Setup

### Required Environment Variables
```bash
# GitHub Integration
GITHUB_PAT="your_github_token"

# Design System Integration  
FIGMA_TOKEN="your_figma_token"

# Team Communication
SLACK_BOT_TOKEN="your_slack_token"
SLACK_SIGNING_SECRET="your_slack_secret"

# Error Monitoring
SENTRY_AUTH_TOKEN="your_sentry_token"
SENTRY_ORG_SLUG="your_org"

# Project Management
LINEAR_API_KEY="your_linear_key"

# API Documentation
APIDOG_API_KEY="your_apidog_key"
```

### Verification Commands
```bash
# Test Claude Code installation
claude --version

# Test MCP server connections
claude --list-servers

# Test basic functionality
claude "Hello! Which agents are available for Flutter development?"
```

## Award-Winning Standards

### What Makes This System Award-Worthy

1. **Evidence-Based Quality**: Every decision backed by metrics and testing
2. **Accessibility First**: WCAG 2.1 AA+ compliance as minimum standard  
3. **Performance by Default**: Industry-leading performance standards built-in
4. **Security Throughout**: Zero-trust security model with comprehensive auditing
5. **User-Centered Design**: User experience and accessibility prioritized
6. **Continuous Excellence**: Automated quality gates and continuous improvement

### Success Metrics
- **Performance**: >95 Lighthouse scores consistently
- **Accessibility**: >98% automated accessibility testing scores
- **Security**: Zero critical vulnerabilities in production
- **Quality**: >90% test coverage across all projects
- **User Satisfaction**: >4.8/5 user ratings and reviews

## Getting Started

1. **Setup Environment**: Configure MCP servers and environment variables
2. **Choose Your Path**: Flutter mobile development or creative web development  
3. **Start Building**: Use specialized commands for award-winning results
4. **Quality Gates**: Every feature passes comprehensive quality validation
5. **Deploy Excellence**: Automated deployment with monitoring and observability

The system is designed to help teams build applications that don't just work—they win awards through exceptional quality, performance, accessibility, and user experience.