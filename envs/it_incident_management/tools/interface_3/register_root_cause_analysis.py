import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class RegisterRootCauseAnalysis(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        incident_id: str,
        conducted_by_id: str,
        analysis_method: str,
        status: str = "in_progress"
    ) -> str:
        def generate_id(table: Dict[str, Any]) -> str:
            if not table:
                return "1"
            return str(max(int(k) for k in table.keys()) + 1)

        try:
            rcas = data.setdefault("root_cause_analysis", {})

            valid_methods = {"five_whys","fishbone","timeline_analysis","fault_tree"}
            if analysis_method not in valid_methods:
                return json.dumps({"success": False, "error": f"Invalid analysis_method. Must be one of {sorted(valid_methods)}"})

            valid_status = {"in_progress","completed","approved"}
            if status not in valid_status:
                return json.dumps({"success": False, "error": f"Invalid status. Must be one of {sorted(valid_status)}"})

            rca_id = generate_id(rcas)
            timestamp = "2025-09-02T23:59:59"

            new_rca = {
                "rca_id": rca_id,
                "incident_id": incident_id,
                "analysis_method": analysis_method,
                "conducted_by_id": conducted_by_id,
                "completed_at": None,
                "status": status,
                "created_at": timestamp
            }

            rcas[rca_id] = new_rca
            return json.dumps({"rca_id": rca_id, "success": True})
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_root_cause_analysis",
                "description": "Create an RCA record; sets created_at",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "conducted_by_id": {"type": "string"},
                        "analysis_method": {"type": "string", "description": "five_whys|fishbone|timeline_analysis|fault_tree"},
                        "status": {"type": "string", "description": "in_progress|completed|approved (default in_progress)"}
                    },
                    "required": ["incident_id","conducted_by_id","analysis_method"]
                }
            }
        }
