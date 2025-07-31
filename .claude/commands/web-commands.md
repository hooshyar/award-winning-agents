# Web Development Commands

Custom slash commands for award-winning web development workflows.

## Creative Development Commands

### `/web-creative [project-type]`
**Purpose**: Create award-winning creative web experiences
**Agent**: web-creative
**Flags**: `--magic --figma --wave-mode --persona-frontend`

**Workflow**:
1. Creative concept development and design system
2. Advanced UI component creation with animations
3. Accessibility-first implementation (WCAG 2.1 AA+)
4. Performance optimization for creative elements
5. Cross-browser testing and validation

### `/web-component [component-name]`
**Purpose**: Build advanced UI components with design system integration
**Agent**: web-creative + web-architect
**Flags**: `--magic --c7 --validate`

**Workflow**:
1. Component specification and design system alignment
2. Advanced CSS and JavaScript implementation
3. Accessibility features and keyboard navigation
4. Performance optimization and lazy loading
5. Storybook documentation and testing

### `/web-animation [animation-type]`
**Purpose**: Create performant, accessible animations and interactions
**Agent**: web-creative
**Flags**: `--magic --validate --think`

**Workflow**:
1. Animation design and performance planning
2. CSS/JavaScript animation implementation
3. Accessibility considerations (prefers-reduced-motion)
4. Performance optimization (60fps target)
5. Cross-browser compatibility testing

## Architecture Commands

### `/web-architecture [project-scope]`
**Purpose**: Design scalable web application architecture
**Agent**: web-architect
**Flags**: `--think-hard --seq --wave-mode`

**Workflow**:
1. System architecture design and documentation
2. Performance budget and optimization strategy
3. Scalability planning and implementation
4. Security architecture and compliance
5. Monitoring and observability setup

### `/web-optimize [optimization-type]`
**Purpose**: Comprehensive web performance optimization
**Agent**: web-performance + web-architect
**Flags**: `--play --seq --validate`

**Workflow**:
1. Performance audit and bottleneck identification
2. Core Web Vitals optimization (LCP, FID, CLS)
3. Bundle size optimization and code splitting
4. Image optimization and lazy loading
5. Caching strategy and CDN optimization

### `/web-pwa [feature]`
**Purpose**: Progressive Web App implementation with offline capabilities
**Agent**: web-architect + web-fullstack
**Flags**: `--validate --seq --c7`

**Workflow**:
1. Service worker implementation and caching strategy
2. Offline functionality and data synchronization
3. App manifest and installation prompts
4. Push notification integration
5. Performance and reliability testing

## Full-Stack Commands

### `/web-api [api-type]`
**Purpose**: Design and implement robust web APIs
**Agent**: web-fullstack
**Flags**: `--seq --validate --safe-mode`

**Workflow**:
1. API design and OpenAPI specification
2. Security implementation (authentication, authorization)
3. Performance optimization and caching
4. Error handling and validation
5. Documentation and testing

### `/web-database [database-type]`
**Purpose**: Database design and optimization for web applications
**Agent**: web-fullstack + web-architect
**Flags**: `--think --validate --safe-mode`

**Workflow**:
1. Database schema design and optimization
2. Query performance optimization
3. Data migration and backup strategies
4. Security and compliance implementation
5. Monitoring and alerting setup

### `/web-auth [auth-strategy]`
**Purpose**: Secure authentication and authorization implementation
**Agent**: web-fullstack + security-specialist
**Flags**: `--safe-mode --validate --ultrathink`

**Workflow**:
1. Authentication strategy design and implementation
2. Security best practices and compliance
3. User experience optimization
4. Session management and security
5. Penetration testing and validation

## Quality & Testing Commands

### `/web-test [test-type]`
**Purpose**: Comprehensive web application testing
**Agent**: web-performance + security-specialist
**Flags**: `--play --validate --delegate`

**Workflow**:
1. Unit and integration testing setup
2. End-to-end testing with Playwright
3. Performance testing and benchmarking
4. Accessibility testing and validation
5. Security testing and vulnerability assessment

### `/web-audit`
**Purpose**: Complete web application quality and compliance audit
**Agent**: web-creative + security-specialist + web-performance
**Flags**: `--ultrathink --wave-mode --validate`

**Workflow**:
1. Lighthouse audit and Core Web Vitals analysis
2. Accessibility compliance testing (WCAG 2.1 AA+)
3. Security vulnerability assessment
4. SEO optimization and validation
5. Cross-browser compatibility testing

### `/web-accessibility [scope]`
**Purpose**: Accessibility audit and implementation
**Agent**: web-accessibility + web-creative
**Flags**: `--validate --play --c7`

**Workflow**:
1. Accessibility audit and compliance assessment
2. Semantic HTML and ARIA implementation
3. Keyboard navigation and screen reader testing
4. Color contrast and visual accessibility
5. User testing with disabled users

## Deployment Commands

### `/web-deploy [environment]`
**Purpose**: Automated web application deployment with quality gates
**Agent**: devops-engineer + web-architect
**Flags**: `--safe-mode --validate --seq`

**Workflow**:
1. Build optimization and bundle analysis
2. Security scanning and vulnerability assessment
3. Performance testing and validation
4. CDN deployment and cache invalidation
5. Monitoring and alerting configuration

### `/web-cdn [optimization]`
**Purpose**: CDN optimization and global content delivery
**Agent**: devops-engineer + web-performance
**Flags**: `--validate --think --uc`

**Workflow**:
1. CDN strategy and configuration
2. Global edge optimization
3. Cache invalidation and versioning
4. Performance monitoring and optimization
5. Cost optimization and reporting

### `/web-monitoring [monitoring-type]`
**Purpose**: Comprehensive web application monitoring setup
**Agent**: devops-engineer + web-performance
**Flags**: `--sentry --validate --seq`

**Workflow**:
1. Real User Monitoring (RUM) implementation
2. Error tracking and alerting
3. Performance monitoring and optimization
4. Business metrics and analytics
5. Dashboard creation and alerting

## SEO & Marketing Commands

### `/web-seo [strategy]`
**Purpose**: Search engine optimization and performance
**Agent**: web-creative + technical-writer
**Flags**: `--c7 --validate --web-fetch`

**Workflow**:
1. Technical SEO audit and optimization
2. Content optimization and meta tags
3. Schema markup and structured data
4. Page speed optimization for SEO
5. Search console integration and monitoring

### `/web-analytics [platform]`
**Purpose**: Advanced web analytics and user behavior tracking
**Agent**: web-fullstack + web-performance
**Flags**: `--validate --safe-mode --c7`

**Workflow**:
1. Analytics platform integration and configuration
2. Custom event tracking and user journeys
3. Conversion optimization and A/B testing
4. Privacy compliance (GDPR, CCPA)
5. Reporting and dashboard creation

## Creative Specialization Commands

### `/web-webgl [project-type]`
**Purpose**: WebGL and 3D web experience development
**Agent**: web-creative
**Flags**: `--magic --validate --think-hard`

**Workflow**:
1. 3D scene design and optimization
2. WebGL implementation with Three.js
3. Performance optimization for mobile devices
4. Fallback strategies for older browsers
5. User interaction and animation design

### `/web-canvas [animation-type]`
**Purpose**: Advanced Canvas API animations and visualizations
**Agent**: web-creative
**Flags**: `--magic --validate --think`

**Workflow**:
1. Canvas animation design and planning
2. High-performance animation implementation
3. Interactive user controls and responses
4. Mobile optimization and touch support
5. Accessibility considerations and alternatives

### `/web-svg [graphic-type]`
**Purpose**: Interactive SVG graphics and animations
**Agent**: web-creative
**Flags**: `--magic --c7 --validate`

**Workflow**:
1. SVG design optimization and scalability
2. Interactive animation implementation
3. Accessibility features and descriptions
4. Performance optimization and lazy loading
5. Cross-browser compatibility testing

## Command Usage Examples

```bash
# Create award-winning creative website
/web-creative portfolio

# Build advanced navigation component
/web-component mega-menu

# Create smooth page transitions
/web-animation page-transitions

# Design scalable e-commerce architecture
/web-architecture ecommerce

# Optimize Core Web Vitals
/web-optimize performance

# Implement PWA with offline support
/web-pwa offline-first

# Create secure REST API
/web-api rest

# Implement user authentication
/web-auth oauth2

# Run comprehensive testing suite
/web-test all

# Perform complete quality audit
/web-audit

# Test accessibility compliance
/web-accessibility wcag-aa

# Deploy to production with monitoring
/web-deploy production

# Setup global CDN optimization
/web-cdn global

# Implement comprehensive monitoring
/web-monitoring rum

# Optimize for search engines
/web-seo technical

# Setup privacy-compliant analytics
/web-analytics gdpr

# Create interactive 3D experience
/web-webgl product-showcase

# Build data visualization
/web-canvas charts

# Create interactive infographic
/web-svg interactive-map
```

## Quality Standards Integration

Each command automatically applies:
- **Performance Validation**: Lighthouse scores >95, Core Web Vitals green
- **Accessibility Testing**: WCAG 2.1 AA+ compliance (>98% score)
- **Security Scanning**: OWASP compliance, vulnerability assessment
- **SEO Optimization**: Technical SEO best practices
- **Cross-Browser Testing**: Chrome, Firefox, Safari, Edge compatibility