entity_map = {
                 "current_tax_payable": ["应纳税额合计", ],
                 "current_taxable_sales": ["(一)按适用税率计税销售额", ],
                 "current_income_transout_money": ['进项税额转出', ],
                 "export_sales": ['(三)免、抵、退办法出口销售额', ],
                 'column5': ['(二)按简易办法计税销售额', ],
                 'tax_free_sales': ['(四)免税销售额', ],
                 'current_income_tax': ['进项税额', ],
                 'current_income_transout_money': ['进项税额转出', ],
                 'operation_revenue': ['其中：营业收入', ],
                 'operating_costs': ['其中：营业成本', ],
                 'current_income_internal': ['本期国内进项', ],
                 'current_income_internal_export': ['本期海关进口进项', ],
                 'v1_column7': ['即征即退服务、不动产和无形资产(销售额)', ],
                 'v1_column14': ['即征即退货物及加工修理修配劳务(销售额)', ],
                 'v1_column18': ['货物及加工修理修配劳务(销售额)', ]

             },

vat_entity_map = {
    "(一)按适用税率计税销售额": "current_taxable_sales",
    "(一)按适用税率征税销售额": "current_taxable_sales",
    "其中:应税货物销售额": "cargo_taxable_sale",
    "应税劳务销售额": "services_taxable_sales",
    "纳税检查调整的销售额": "adjusted_after_tax_inspection_sales",
    "(二)按简易办法计税销售额": "simple_taxable_sales",
    "(二)按简易征收办法征税销售额": "simple_taxable_sales",
    "其中:纳税检查调整的销售额": "simple_adjusted_after_tax_inspection_sales",
    "(三)免、抵、退办法出口销售额": "tax_free_export_sales",
    "(三)免、抵、退办法出口销": "tax_free_export_sales",
    "(四)免税销售额": "tax_free_sales",
    "其中:免税货物销售额": 'cargo_tax_free_sales',
    "免税劳务销售额": "services_tax_free_sales",
    "销项税额": "output_tax",
    "进项税额": "income_tax",
    "上期留抵税额": "previous_term_retained_tax",
    "进项税额转出": "transfer_out_of_input_tax",
    "免、抵、退应退税额": "tax_free_return_tax",
    "按适用税率计算的纳税检查应补缴税额": "applicable_adjusted_after_inspection_tax",
    "应抵扣税额合计": "suppose_deduction_sum_tax",
    "应抵扣税额合计17=12+13-14-15+16": "suppose_deduction_sum_tax",
    "应抵扣税额合计(12+13-14-15+16)": "suppose_deduction_sum_tax",
    "实际抵扣税额": "deduction_sum_tax",
    "实际扣税额(如17<11,则为17,否则为11)": "deduction_sum_tax",
    "应纳税额": "payable_tax",
    "应纳税额(19=11-18)": "payable_tax",
    "期末留抵税额": "end_term_retained_tax",
    "期末留抵税额(20=17-18)": "end_term_retained_tax",
    "简易计税办法计算的应纳税额": "simple_tax",
    "简易征收办法计算的应纳税额": "simple_tax",
    "按简易计税办法计算的纳税检查应补缴税额": "simple_adjusted_after_inspection_tax",
    "按简易征收办法计算的纳税检查应补缴税额": "simple_adjusted_after_inspection_tax",
    "应纳税额减征额": "reduction_payable_tax",
    "应纳税额合计": "payable_sum_tax",
    "应纳税额合计(24=19+21-23)": "payable_sum_tax",
    "期初未缴税额(多缴为负数)": "beginning_term_back_tax",
    "实收出口开具专用缴款书退税额": "actual_export_receipt_covering_warrant_return_tax",
    "实收出口开具专用缴款书退税": "actual_export_receipt_covering_warrant_return_tax",
    "本期已缴税额": "current_term_paid_tax",
    "本期已缴税额(27=28+29+30+31)": "current_term_paid_tax",
    "分次预缴税额": "stage_prepaid_tax",
    "1分次预缴税额": "stage_prepaid_tax",
    "2出口开具专用缴款书预缴税额": "export_receipt_covering_warrant_return_tax",
    "3本期缴纳上期应纳税额": "current_term_pay_previous_term_payable_tax",
    "4本期缴纳欠缴税额": "current_term_pay_arrears_tax",
    "期末未缴税额(多缴为负数)": "end_term_back_tax",
    "期末未缴税额(多缴为负数)32=24+25+26-27": "end_term_back_tax",
    "其中:欠缴税额(≥0)": "end_term_arrears_tax",
    "其中:欠缴税额(>=0)33=25+26-27": "end_term_arrears_tax",
    "本期应补(退)税额": "current_term_return_tax",
    "本期应补(退)税额34=24-28-29": "current_term_return_tax",
    "即征即退实际退税额": "actual_imposition_return_tax",
    "期初未缴查补税额": "beginning_term_back_mending_tax",
    "本期入库查补税额": "current_term_warehouse_in_mending_tax",
    "期末未缴查补税额": "end_term_back_mending_tax",
    "期末未缴查补税额38=16+22+36-37": "end_term_back_mending_tax"
}


VAT1_entity_column_mapping = {
    "jiangsu":["cargo_machining_repair_labour_tax_16",
    "service_immovables_intangible_assets_tax_16",
    "sales_tax_rate_13",
    "cargo_machining_repair_labour_tax_10",
    "service_immovables_intangible_assets_tax_10",
    "tax_rate_6",
    "actual_imposition_return_cargo_machining_repair_labour_tax",
    "actual_imposition_return_service_immovables_intangible_assets_tax",
    "simple_charge_rate_6",
    "simple_cargo_machining_repair_labour_charge_rate_5",
    "simple_service_immovables_intangible_assets_charge_rate_5",
    "simple_charge_rate_4",
    "simple_cargo_machining_repair_labour_tax_3",
    "simple_service_immovables_intangible_assets_tax_3",
    "simple_pre_charge_rate_one",
    "simple_pre_charge_rate_two",
    "simple_pre_charge_rate_three",
    "simple_actual_imposition_return_cargo_machining_repair_labour_pre_charge_rate",
    "simple_actual_imposition_return_service_immovables_intangible_assets_charge_rate"
    "cargo_machining_repair_labour_return_tax",
    "service_immovables_intangible_return_tax",
    "cargo_machining_repair_labour_tax_free",
    "service_immovables_intangible_tax_free"

    ],
    "guangzhou": ["cargo_machining_repair_labour_tax_16",
    "service_immovables_intangible_assets_tax_16",
    "sales_tax_rate_13",
    "cargo_machining_repair_labour_tax_10",
    "service_immovables_intangible_assets_tax_10",
    "tax_rate_6",
    "actual_imposition_return_cargo_machining_repair_labour_tax",
    "actual_imposition_return_service_immovables_intangible_assets_tax",
    "simple_charge_rate_6",
    "simple_cargo_machining_repair_labour_charge_rate_5",
    "simple_service_immovables_intangible_assets_charge_rate_5",
    "simple_charge_rate_4",
    "simple_cargo_machining_repair_labour_tax_3",
    "simple_service_immovables_intangible_assets_tax_3",
    "simple_pre_charge_rate_one",
    "simple_pre_charge_rate_two",
    "simple_pre_charge_rate_three",
    "simple_actual_imposition_return_cargo_machining_repair_labour_pre_charge_rate",
    "simple_actual_imposition_return_service_immovables_intangible_assets_charge_rate"
    "cargo_machining_repair_labour_return_tax",
    "service_immovables_intangible_return_tax",
    "cargo_machining_repair_labour_tax_free",
    "service_immovables_intangible_tax_free"

    ],

    "shenzhen":["cargo_machining_repair_labour_tax_16",
    "service_immovables_intangible_assets_tax_16",
    "sales_tax_rate_13",
    "cargo_machining_repair_labour_tax_10",
    "service_immovables_intangible_assets_tax_10",
    "tax_rate_6",
    "actual_imposition_return_cargo_machining_repair_labour_tax",
    "actual_imposition_return_service_immovables_intangible_assets_tax",
    "simple_charge_rate_6",
    "simple_cargo_machining_repair_labour_charge_rate_5",
    "simple_service_immovables_intangible_assets_charge_rate_5",
    "simple_charge_rate_4",
    "simple_cargo_machining_repair_labour_tax_3",
    "simple_service_immovables_intangible_assets_tax_3",
    "simple_pre_charge_rate_one",
    "simple_pre_charge_rate_two",
    "simple_pre_charge_rate_three",
    "simple_pre_charge_rate_four",
    "simple_pre_charge_rate_five",
    "simple_pre_charge_rate_six",
    "simple_pre_charge_rate_seven",
    "simple_pre_charge_rate_nine",
    "simple_actual_imposition_return_cargo_machining_repair_labour_pre_charge_rate",
    "simple_actual_imposition_return_service_immovables_intangible_assets_charge_rate"
    "cargo_machining_repair_labour_return_tax",
    "service_immovables_intangible_return_tax",
    "cargo_machining_repair_labour_tax_free",
    "service_immovables_intangible_tax_free"]


}


VAT1_entity_column_row_mapping = [
    "special_VAT_invoice_tax_sales_control_sales",
    "special_VAT_invoice_tax_sales_control_tax",
    "other_invoices_output_sales",
    "other_invoices_output_tax",
    "unissue_invoice_tax_sales",
    "unissue_invoice_tax_tax",
    "adjusted_sales_after_tax_inspection_sales",
    "adjusted_sales_after_tax_inspection_tax",
    "sum_sales",
    "sum_tax",
    "sum_price_tax_sum",
    "actual_amount_of_service_real_estate_intangible_assets_deducted_during_current_period",
    "aftertax_sales",
    "aftertax_tax"
]

VAT2_entity_column_mapping =[
    "The_VAT_special_invoice_with_conformity_certification",
    "certification_current_period_is_consistent_and_the_declaration_of_the_current_period_is_deducted",
    "previous_certification_is_consistent_and_the_current_declaration_is_deducted",
    "other_tax_proof",
    "customs_import_value_added_tax_special_payment_book",
    "purchase_invoice_sales_invoice_of_agricultural_product",
    "withholding_tax_payment_voucher",
    "additional_deduction_of_input_tax_agricultural_products",
    "other",
    "the_period_used_for_the_purchase_of_real_estate_tax_ deduction_vouchers",
    "current_immovable_property_is_allowed_to_deduct_input_tax",
    "proof_of_input_tax_deduction_for_foreign_trade_enterprises",
    "declare_the_total_amount_of_input_tax_deducted_current_period"




]

VAT2_entity_column_mapping_1 =[
    "amount_of_current_input_tax_transferred_out",
    "among_them_tax_free_items",
    "collective_welfare_individual_consumption",
    "abnormal_loss",
    "simple_tax_method_for_tax_items",
    "input_tax_that_may_not_be_deducted_by_means_of_tax_refund",
    "tax_payment_check_for_reduction_of_input_tax",
    "input_tax_indicated_in_the_special_invoice_information_form_of_red_letter",
    "tax_credit_for_the_previous_period",
    "last_period_leave_tax_credit_tax_refund",
    "other_circumstances_in_which_input_tax_shall_be_transferred_out"
    ]



VAT2_entity_column_mapping_2 =[
    "The_VAT_special_invoice_with_conformity_certification",
    "the_beginning_of_the_certification_has_been_consistent_but_did",
    "The_current_period_is_consistent_with_the_certification_and_the_current_period_has_not_been_declared_deduction",
    "been_certified_but_not_declared_the_deduction_at_end_period",
    "according to_the_provisions_of_the_tax_law_is_not_allowed_to_deduct",
    "input_tax_that_may_not_be_deducted_by_means_of_tax_refund",
    "other_tax_proof",
    "customs_import_value_added_tax_special_payment_book",
    "purchase_invoice_sales_invoice_of_agricultural_product",
    "withholding_tax_payment_voucher",
    "other"
    ]


VAT2_entity_column_mapping_3 = [
    "The_special_VAT_invoice_conforming_certification_current_period",
    "withholding_tax"


]



VAT2_entity_column_row_mapping = [
    "declare_the_input_tax_deducted_number",
    "declare_the_input_tax_deducted_money",
    "declare_the_input_tax_deducted_tax",
    "input_tax_transferred_out",
    "pending_deduct_VAT_on_purchase_number",
    "pending_deduct_VAT_on_purchase_money",
    "pending_deduct_VAT_on_purchase_tax",
    "other_number",
    "other_money",
    "other_tax"
]



area_mapping = {
    "nanjing": "jiangsu",
    "wuxi": "jiangsu",
    "suzhou": "jiangsu",
    "lianyunhang":"jiangsu",
    "jiangsu": "jiangsu",
    "changzhou": "jiangsu",
    "huaian": "jiangsu",
    "taizhou":"jiangsu",
    "yangzhou":"jiangsu",
    "zhengjiang":"jiangsu",
    'guangdong': "guangzhou",
    "dongwan":"guangzhou",
    "shantou":"guangzhou",
    "foshan":"guangzhou",
    "huizhou":"guangzhou",
    "shenzhen":"shenzhen",
    "hefei":"hefei",
    "tianjing":"tianjing3"

}