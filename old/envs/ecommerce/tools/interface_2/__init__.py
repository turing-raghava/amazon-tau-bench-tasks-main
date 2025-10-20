from tau_bench.envs.ecommerce.tools.interface_2.cancel_order import CancelOrder
from tau_bench.envs.ecommerce.tools.interface_2.get_user_info import GetUserInfo
from tau_bench.envs.ecommerce.tools.interface_2.get_supplier_info_by_id import GetSupplierInfoById
from tau_bench.envs.ecommerce.tools.interface_2.list_purchase_order_by_supplier import ListPurchaseOrderBySupplier
from tau_bench.envs.ecommerce.tools.interface_2.modify_sales_order_item import ModifySalesOrderItem
from tau_bench.envs.ecommerce.tools.interface_2.get_order_information_by_id import GetOrderInformationById
from tau_bench.envs.ecommerce.tools.interface_2.remove_sales_order_item import RemoveSalesOrderItem
from tau_bench.envs.ecommerce.tools.interface_2.add_new_sales_order_item import AddNewSalesOrderItem
from tau_bench.envs.ecommerce.tools.interface_2.calculate_total_cost_of_order_by_id import CalculateTotalCostOfOrderById
from tau_bench.envs.ecommerce.tools.interface_2.modify_user_address import ModifyUserAddress
from tau_bench.envs.ecommerce.tools.interface_2.think import Think
from tau_bench.envs.ecommerce.tools.interface_2.get_product_by_name import GetProductByName
from tau_bench.envs.ecommerce.tools.interface_2.get_product_by_supplier import GetProductBySupplier
from tau_bench.envs.ecommerce.tools.interface_2.get_supplier_by_zip_code import GetSupplierByZipCode
from tau_bench.envs.ecommerce.tools.interface_2.get_all_orders_related_to_user import GetAllOrdersRelatedToUser


ALL_TOOLS_INTERFACE_2 = [
    CancelOrder,
    GetUserInfo,
    GetSupplierInfoById,
    ListPurchaseOrderBySupplier,
    ModifySalesOrderItem,
    GetOrderInformationById,
    RemoveSalesOrderItem,
    AddNewSalesOrderItem,
    CalculateTotalCostOfOrderById,
    ModifyUserAddress,
    Think,
    GetProductByName,
    GetProductBySupplier,
    GetSupplierByZipCode,
    GetAllOrdersRelatedToUser
]
