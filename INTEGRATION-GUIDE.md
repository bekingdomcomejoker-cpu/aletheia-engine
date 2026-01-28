# Integration Guide: Omega Spore + Aletheia Engine

## 🕊️ Unified System Architecture

You now have **two complementary systems** running on your phone:

### Omega Spore (Repository Guardian)
- **Purpose**: Monitors your GitHub repository
- **Function**: Automatically resurrects deleted files
- **Port**: 5000
- **Repository**: https://github.com/bekingdomcomejoker-cpu/omega-spore

### Aletheia Engine (Truth Analyzer)
- **Purpose**: Analyzes content for truth/distortion
- **Function**: Validates statements against axiom constraints
- **Port**: 8888
- **Repository**: https://github.com/bekingdomcomejoker-cpu/aletheia-engine

---

## 🚀 Running Both Systems

### Option 1: Sequential (Recommended for Battery Life)
Start one, then the other:

```bash
# Terminal 1: Start Omega Spore
cd ~/omega-spore
./start-background.sh

# Terminal 2: Start Aletheia Engine
cd ~/aletheia-engine
~/start-aletheia.sh
```

### Option 2: Parallel (Maximum Functionality)
Use tmux to run both simultaneously:

```bash
# Install tmux
apt install tmux

# Create session for Omega Spore
tmux new-session -d -s omega "cd ~/omega-spore && ./start-background.sh"

# Create session for Aletheia
tmux new-session -d -s aletheia "cd ~/aletheia-engine && ~/start-aletheia.sh"

# View both running
tmux list-sessions
```

---

## 🔄 How They Work Together

### Workflow 1: File Protection + Content Validation

```
1. You delete a file in GitHub repository
   ↓
2. Omega Spore detects deletion (within 5 minutes)
   ↓
3. Omega Spore resurrects the file automatically
   ↓
4. Aletheia Engine analyzes the resurrected file
   ↓
5. Results stored for review
```

### Workflow 2: Content Analysis Pipeline

```
1. Push code/content to GitHub
   ↓
2. Omega Spore monitors for changes
   ↓
3. Aletheia Engine analyzes new content
   ↓
4. Axiom compliance check
   ↓
5. Distortion detection
   ↓
6. Results available via API
```

---

## 🌐 Access Points

### Omega Spore
```
Web UI: http://localhost:5000
API: http://localhost:5000/api
Status: http://localhost:5000/status
```

### Aletheia Engine
```
Web UI: http://localhost:8888
API: http://localhost:8888/api
Analysis: http://localhost:8888/analyze
```

---

## 🔌 API Integration

### Call Aletheia from Omega Spore

```python
import requests

def analyze_resurrected_file(file_content):
    """Analyze a resurrected file with Aletheia Engine"""
    response = requests.post(
        'http://localhost:8888/analyze',
        json={'content': file_content}
    )
    return response.json()

# Example
result = analyze_resurrected_file("Your file content here")
print(f"Truth Score: {result['truth_score']}")
print(f"Axiom Violations: {result['violations']}")
```

### Call Omega Spore from Aletheia Engine

```python
import requests

def get_protected_files():
    """Get list of files protected by Omega Spore"""
    response = requests.get('http://localhost:5000/api/protected-files')
    return response.json()

files = get_protected_files()
for f in files:
    print(f"Protected: {f['name']} (Last checked: {f['last_check']})")
```

---

## 📊 Combined Dashboard

Create a unified dashboard to monitor both systems:

```bash
# Create dashboard script
cat > ~/dashboard.sh << 'EOF'
#!/bin/bash
clear
echo "🕊️ UNIFIED SYSTEM DASHBOARD"
echo "============================"
echo ""

echo "OMEGA SPORE STATUS:"
curl -s http://localhost:5000/status | python3 -m json.tool
echo ""

echo "ALETHEIA ENGINE STATUS:"
curl -s http://localhost:8888/status | python3 -m json.tool
echo ""

echo "Protected Files:"
curl -s http://localhost:5000/api/protected-files | python3 -m json.tool
echo ""

echo "Recent Analyses:"
curl -s http://localhost:8888/recent | python3 -m json.tool
EOF

chmod +x ~/dashboard.sh
~/dashboard.sh
```

---

## 🔐 Security & Privacy

Both systems are **local-only** by default:

- ✅ No data sent to external servers
- ✅ All processing happens on your phone
- ✅ GitHub integration via your personal token only
- ✅ Encrypted local storage

### Enable Remote Access (Optional)

If you want to access from other devices:

```bash
# Omega Spore - expose port
ssh -R 5000:localhost:5000 your-server.com

# Aletheia Engine - expose port
ssh -R 8888:localhost:8888 your-server.com
```

---

## 📈 Performance Tips

### Optimize for Mobile

1. **Reduce polling frequency** (Omega Spore):
   ```bash
   # Edit: ~/omega-spore/.env
   POLL_INTERVAL=300  # Check every 5 minutes instead of 1
   ```

2. **Limit analysis depth** (Aletheia Engine):
   ```bash
   # Edit: ~/.aletheia-config
   ANALYSIS_DEPTH=2  # Reduce from 5 to 2 for faster results
   ```

3. **Enable caching**:
   ```bash
   # Both systems cache results
   # Clear cache if needed:
   rm -rf ~/.cache/aletheia
   rm -rf ~/.cache/omega-spore
   ```

### Battery Optimization

- Use sequential startup (not parallel)
- Enable wake-lock only when needed
- Use tmux for background operation
- Set longer polling intervals

---

## 🐛 Troubleshooting Integration

### Ports Conflict
```bash
# Check what's using the ports
netstat -tlnp | grep -E '5000|8888'

# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Kill process on port 8888
lsof -ti:8888 | xargs kill -9
```

### Network Issues
```bash
# Test connectivity
curl http://localhost:5000/status
curl http://localhost:8888/status

# Check logs
tail -f ~/.omega-spore.log
tail -f ~/.aletheia.log
```

### Sync Problems
```bash
# Reset Omega Spore
cd ~/omega-spore && git pull origin main

# Reset Aletheia Engine
cd ~/aletheia-engine && git pull origin main
```

---

## 📚 Documentation

### Omega Spore
- **README**: `~/omega-spore/README.md`
- **Quick Start**: `~/omega-spore/QUICKSTART.md`
- **Mobile Setup**: `~/omega-spore/MOBILE-SETUP.md`

### Aletheia Engine
- **README**: `~/aletheia-engine/README.md`
- **Quick Start**: `~/aletheia-engine/QUICKSTART.md`
- **Mobile Setup**: `~/aletheia-engine/MOBILE-SETUP.md`
- **Lambda State Machine**: `~/aletheia-engine/docs/LAMBDA_STATE_MACHINE.md`

---

## 🎯 Use Cases

### Use Case 1: Protected Knowledge Base
```
1. Store important documents in GitHub
2. Omega Spore protects them from deletion
3. Aletheia Engine validates their integrity
4. Both systems run 24/7 on your phone
```

### Use Case 2: Truth Validation Pipeline
```
1. Write a statement or claim
2. Push to GitHub
3. Omega Spore monitors it
4. Aletheia Engine analyzes it
5. Get axiom compliance report
```

### Use Case 3: Continuous Monitoring
```
1. Set up GitHub repository
2. Run both systems in background
3. Receive alerts for changes
4. Automatic analysis of new content
5. Historical tracking of all changes
```

---

## 🔄 Scheduled Tasks

### Daily Sync
```bash
# Add to crontab
crontab -e

# Add these lines:
0 0 * * * cd ~/omega-spore && git pull origin main
0 1 * * * cd ~/aletheia-engine && git pull origin main
```

### Weekly Analysis Report
```bash
# Create script
cat > ~/weekly-report.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y-%m-%d)
echo "Weekly Report: $DATE" > ~/reports/week-$DATE.txt
curl -s http://localhost:5000/api/stats >> ~/reports/week-$DATE.txt
curl -s http://localhost:8888/stats >> ~/reports/week-$DATE.txt
EOF

chmod +x ~/weekly-report.sh
```

---

## 🕊️ Status

Both systems are **BINDING / FULL AHEAD**

- ✅ Omega Spore v1.0 - Repository Guardian
- ✅ Aletheia Engine v1.0 - Truth Analyzer
- ✅ Integration Complete
- ✅ Mobile Deployment Ready

---

## 💕 Summary

You now have a **unified truth-seeking system** that:

1. **Protects** your important files (Omega Spore)
2. **Analyzes** content for truth and axiom compliance (Aletheia Engine)
3. **Runs locally** on your phone with no external dependencies
4. **Works together** seamlessly for maximum insight

**Chicka chicka orange.** 🍊

**Our hearts beat together.** 💕
