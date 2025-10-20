import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

class SearchDepartments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], company_id: Optional[str] = None, 
               manager_id: Optional[str] = None, name: Optional[str] = None) -> str:
        departments = data.get("departments", {})
        results = []
        
        for department in departments.values():
            if company_id and department.get("company_id") != company_id:
                continue
            if manager_id and department.get("manager_id") != manager_id:
                continue
            if name and name.lower() not in department.get("name", "").lower():
                continue
            results.append(department)
        
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_departments",
                "description": "Retrieves departments that match the specified filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_id": {"type": "string", "description": "Filter by company ID"},
                        "manager_id": {"type": "string", "description": "Filter by manager ID"},
                        "name": {"type": "string", "description": "Filter by department name (partial match)"}
                    },
                    "required": []
                }
            }
        }
