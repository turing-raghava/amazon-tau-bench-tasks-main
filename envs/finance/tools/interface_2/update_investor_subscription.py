import json
from typing import Any, Dict, Union
from tau_bench.envs.tool import Tool

class UpdateInvestorSubscription(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subscription_id: str, field_name: str, field_value: Union[str, int, float, bool],
               compliance_officer_approval: bool, finance_officer_approval: bool) -> str:
        
        if not compliance_officer_approval:
            return json.dumps({"error": "Compliance Officer approval required. Process halted."})
        
        if not finance_officer_approval:
            return json.dumps({"error": "Finance Officer approval required. Process halted."})
        
        subscriptions = data.get("subscriptions", {})
        
        # Validate subscription exists
        if str(subscription_id) not in subscriptions:
            return json.dumps({"error": f"Subscription {subscription_id} not found"})
        
        subscription = subscriptions[str(subscription_id)]
        timestamp = "2025-10-01T00:00:00"
        
        # Apply changes
        if field_name in ["amount", "status"]:
            subscription[field_name] = field_value

        subscription["updated_at"] = timestamp

        return json.dumps({"subscription_after_update": subscription})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_investor_subscription",
                "description": "Update subscription details (supports 'amount' and 'status') with required approvals",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "ID of the investor subscription to update"
                        },
                        "field_name": {
                            "type": "string",
                            "description": "Field to update",
                            "enum": ["amount", "status"]
                        },
                        "field_value": {
                            "type": ["string", "number", "boolean"],
                            "description": "New value for the field"
                        },
                        "compliance_officer_approval": {
                            "type": "boolean",
                            "description": "Compliance Officer approval flag (True/False)"
                        },
                        "finance_officer_approval": {
                            "type": "boolean",
                            "description": "Finance Officer approval flag (True/False)"
                        }
                    },
                    "required": [
                        "subscription_id",
                        "field_name",
                        "field_value",
                        "compliance_officer_approval",
                        "finance_officer_approval"
                    ]
                }
            }
        }
