import json
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool

class ListAssets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        user_id: str
    ) -> str:
        assets = data.get("assets", {}).values()
        
        if not assets:
            raise Exception("NoAssetsFound")
        
        if not user_id:
            raise Exception("UserIdRequired")
        
        if not isinstance(user_id, str):
            raise Exception("InvalidUserIdType")
        
        result = [a for a in assets if a.get("user_id") == user_id]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_assets",
                "description": "List all assets that belong to a customer based on the customer's user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string"
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }