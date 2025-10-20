import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

class UpdateInvestorDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], investor_id: str, name: Optional[str] = None,
               contact_email: Optional[str] = None, accreditation_status: Optional[str] = None,
               registration_number: Optional[int] = None, date_of_incorporation: Optional[str] = None,
               country: Optional[str] = None, address: Optional[str] = None,
               tax_id: Optional[str] = None, source_of_funds: Optional[str] = None,
               status: Optional[str] = None) -> str:
        
        investors = data.get("investors", {})
        
        # Validate investor exists
        if str(investor_id) not in investors:
            raise ValueError(f"Investor {investor_id} not found")
        
        investor = investors[str(investor_id)]
        
        # Validate accreditation status if provided
        if accreditation_status:
            valid_accreditation = ["accredited", "non_accredited"]
            if accreditation_status not in valid_accreditation:
                raise ValueError(f"Invalid accreditation status. Must be one of {valid_accreditation}")
            investor["accreditation_status"] = accreditation_status
        
        # Validate status if provided
        if status:
            valid_statuses = ["onboarded", "offboarded"]
            if status not in valid_statuses:
                raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
            investor["status"] = status
        
        # Validate source of funds if provided
        if source_of_funds:
            valid_sources = ["retained_earnings", "shareholder_capital", "asset_sale", "loan_facility", 
                            "external_investment", "government_grant", "merger_or_acquisition_proceeds",
                            "royalty_or_licensing_income", "dividend_income", "other"]
            if source_of_funds not in valid_sources:
                raise ValueError(f"Invalid source of funds. Must be one of {valid_sources}")
            investor["source_of_funds"] = source_of_funds
        
        # Update fields if provided
        if name is not None:
            investor["name"] = name
        if contact_email is not None:
            investor["contact_email"] = contact_email
        if registration_number is not None:
            investor["registration_number"] = registration_number
        if date_of_incorporation is not None:
            investor["date_of_incorporation"] = date_of_incorporation
        if country is not None:
            investor["country"] = country
        if address is not None:
            investor["address"] = address
        if tax_id is not None:
            investor["tax_id"] = tax_id
        
        return json.dumps(investor)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_investor_details",
                "description": "Update investor details for regulatory updates and address/contact changes",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "investor_id": {
                            "type": "string",
                            "description": "ID of the investor"
                        },
                        "name": {
                            "type": "string",
                            "description": "Updated investor name"
                        },
                        "contact_email": {
                            "type": "string",
                            "description": "Updated contact email"
                        },
                        "accreditation_status": {
                            "type": "string",
                            "description": "Accreditation status",
                            "enum": ["accredited", "non_accredited"]
                        },
                        "registration_number": {
                            "type": "integer",
                            "description": "Updated registration/company number"
                        },
                        "date_of_incorporation": {
                            "type": "string",
                            "description": "Updated date of incorporation (YYYY-MM-DD)"
                        },
                        "country": {
                            "type": "string",
                            "description": "Updated country"
                        },
                        "address": {
                            "type": "string",
                            "description": "Updated address"
                        },
                        "tax_id": {
                            "type": "string",
                            "description": "Updated tax identifier"
                        },
                        "source_of_funds": {
                            "type": "string",
                            "description": "Updated source of funds",
                            "enum": [
                                "retained_earnings", "shareholder_capital", "asset_sale", "loan_facility",
                                "external_investment", "government_grant", "merger_or_acquisition_proceeds",
                                "royalty_or_licensing_income", "dividend_income", "other"
                            ]
                        },
                        "status": {
                            "type": "string",
                            "description": "Updated onboarding status",
                            "enum": ["onboarded", "offboarded"]
                        }
                    },
                    "required": ["investor_id"]
                }
            }
        }
