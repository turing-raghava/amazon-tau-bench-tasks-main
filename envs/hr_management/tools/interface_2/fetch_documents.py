import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

class FetchDocuments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], document_id: Optional[str] = None, document_name: Optional[str] = None,
               document_type: Optional[str] = None, employee_id: Optional[str] = None,
               confidentiality_level: Optional[str] = None, status: Optional[str] = None) -> str:
        document_storage = data.get("document_storage", {})
        results = []
        
        for document in document_storage.values():
            if document_id and document.get("document_id") != document_id:
                continue
            if document_type and document.get("document_type") != document_type:
                continue
            if employee_id and document.get("employee_id") != employee_id:
                continue
            if confidentiality_level and document.get("confidentiality_level") != confidentiality_level:
                continue
            if status and document.get("status") != status:
                continue
            if document_name:
                if document_name.lower() != document.get("document_name").lower():
                    continue
            results.append(document)
        
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_documents",
                "description": "Fetch documents with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "document_id": {"type": "string", "description": "Filter by document ID"},
                        "document_type": {"type": "string", "description": "Filter by document type (contract, policy, handbook, form, certificate, report, resume, offer_letter)"},
                        "employee_id": {"type": "string", "description": "Filter by employee ID"},
                        "confidentiality_level": {"type": "string", "description": "Filter by confidentiality level (public, internal, confidential, restricted)"},
                        "document_name": {"type": "string", "description": "Filter by document name case insensitively"},
                        "status": {"type": "string", "description": "Filter by status (active, archived, deleted)"}
                    },
                    "required": []
                }
            }
        }
