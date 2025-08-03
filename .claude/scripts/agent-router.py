#!/usr/bin/env python3
"""
Agent-First Routing System for Claude Code
Intelligently routes requests to specialized agents with fallback mechanisms
"""

import json
import re
import os
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class AgentMatch:
    """Represents an agent match with confidence score"""
    name: str
    confidence: float
    reasoning: str
    fallback_agents: List[str]

@dataclass
class RoutingResult:
    """Result of routing decision"""
    selected_agent: Optional[str]
    confidence: float
    fallback_chain: List[str]
    reasoning: str
    use_task_tool: bool = False

class AgentRouter:
    """Intelligent agent routing system"""
    
    def __init__(self, config_path: str = "../config"):
        self.config_path = Path(config_path).expanduser()
        self.agents = self._load_agent_registry()
        self.routing_rules = self._load_routing_rules()
        self.config = self._load_router_config()
        
    def _load_agent_registry(self) -> Dict:
        """Load agent registry from configuration"""
        registry_file = self.config_path / "agent-registry.json"
        if registry_file.exists():
            with open(registry_file) as f:
                return json.load(f)
        else:
            print(f"Registry file not found at {registry_file}, using defaults")
        return self._get_default_registry()
    
    def _load_routing_rules(self) -> List[Dict]:
        """Load routing rules from configuration"""
        rules_file = self.config_path / "routing-rules.json"
        if rules_file.exists():
            with open(rules_file) as f:
                return json.load(f)["rules"]
        return self._get_default_rules()
    
    def _load_router_config(self) -> Dict:
        """Load router configuration"""
        config_file = self.config_path / "router.json"
        if config_file.exists():
            with open(config_file) as f:
                return json.load(f)["agent_routing"]
        return self._get_default_config()
    
    def route_request(self, user_input: str, context: str = "") -> RoutingResult:
        """Main routing function - returns best agent match with fallback"""
        
        # Extract keywords and analyze context
        keywords = self._extract_keywords(user_input.lower())
        context_signals = self._analyze_context(context.lower())
        
        print(f"Keywords: {keywords}")
        print(f"Context signals: {context_signals}")
        print(f"Available agents: {len(self.agents.get('agents', []))}")
        
        # Find agent matches
        agent_matches = self._find_agent_matches(user_input, keywords, context_signals)
        
        print(f"Agent matches found: {len(agent_matches)}")
        for match in agent_matches:
            print(f"  - {match.name}: {match.confidence:.2f} ({match.reasoning})")
        
        # Sort by confidence
        agent_matches.sort(key=lambda x: x.confidence, reverse=True)
        
        # Apply routing decision logic
        return self._make_routing_decision(agent_matches, user_input, keywords)
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract relevant keywords from input text"""
        # Remove common words and focus on technical terms
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'its', 'our', 'their'}
        
        words = re.findall(r'\b\w+\b', text)
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        # Add technical phrases
        technical_phrases = [
            'not working', 'stack trace', 'error message', 'performance issue',
            'cross platform', 'state management', 'web development', 'mobile development',
            'root cause', 'deep dive', 'best practices', 'code review'
        ]
        
        for phrase in technical_phrases:
            if phrase in text:
                keywords.extend(phrase.split())
        
        return list(set(keywords))
    
    def _analyze_context(self, context: str) -> Dict[str, bool]:
        """Analyze context for technical signals"""
        signals = {
            'has_error_trace': bool(re.search(r'(traceback|stack trace|error:|exception)', context)),
            'has_code_snippet': bool(re.search(r'(```|function|class|def |var |const )', context)),
            'has_performance_metrics': bool(re.search(r'(ms|seconds|memory|cpu|performance)', context)),
            'has_mobile_context': bool(re.search(r'(flutter|ios|android|mobile|app store)', context)),
            'has_web_context': bool(re.search(r'(html|css|javascript|react|vue|angular|web)', context)),
            'has_backend_context': bool(re.search(r'(api|database|server|backend|microservice)', context)),
            'has_security_context': bool(re.search(r'(security|vulnerability|auth|permission)', context))
        }
        return signals
    
    def _find_agent_matches(self, user_input: str, keywords: List[str], context_signals: Dict) -> List[AgentMatch]:
        """Find matching agents with confidence scores"""
        matches = []
        
        for agent in self.agents.get("agents", []):
            confidence = self._calculate_confidence(agent, user_input, keywords, context_signals)
            print(f"Agent {agent['name']}: confidence = {confidence:.3f}")
            if confidence >= self.config.get("confidence_threshold", 0.7):
                matches.append(AgentMatch(
                    name=agent["name"],
                    confidence=confidence,
                    reasoning=self._explain_match(agent, keywords, context_signals),
                    fallback_agents=agent.get("fallback", [])
                ))
        
        return matches
    
    def _calculate_confidence(self, agent: Dict, user_input: str, keywords: List[str], context_signals: Dict) -> float:
        """Calculate confidence score for agent match"""
        score = 0.0
        
        # Keyword matching
        primary_keywords = agent.get("primary_keywords", [])
        secondary_keywords = agent.get("secondary_keywords", [])
        
        primary_matches = sum(1 for kw in keywords if any(pk in kw for pk in primary_keywords))
        secondary_matches = sum(1 for kw in keywords if any(sk in kw for sk in secondary_keywords))
        
        # Weight primary keywords more heavily
        keyword_score = (primary_matches * 0.8 + secondary_matches * 0.4) / max(len(keywords), 1)
        score += min(keyword_score, 1.0) * 0.6
        
        # Pattern matching
        patterns = agent.get("activation_patterns", [])
        pattern_score = 0
        for pattern in patterns:
            if re.search(pattern, user_input, re.IGNORECASE):
                pattern_score = 1.0
                break
        score += pattern_score * 0.3
        
        # Context signal matching
        domains = agent.get("domains", [])
        context_score = 0
        if "debugging" in domains and context_signals.get("has_error_trace"):
            context_score += 0.5
        if "mobile" in domains and context_signals.get("has_mobile_context"):
            context_score += 0.5
        if "web" in domains and context_signals.get("has_web_context"):
            context_score += 0.5
        if "backend" in domains and context_signals.get("has_backend_context"):
            context_score += 0.5
        
        score += min(context_score, 1.0) * 0.1
        
        return min(score, 1.0)
    
    def _explain_match(self, agent: Dict, keywords: List[str], context_signals: Dict) -> str:
        """Generate explanation for why agent was matched"""
        reasons = []
        
        # Check keyword matches
        primary_keywords = agent.get("primary_keywords", [])
        matched_primary = [kw for kw in keywords if any(pk in kw for pk in primary_keywords)]
        if matched_primary:
            reasons.append(f"Primary keywords matched: {', '.join(matched_primary[:3])}")
        
        # Check context signals
        domains = agent.get("domains", [])
        if "debugging" in domains and context_signals.get("has_error_trace"):
            reasons.append("Error/debugging context detected")
        if "mobile" in domains and context_signals.get("has_mobile_context"):
            reasons.append("Mobile development context detected")
        
        return "; ".join(reasons) if reasons else "General pattern match"
    
    def _make_routing_decision(self, matches: List[AgentMatch], user_input: str, keywords: List[str]) -> RoutingResult:
        """Make final routing decision with fallback logic"""
        
        if not matches:
            # No agent matches - decide between task tool and direct execution
            if self._is_complex_task(user_input, keywords):
                return RoutingResult(
                    selected_agent=None,
                    confidence=0.0,
                    fallback_chain=["task_tool_general"],
                    reasoning="No specialized agent match, but task appears complex - using general task tool",
                    use_task_tool=True
                )
            else:
                return RoutingResult(
                    selected_agent=None,
                    confidence=0.0,
                    fallback_chain=["direct_execution"],
                    reasoning="Simple task, no specialized agent needed"
                )
        
        best_match = matches[0]
        
        # High confidence - use primary agent
        if best_match.confidence >= 0.9:
            return RoutingResult(
                selected_agent=best_match.name,
                confidence=best_match.confidence,
                fallback_chain=best_match.fallback_agents + ["task_tool_general", "direct_execution"],
                reasoning=f"High confidence match: {best_match.reasoning}"
            )
        
        # Medium confidence - include more fallbacks
        elif best_match.confidence >= 0.7:
            fallback_chain = best_match.fallback_agents[:]
            if len(matches) > 1:
                fallback_chain.append(matches[1].name)  # Add second-best agent
            fallback_chain.extend(["task_tool_general", "direct_execution"])
            
            return RoutingResult(
                selected_agent=best_match.name,
                confidence=best_match.confidence,
                fallback_chain=fallback_chain,
                reasoning=f"Medium confidence match: {best_match.reasoning}"
            )
        
        # Low confidence - prefer task tool with agent consultation
        else:
            return RoutingResult(
                selected_agent=None,
                confidence=best_match.confidence,
                fallback_chain=[best_match.name, "task_tool_general", "direct_execution"],
                reasoning=f"Low confidence - consulting {best_match.name} via task tool",
                use_task_tool=True
            )
    
    def _is_complex_task(self, user_input: str, keywords: List[str]) -> bool:
        """Determine if task is complex enough to warrant task tool usage"""
        complexity_indicators = [
            'analyze', 'investigate', 'research', 'comprehensive', 'detailed',
            'architecture', 'system', 'multiple', 'complex', 'advanced',
            'optimize', 'performance', 'scale', 'security', 'integration'
        ]
        
        # Long input suggests complexity
        if len(user_input.split()) > 20:
            return True
        
        # Multiple technical keywords suggest complexity  
        if len(keywords) > 5:
            return True
        
        # Complexity indicators present
        complexity_score = sum(1 for indicator in complexity_indicators if indicator in user_input.lower())
        return complexity_score >= 2
    
    def _get_default_registry(self) -> Dict:
        """Default agent registry if no config file exists"""
        return {
            "agents": [
                {
                    "name": "deep-research-issue-fixer",
                    "priority": 9,
                    "domains": ["debugging", "troubleshooting", "analysis"],
                    "primary_keywords": ["debug", "error", "issue", "problem", "bug", "broken"],
                    "secondary_keywords": ["not working", "fails", "crashes", "exception", "investigate"],
                    "activation_patterns": ["debug.*", "error.*", "issue.*", "problem.*", "bug.*"],
                    "fallback": ["qa-testing-specialist", "research-specialist"]
                },
                {
                    "name": "flutter-mobile-development",
                    "priority": 8,
                    "domains": ["mobile", "flutter", "cross-platform"],
                    "primary_keywords": ["flutter", "mobile", "ios", "android", "dart"],
                    "secondary_keywords": ["app", "widget", "material", "cupertino"],
                    "activation_patterns": ["flutter.*", "mobile.*", "(ios|android).*"],
                    "fallback": ["tech-lead-architect", "frontend-specialist"]
                },
                {
                    "name": "tech-lead-architect",
                    "priority": 8,
                    "domains": ["architecture", "system design", "scalability"],
                    "primary_keywords": ["architecture", "design", "scalability", "system"],
                    "secondary_keywords": ["patterns", "microservices", "monolith", "distributed"],
                    "activation_patterns": ["architect.*", "design.*", "system.*"],
                    "fallback": ["backend-specialist", "devops-engineer"]
                }
            ]
        }
    
    def _get_default_rules(self) -> List[Dict]:
        """Default routing rules if no config file exists"""
        return [
            {
                "pattern": "(debug|error|issue|problem|bug)",
                "agent": "deep-research-issue-fixer",
                "confidence": 0.9,
                "fallback": ["qa-testing-specialist", "research-specialist"]
            },
            {
                "pattern": "(flutter|mobile|ios|android)",
                "agent": "flutter-mobile-development",
                "confidence": 0.8,
                "fallback": ["tech-lead-architect"]
            }
        ]
    
    def _get_default_config(self) -> Dict:
        """Default router configuration"""
        return {
            "enabled": True,
            "mode": "agent_first",
            "confidence_threshold": 0.7,
            "max_agents": 3,
            "fallback_timeout": 30,
            "parallel_evaluation": True
        }

def main():
    """CLI interface for testing the router"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agent-router.py 'user input' [context]")
        return
    
    user_input = sys.argv[1]
    context = sys.argv[2] if len(sys.argv) > 2 else ""
    
    router = AgentRouter()
    result = router.route_request(user_input, context)
    
    print(f"Selected Agent: {result.selected_agent}")
    print(f"Confidence: {result.confidence:.2f}")
    print(f"Use Task Tool: {result.use_task_tool}")
    print(f"Reasoning: {result.reasoning}")
    print(f"Fallback Chain: {' -> '.join(result.fallback_chain)}")

if __name__ == "__main__":
    main()