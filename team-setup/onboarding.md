# Award-Winning Development Team Onboarding

Welcome to the award-winning development team! This guide will help you set up your environment and understand our development philosophy.

## Team Philosophy

**"Evidence-based excellence | User-centered design | Performance by default | Security first"**

We build applications that win awards by maintaining the highest standards in:
- **Performance**: >95 Lighthouse scores, 60fps animations, <2s load times
- **Accessibility**: WCAG 2.1 AA+ compliance as minimum standard
- **Security**: OWASP best practices, zero-trust architecture
- **Quality**: >90% test coverage, comprehensive code reviews

## Quick Start Setup

### 1. Install Claude Code

```bash
# Install Claude Code CLI
curl -fsSL https://claude.ai/install.sh | sh

# Verify installation
claude --version
```

### 2. Clone Team Agents Repository

```bash
# Clone the team agents configuration
git clone https://github.com/your-org/award-winning-agents.git
cd award-winning-agents

# Copy configuration to your Claude directory
cp -r .claude/* ~/.claude/
cp .mcp.json ~/.claude/
```

### 3. Setup Environment Variables

Create `.env` file with required MCP server credentials:

```bash
# GitHub Integration
export GITHUB_PAT="your_github_personal_access_token"

# Figma Integration (for design system work)
export FIGMA_TOKEN="your_figma_api_token"

# Team Communication
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_SIGNING_SECRET="your_slack_signing_secret"

# Error Monitoring
export SENTRY_AUTH_TOKEN="your_sentry_auth_token"
export SENTRY_ORG_SLUG="your_sentry_org"

# Project Management
export LINEAR_API_KEY="your_linear_api_key"

# API Documentation
export APIDOG_API_KEY="your_apidog_api_key"
```

### 4. Verify MCP Server Setup

```bash
# Test MCP server connections
claude --list-servers

# Test GitHub integration
claude "Check my recent GitHub activity"

# Test Flutter tools (if doing mobile development)
claude "/flutter-test-all"
```

## Agent Specializations

Our team uses specialized Claude Code agents for different roles:

### Flutter Development Team
- **Flutter Architect**: System design, performance optimization, scalability
- **Flutter Senior**: Feature implementation, code review, quality assurance
- **Flutter UI/UX**: Design system implementation, user experience
- **Flutter Testing**: QA, automated testing, CI/CD optimization
- **Flutter Platform**: Native integrations, platform-specific features

### Web Development Team
- **Web Architect**: Frontend architecture, performance, scalability
- **Web Fullstack**: Full-stack development, API design, database optimization
- **Web Creative**: Award-winning design, animations, creative experiences
- **Web Performance**: Core Web Vitals, optimization, monitoring
- **Web Accessibility**: WCAG compliance, inclusive design

### Cross-Platform Specialists
- **DevOps Engineer**: CI/CD, deployment, infrastructure automation
- **Security Specialist**: Security audits, compliance, threat modeling
- **Product Manager**: Requirements, roadmap, quality gates
- **Technical Writer**: Documentation, knowledge transfer, guides

## Development Workflow

### Daily Workflow
1. **Morning Standup**: AI-powered status via Slack integration
2. **Feature Development**: Context-aware agents with quality gates
3. **Code Review**: Automated security and performance analysis
4. **Testing**: Comprehensive E2E testing with Playwright
5. **Deployment**: Zero-downtime deployments with monitoring

### Quality Gates
Every feature must pass:
- **Code Review**: Peer review with AI-assisted analysis
- **Security Scan**: Automated vulnerability assessment
- **Performance Test**: Lighthouse >95, Core Web Vitals green
- **Accessibility Audit**: WCAG 2.1 AA+ compliance
- **Cross-Browser Test**: Chrome, Firefox, Safari, Edge compatibility

### Command Examples

```bash
# Flutter development
claude "/flutter-new award_app"
claude "/flutter-feature user_authentication"
claude "/flutter-optimize"
claude "/flutter-test-all"
claude "/flutter-release 1.0.0"

# Web development
claude "/web-creative portfolio"
claude "/web-component navigation"
claude "/web-optimize performance"
claude "/web-audit"
claude "/web-deploy production"

# Quality assurance
claude "/analyze --security-audit"
claude "/improve --accessibility"
claude "/test --cross-browser"
```

## Project Structure Standards

### Flutter Projects
```
award_flutter_app/
├── lib/
│   ├── core/           # Core utilities and constants
│   ├── features/       # Feature-based architecture
│   ├── shared/         # Shared components and services
│   └── main.dart       # Application entry point
├── test/               # Unit and widget tests
├── integration_test/   # Integration tests
├── ios/               # iOS-specific code
├── android/           # Android-specific code
└── web/               # Web-specific code
```

### Web Projects
```
award_web_app/
├── src/
│   ├── components/     # Reusable UI components
│   ├── features/       # Feature-based modules
│   ├── services/       # API and business logic
│   ├── styles/         # Design system and themes
│   └── utils/          # Utility functions
├── public/             # Static assets
├── tests/              # Test files
└── docs/               # Documentation
```

## Performance Standards

### Flutter Performance Targets
- **App Startup**: <2s cold start, <500ms warm start
- **UI Responsiveness**: 60fps sustained, <16ms frame time
- **Memory Usage**: <100MB baseline, <200MB peak
- **Bundle Size**: <50MB APK, <20MB essential features

### Web Performance Targets
- **Lighthouse Score**: >95 all metrics
- **Core Web Vitals**: LCP <2.5s, FID <100ms, CLS <0.1
- **Bundle Size**: <500KB initial, <2MB total
- **Accessibility**: >98% automated testing score

## Security Standards

### Mobile Security (Flutter)
- **Secure Storage**: FlutterSecureStorage for sensitive data
- **Network Security**: Certificate pinning, encrypted requests
- **Code Protection**: Obfuscation, anti-tampering measures
- **Biometrics**: Secure biometric authentication

### Web Security
- **Content Security Policy**: XSS protection
- **HTTPS Everywhere**: Secure transport enforcement
- **Authentication**: JWT with refresh tokens, secure cookies
- **Input Validation**: Client and server-side validation

## Accessibility Standards

### WCAG 2.1 AA+ Compliance
- **Keyboard Navigation**: Full functionality without mouse
- **Screen Reader**: Perfect semantic markup and ARIA
- **Color Contrast**: >7:1 for normal text, >4.5:1 for large text
- **Motion**: Respect prefers-reduced-motion preferences

### Testing Requirements
- **Automated**: axe-core integration in CI/CD
- **Manual**: Keyboard and screen reader testing
- **User Testing**: Regular testing with disabled users

## Team Communication

### Slack Integration
- **Daily Standups**: Automated status updates via AI
- **Code Reviews**: Automated notifications and summaries
- **Deployments**: Real-time deployment status and metrics
- **Incidents**: Automated incident response and communication

### Documentation Standards
- **Architecture Decisions**: ADR format with rationale
- **API Documentation**: OpenAPI specifications with examples
- **User Guides**: Step-by-step with screenshots and videos
- **Code Comments**: Meaningful explanations, not obvious statements

## Continuous Learning

### Stay Updated
- **Flutter**: Follow Flutter team updates and best practices
- **Web Standards**: Monitor W3C specifications and browser updates
- **Security**: Subscribe to OWASP updates and vulnerability reports
- **Accessibility**: Follow WCAG updates and inclusive design trends

### Knowledge Sharing
- **Weekly Tech Talks**: Team members present new learnings
- **Code Review Learning**: Use reviews as teaching opportunities  
- **Documentation**: Maintain up-to-date team knowledge base
- **Mentoring**: Pair programming and knowledge transfer sessions

## Getting Help

### Internal Resources
- **Team Slack**: #award-winning-dev for questions and discussions
- **Documentation**: Internal wiki with team-specific guides
- **Code Reviews**: Ask for help during review process
- **1:1 Meetings**: Regular mentoring and guidance sessions

### External Resources
- **Claude Code Docs**: https://docs.anthropic.com/claude-code
- **Flutter Docs**: https://docs.flutter.dev
- **Web Platform**: https://web.dev
- **Accessibility**: https://www.w3.org/WAI/WCAG21/quickref/

## Success Metrics

### Individual Success
- **Code Quality**: Maintain >90% test coverage, zero lint errors
- **Performance**: Meet all performance targets consistently
- **Security**: Zero security vulnerabilities introduced
- **Accessibility**: 100% WCAG compliance on delivered features

### Team Success
- **Award Submissions**: Regular submission to industry awards
- **User Satisfaction**: >4.8/5 user ratings and reviews
- **Performance Rankings**: Top 25% in industry benchmarks
- **Recognition**: Industry recognition and speaking opportunities

Welcome to the team! Let's build award-winning applications together! 🏆