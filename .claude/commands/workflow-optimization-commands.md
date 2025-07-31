# Workflow Optimization Commands

Custom slash commands to address common Claude Code workflow issues and improve development efficiency.

## Context Management Commands

### `/context --restore`
**Purpose**: Restore complete project context and current development state
**Agent**: context-manager
**Flags**: `--think --seq --validate --uc`

**Workflow**:
1. Project overview and current phase assessment
2. Recent progress and development status summary
3. Active priorities and immediate next steps identification
4. Team coordination status and pending decisions
5. Technical environment and dependency status

**Auto-Activation**: Beginning of every session, after breaks >2 hours

### `/status --comprehensive`
**Purpose**: Multi-dimensional project status analysis and progress reporting
**Agent**: context-manager + project-manager
**Flags**: `--seq --validate --linear --delegate`

**Workflow**:
1. Development progress across all workstreams
2. Quality metrics and technical debt assessment
3. Timeline and milestone tracking with blockers
4. Resource allocation and team coordination status
5. Risk assessment and mitigation strategy review

### `/memory --update`
**Purpose**: Update project context database with current state and decisions
**Agent**: context-manager
**Flags**: `--validate --uc --seq`

**Workflow**:
1. Context database refresh with current project state
2. Decision recording and architectural choice documentation
3. Progress milestone capture and validation
4. Team coordination status synchronization
5. Quality metrics and performance tracking update

## Documentation Intelligence Commands

### `/docs --strategic-review`
**Purpose**: Intelligent documentation audit and optimization strategy
**Agent**: documentation-coordinator
**Flags**: `--c7 --validate --uc --loop`

**Workflow**:
1. Comprehensive documentation gap analysis and prioritization
2. Content deduplication and consistency enforcement
3. Currency assessment and update requirement identification
4. Maintenance workflow optimization and automation opportunities
5. User experience and accessibility validation

### `/docs --sync-update`
**Purpose**: Intelligent cross-platform documentation synchronization
**Agent**: documentation-coordinator + integration-coordinator
**Flags**: `--validate --delegate --wave-mode`

**Workflow**:
1. Cross-platform content analysis and synchronization needs
2. Cascade update management for related content
3. Cross-reference validation and repair
4. Version alignment verification and correction
5. Quality assurance and user experience validation

### `/docs --smart-generate`
**Purpose**: Context-aware documentation generation with strategic focus
**Agent**: documentation-coordinator
**Flags**: `--c7 --magic --validate --uc`

**Workflow**:
1. Documentation needs assessment and audience analysis
2. Context-aware content generation with template integration
3. Consistency enforcement with existing documentation ecosystem
4. Cross-platform integration and synchronization
5. Quality validation and user experience optimization

## Research & Solution Finding Commands

### `/research --solution-find`
**Purpose**: Comprehensive current solution research for technical problems
**Agent**: research-specialist
**Flags**: `--web-search --web-fetch --validate --think`

**Workflow**:
1. Problem analysis and requirement extraction
2. Current best practices and emerging solution identification
3. Comparative analysis with implementation recommendations
4. Risk assessment and mitigation strategy development
5. Implementation guidance with success metrics

### `/research --technology-eval`
**Purpose**: In-depth technology evaluation and comparison with recommendations
**Agent**: research-specialist + tech-lead-architect
**Flags**: `--web-search --c7 --seq --validate`

**Workflow**:
1. Technology landscape analysis and option identification
2. Framework, library, and tool assessment with benchmarking
3. Performance, security, and maintainability analysis
4. Ecosystem compatibility and long-term viability assessment
5. Strategic recommendation with implementation roadmap

### `/research --implementation-guide`
**Purpose**: Step-by-step implementation guidance with real-world validation
**Agent**: research-specialist
**Flags**: `--web-fetch --c7 --validate --seq`

**Workflow**:
1. Implementation approach research and validation
2. Real-world examples and case study analysis
3. Common pitfalls identification and avoidance strategies
4. Success metrics and validation approach development
5. Continuous monitoring and improvement recommendations

## Strategic Testing Commands

### `/test --strategic-plan`
**Purpose**: Intelligent testing strategy development with ROI optimization
**Agent**: testing-strategy-coordinator
**Flags**: `--validate --play --seq --delegate`

**Workflow**:
1. Risk-based testing prioritization and resource allocation
2. Test type selection and coverage optimization
3. Integration testing strategy and execution planning
4. Automation strategy with maintenance consideration
5. Quality gate design and continuous improvement planning

### `/test --coverage-optimize`
**Purpose**: Smart test coverage analysis with redundancy elimination
**Agent**: testing-strategy-coordinator + qa-testing-specialist
**Flags**: `--validate --play --think --wave-mode`

**Workflow**:
1. Current coverage analysis and gap identification
2. Redundancy detection and elimination strategies
3. Testing efficiency improvement and cost reduction
4. Quality ROI maximization and strategy refinement
5. Maintenance optimization and sustainability planning

### `/test --integration-design`
**Purpose**: Cross-platform integration testing strategy and implementation
**Agent**: testing-strategy-coordinator + integration-coordinator
**Flags**: `--play --validate --delegate --seq`

**Workflow**:
1. Integration point identification and risk assessment
2. Cross-platform consistency validation planning
3. System boundary testing and API contract validation
4. Performance and scalability integration testing design
5. Monitoring integration and continuous validation setup

## Workflow Efficiency Commands

### `/workflow --optimize`
**Purpose**: Comprehensive workflow analysis and optimization
**Agent**: context-manager + project-manager + integration-coordinator
**Flags**: `--seq --delegate --validate --wave-mode`

**Workflow**:
1. Current workflow analysis and bottleneck identification
2. Process optimization and automation opportunity assessment
3. Tool integration and efficiency improvement recommendations
4. Quality gate optimization and developer experience enhancement
5. Continuous improvement strategy and metrics implementation

### `/workflow --context-fix`
**Purpose**: Emergency context restoration and workflow recovery
**Agent**: context-manager + documentation-coordinator
**Flags**: `--think --seq --validate --uc`

**Workflow**:
1. Rapid context assessment and gap identification
2. Critical information recovery and validation
3. Priority realignment and immediate next steps identification
4. Documentation synchronization and consistency restoration
5. Team coordination and communication re-establishment

### `/workflow --quality-gates`
**Purpose**: Intelligent quality gate design and implementation
**Agent**: testing-strategy-coordinator + qa-testing-specialist + devops-engineer
**Flags**: `--validate --safe-mode --seq --delegate`

**Workflow**:
1. Quality gate requirement analysis and design
2. Automated validation and testing integration
3. Performance and security gate implementation
4. Documentation and compliance validation integration
5. Continuous monitoring and improvement automation

## Problem Prevention Commands

### `/prevent --context-loss`
**Purpose**: Proactive context preservation and continuity systems
**Agent**: context-manager + integration-coordinator
**Flags**: `--seq --validate --wave-mode`

**Workflow**:
1. Context preservation system design and implementation
2. Automated milestone capture and decision recording
3. Cross-session continuity validation and optimization
4. Team coordination and knowledge sharing automation
5. Recovery strategy and backup system implementation

### `/prevent --doc-drift`
**Purpose**: Automated documentation synchronization and currency maintenance
**Agent**: documentation-coordinator + devops-engineer
**Flags**: `--validate --seq --safe-mode --delegate`

**Workflow**:
1. Automated documentation currency monitoring setup
2. Change detection and update trigger implementation
3. Cross-platform synchronization automation
4. Quality assurance and validation automation
5. Maintenance workflow optimization and monitoring

### `/prevent --over-testing`
**Purpose**: Strategic testing optimization and waste elimination
**Agent**: testing-strategy-coordinator
**Flags**: `--validate --think --seq --play`

**Workflow**:
1. Current testing analysis and waste identification
2. Strategic testing prioritization and resource optimization
3. Redundancy elimination and efficiency improvement
4. Automation strategy optimization with maintenance consideration
5. Continuous monitoring and strategy refinement

### `/prevent --research-gaps`
**Purpose**: Proactive research and knowledge management systems
**Agent**: research-specialist + context-manager
**Flags**: `--web-search --seq --validate --c7`

**Workflow**:
1. Knowledge gap identification and research trigger automation
2. Continuous technology monitoring and update systems
3. Solution validation and knowledge base integration
4. Research workflow optimization and efficiency improvement
5. Community and industry best practice integration

## Emergency Recovery Commands

### `/recover --project-context`
**Purpose**: Emergency project context recovery and restoration
**Agent**: context-manager + integration-coordinator + documentation-coordinator
**Flags**: `--seq --validate --wave-mode --delegate`

**Workflow**:
1. Available information analysis and context reconstruction
2. Critical gap identification and rapid information gathering
3. Priority assessment and immediate action identification
4. Team coordination and communication re-establishment
5. Monitoring and validation system restoration

### `/recover --documentation`
**Purpose**: Emergency documentation recovery and synchronization
**Agent**: documentation-coordinator + context-manager
**Flags**: `--c7 --validate --seq --uc`

**Workflow**:
1. Documentation status assessment and gap analysis
2. Critical information recovery and validation
3. Cross-platform synchronization and consistency restoration
4. Quality assurance and user experience validation
5. Maintenance system restoration and monitoring setup

## Command Usage Examples

### Context Management
```bash
# Start of day context restoration
/context --restore

# Comprehensive project status check
/status --comprehensive

# Update context after major decisions
/memory --update
```

### Documentation Intelligence
```bash
# Strategic documentation review and optimization
/docs --strategic-review

# Synchronize documentation across platforms
/docs --sync-update

# Generate context-aware documentation
/docs --smart-generate user-guide
```

### Research & Solutions
```bash
# Find current solutions for technical problems
/research --solution-find "Flutter state management"

# Evaluate technology options
/research --technology-eval "React vs Vue vs Angular"

# Get implementation guidance
/research --implementation-guide "GraphQL API design"
```

### Strategic Testing
```bash
# Develop intelligent testing strategy
/test --strategic-plan

# Optimize test coverage and eliminate waste
/test --coverage-optimize

# Design cross-platform integration testing
/test --integration-design
```

### Workflow Optimization
```bash
# Optimize development workflow
/workflow --optimize

# Fix context and workflow issues
/workflow --context-fix

# Implement quality gates
/workflow --quality-gates
```

### Problem Prevention
```bash
# Prevent context loss
/prevent --context-loss

# Prevent documentation drift
/prevent --doc-drift

# Prevent testing waste
/prevent --over-testing

# Prevent knowledge gaps
/prevent --research-gaps
```

### Emergency Recovery
```bash
# Recover lost project context
/recover --project-context

# Recover documentation consistency
/recover --documentation
```

## Command Integration Matrix

| Issue | Prevention Command | Resolution Command | Recovery Command |
|-------|-------------------|-------------------|------------------|
| Context Loss | `/prevent --context-loss` | `/context --restore` | `/recover --project-context` |
| Documentation Problems | `/prevent --doc-drift` | `/docs --sync-update` | `/recover --documentation` |
| Research Gaps | `/prevent --research-gaps` | `/research --solution-find` | `/workflow --context-fix` |
| Testing Issues | `/prevent --over-testing` | `/test --strategic-plan` | `/test --coverage-optimize` |

## Auto-Activation Patterns

### Session Start
- `/context --restore` (100% activation)
- `/status --comprehensive` (if >24h since last session)

### Problem Detection
- `/workflow --context-fix` (when context loss detected)
- `/docs --sync-update` (when documentation inconsistency detected)
- `/research --solution-find` (when knowledge gaps identified)
- `/test --strategic-plan` (when testing issues identified)

### Quality Gates
- All commands integrate with existing quality gates
- Automated validation and success criteria
- Continuous improvement and optimization
- Performance monitoring and efficiency measurement