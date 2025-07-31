# Optional Enhancements Guide - Advanced Team Integrations

**🎉 IMPORTANT: This guide is COMPLETELY OPTIONAL!**

All 13 agents work perfectly without any setup. This guide is only for teams who want advanced integrations with external services like GitHub, Slack, Figma, etc.

## 🚀 Zero Setup Usage (Recommended)

### Just Copy & Use (30 seconds)
```bash
# Clone and copy (works immediately!)
git clone https://github.com/your-org/award-winning-agents.git
cd award-winning-agents
cp -r .claude/* ~/.claude/
cp .mcp.json ~/.claude/

# Start using immediately - no setup needed!
claude "Hello! Show me available agents for Flutter development."
```

**✅ All 13 agents work perfectly at this point!**

## 🔧 Optional Advanced Integrations

**Only proceed if you want team collaboration features like:**
- GitHub integration for automated code reviews
- Slack notifications for deployment status  
- Figma design system synchronization
- Error monitoring with Sentry
- Project management with Linear

### Step 1: Choose Your Integration Level

**Minimalist (Web Research Only)**
```bash
# Copy just the web-fetch server (no API keys needed)
# Edit .mcp.json and add only:
{
  "web-fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch"]
  }
}
```

**Team Collaboration**
```bash
# Add GitHub and Slack for team coordination
# Requires: GITHUB_PAT, SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
```

**Full Integration**
```bash
# Copy all servers from mcp-optional.json
# Requires: All API keys listed below
```

## 🔧 Complete Configuration Guide

### Required API Keys Setup

#### GitHub Personal Access Token
1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `workflow`, `write:packages`
4. Copy token to `GITHUB_PAT` in `.env`

#### Slack Bot Configuration
1. Go to [Slack API](https://api.slack.com/apps)
2. Click "Create New App" → "From scratch"
3. Add OAuth scopes: `chat:write`, `files:read`, `users:read`
4. Install app to workspace
5. Copy Bot User OAuth Token to `SLACK_BOT_TOKEN`
6. Copy Signing Secret to `SLACK_SIGNING_SECRET`

#### Figma API Token (For Design System Work)
1. Go to [Figma Account Settings](https://www.figma.com/developers/api#access-tokens)
2. Generate new personal access token
3. Copy to `FIGMA_TOKEN` in `.env`

#### Linear API Key (For Project Management)
1. Go to [Linear Settings > API](https://linear.app/settings/api)
2. Create new API key
3. Copy to `LINEAR_API_KEY` in `.env`

#### Sentry Configuration (For Error Monitoring)
1. Go to [Sentry Account > API](https://sentry.io/settings/account/api/auth-tokens/)
2. Create new auth token with project permissions
3. Copy to `SENTRY_AUTH_TOKEN` in `.env`
4. Add your organization slug to `SENTRY_ORG_SLUG`

### Optional Enhancements

#### Apidog Integration (API Documentation)
1. Log into your Apidog account
2. Go to account settings and generate API key
3. Copy to `APIDOG_API_KEY` in `.env`

#### Firebase Integration (For Firebase Projects)
1. Go to Firebase Console > Project Settings > Service Accounts
2. Generate new private key
3. Copy project ID, private key, and client email to `.env`

## 🧪 Testing Your Setup

### Phase 1: Basic Functionality Test
```bash
# Test Claude Code installation
claude --version

# Test MCP server connections
claude --list-servers

# Test agent availability
claude "Which development agents are available?"
```

### Phase 2: Agent Functionality Test
```bash
# Test context management
claude "/context --restore"

# Test documentation coordination
claude "/docs --strategic-review"

# Test research capabilities
claude "/research --solution-find 'Flutter state management'"

# Test backend consultation
claude "/consult --backend-strategy"
```

### Phase 3: Integration Test
```bash
# Test GitHub integration
claude "Show me recent commits in this repository"

# Test Slack integration (if configured)
claude "Send a test message to our dev channel"

# Test Figma integration (if configured)
claude "Show me our design system components"
```

## 🔍 Troubleshooting Common Issues

### "Invalid settings files" Warning
**Problem**: Missing environment variables for MCP servers
**Solution**: 
1. Ensure `.env` file exists with required variables
2. Check that API keys are correctly formatted
3. Verify no extra spaces or quotes in `.env` file

### GitHub Integration Not Working
**Problem**: GITHUB_PAT missing or insufficient permissions
**Solution**:
1. Verify token has `repo`, `workflow`, `write:packages` scopes
2. Check token hasn't expired
3. Test token manually: `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user`

### Slack Integration Issues
**Problem**: Bot token vs user token confusion
**Solution**:
1. Use Bot User OAuth Token (starts with `xoxb-`)
2. Ensure bot is installed in workspace
3. Verify required scopes are granted

### Figma Access Problems
**Problem**: Token from wrong account or insufficient permissions
**Solution**:
1. Ensure token is from account with access to team files
2. Verify you're using personal access token, not OAuth token
3. Check token hasn't been revoked

### MCP Server Connection Failures
**Problem**: Servers not starting or timing out
**Solution**:
1. Check internet connection
2. Verify API endpoints are accessible
3. Try restarting Claude Code: `claude --restart`

## 🎯 Agent Activation Guide

### Automatic Agent Selection
Agents automatically activate based on keywords and context:

**Management Agents:**
- Type "product strategy" or "requirements" → Product Manager activates
- Type "sprint planning" or "coordination" → Project Manager activates

**Technical Agents:**
- Type "architecture" or "system design" → Tech Lead Architect activates
- Type "backend consultation" or "database choice" → Backend Specialist activates
- Type "Flutter" or "mobile development" → Flutter Mobile Development activates

**Workflow Optimization Agents:**
- Type "where were we" or "project status" → Context Manager activates
- Type "documentation" or "update docs" → Documentation Coordinator activates
- Type "how to" or "research" → Research Specialist activates
- Type "testing strategy" or "test coverage" → Testing Strategy Coordinator activates

### Manual Agent Selection
Use persona flags for explicit agent selection:
```bash
claude --persona-product-manager "Define requirements for user authentication"
claude --persona-backend "Recommend database for e-commerce platform"
claude --persona-context-manager "Restore our project context from yesterday"
```

## 📊 Performance Optimization

### Recommended Flags for Different Scenarios

**MVP Development:**
```bash
claude --uc --validate "/consult --backend-strategy"  # Fast, validated consultation
```

**Complex Architecture:**
```bash
claude --think-hard --seq --wave-mode "/architect --system-design"  # Deep analysis
```

**Team Coordination:**
```bash
claude --delegate --seq "/status --comprehensive"  # Parallel status analysis
```

**Research & Solutions:**
```bash
claude --web-search --web-fetch "/research --solution-find 'NextJS deployment'"
```

## 🔐 Security Best Practices

### API Key Management
1. **Never commit `.env` to version control**
2. **Use different tokens for dev/staging/prod**
3. **Regularly rotate API keys (monthly recommended)**
4. **Monitor API key usage and access logs**
5. **Follow principle of least privilege for scopes**

### Team Access Control
1. **Use team-specific Slack workspaces**
2. **Separate Figma team access by project**
3. **Use organization-level GitHub tokens when possible**
4. **Implement proper Linear workspace permissions**

## 🎓 Getting Started Workflows

### New Team Member Onboarding
```bash
# 1. Setup environment
cp .env.example .env
# Edit .env with provided team API keys

# 2. Verify setup
claude --doctor

# 3. Get project context
claude "/context --restore"

# 4. Understand current architecture
claude "/status --comprehensive"

# 5. Review documentation
claude "/docs --strategic-review"
```

### Starting a New Project
```bash
# 1. Get technology consultation
claude "/consult --backend-strategy"
claude "/recommend --technology-stack"

# 2. Plan architecture
claude "/plan --backend-architecture"

# 3. Setup development workflow
claude "/workflow --optimize"

# 4. Create testing strategy
claude "/test --strategic-plan"
```

### Daily Development Workflow
```bash
# Morning: Restore context
claude "/context --restore"

# During development: Get help as needed
claude "/research --solution-find 'specific problem'"
claude "/docs --smart-generate feature-guide"

# End of day: Update context
claude "/memory --update"
```

## 📈 Success Metrics

After successful setup, you should experience:
- ✅ Zero context loss between sessions
- ✅ <5 minute project context restoration
- ✅ Always current documentation
- ✅ Current solutions for technical problems
- ✅ Strategic test coverage decisions
- ✅ Collaborative backend technology decisions

## 🆘 Getting Help

### Built-in Help
```bash
claude /help                    # General help
claude --list-servers          # Show MCP server status
claude --doctor                # Run diagnostics
```

### Community Support
- **Issues**: Report problems in project GitHub issues
- **Discussions**: Ask questions in GitHub discussions
- **Documentation**: Comprehensive docs in `/docs` folder
- **Team Slack**: #award-winning-dev channel (if configured)

### Emergency Recovery
```bash
# If context is lost
claude "/recover --project-context"

# If documentation is inconsistent  
claude "/recover --documentation"

# If workflow is disrupted
claude "/workflow --context-fix"
```

---

**🎉 You're ready to build award-winning applications with your AI development team!**