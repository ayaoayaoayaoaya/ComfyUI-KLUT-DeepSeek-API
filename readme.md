# ComfyUI-KLUT-DeepSeek-API

DeepSeek API integration nodes for ComfyUI - Chat and Reasoning capabilities

![ComfyUI Compatibility](https://img.shields.io/badge/ComfyUI->=0.1.0-green)
![Version](https://img.shields.io/badge/version-0.1.1-blue)

## Features
- Connect to DeepSeek's official API endpoints
- Support for both `deepseek-chat` and `deepseek-reasoner` models
- Adjustable parameters:
  - Temperature control (0.1-1.0)
  - System prompt context clearing
  - Secure API key input
- Error handling with clear feedback

## Installation

### Via ComfyUI Manager
1. Open ComfyUI
2. Go to `Manager` → `Install Custom Nodes`
3. Search for `KLUTDeepSeekAPI` and install

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ayaoayaoayaoaya/ComfyUI-KLUT-DeepSeek-API.git
Usage
Node: KLUTDeepSeekAPI
Located under klut category in node menu.

Inputs:

Parameter	Type	Description
API Key	String	Your DeepSeek API key (hidden input)
Model	List	deepseek-chat or deepseek-reasoner
Prompt	String	Your input message/question
Clear Context	Int	(0/1) Whether to clear previous context
Temperature	Float	0.1-1.0, controls response randomness
System Prompt	String (Optional)	Initial system instructions
Output:

response: String containing API response or error message

Example Workflow
json
复制
{
  "nodes": [
    {
      "type": "KLUTDeepSeekAPI",
      "inputs": {
        "api_key": "your_api_key_here",
        "model": "deepseek-chat",
        "prompt": "Explain quantum computing simply",
        "clear_context": 1,
        "temperature": 0.7,
        "system_prompt": "You are a physics professor"
      }
    }
  ]
}
Configuration
Get your API key from DeepSeek Platform

The node will automatically use DeepSeek's official endpoint:

python
复制
base_url="https://api.deepseek.com"
Troubleshooting
API errors: Check your API key validity and quota

No response: Verify internet connection

Model not working: Ensure you selected the correct model type

Changelog
v0.1.1: Initial release with basic chat functionality

Note: This is an unofficial plugin not affiliated with DeepSeek. Use at your own risk.

复制

Key improvements made:
1. Added version badges for quick reference
2. Structured the inputs/outputs in a clear table format
3. Included a complete example workflow JSON
4. Added direct link to DeepSeek's platform
5. Included troubleshooting section
6. Made the security notice prominent

Would you like me to add any of the following?
- Screenshot of the node in ComfyUI
- More detailed API error code explanations
- Rate limiting information
- Example use cases