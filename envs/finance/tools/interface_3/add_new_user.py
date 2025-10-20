import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class AddNewUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, 
               email: str, role: str, timezone: str, status: str = "active") -> str:
        
        def generate_id(table: Dict[str, Any]) -> int:
            if not table:
                return 1
            return max(int(k) for k in table.keys()) + 1
        
        users = data.get("users", {})
        
        # Check if email already exists
        for user in users.values():
            if user.get("email") == email:
                raise ValueError(f"Email {email} already exists")
        
        # Validate role
        valid_roles = ["system_administrator", "fund_manager", "compliance_officer", 
                      "finance_officer", "trader"]
        if role not in valid_roles:
            raise ValueError(f"Invalid role. Must be one of {valid_roles}")
        
        # Validate status
        valid_statuses = ["active", "inactive", "suspended"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
        
        user_id = generate_id(users)
        timestamp = "2025-10-01T00:00:00"
        
        new_user = {
            "user_id": str(user_id),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "role": role,
            "timezone": timezone,
            "status": status,
            "created_at": timestamp,
            "updated_at": timestamp
        }
        
        users[str(user_id)] = new_user
        return json.dumps({"new_user": new_user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_user",
                "description": "Add a new user for staff onboarding",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "User's first name"},
                        "last_name": {"type": "string", "description": "User's last name"},
                        "email": {"type": "string", "description": "User's email address"},
                        "role": {"type": "string", "description": "User role (system_administrator, fund_manager, compliance_officer, finance_officer, trader)"},
                        "timezone": {"type": "string", "description": "User's timezone (e.g., 'UTC', 'America/New_York')"},
                        "status": {"type": "string", "description": "User status (active, inactive, suspended), defaults to active"}
                    },
                    "required": ["first_name", "last_name", "email", "role", "timezone"]
                }
            }
        }
