import sys
import os

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from utils import *
except ImportError:    
    from utils import *

class AccountFormatter:
    @staticmethod
    def format(stocks, account):
        headers = [
            "상품번호", "      상품명      ", "보유수량", "  매입금액  ", "   현재가   ", 
            "평가손익율", "  평가손익  "
        ]
        
        header_str = " | ".join(headers)
        separator = "+" + "-"*100 + "+"

        log_messages = [
            f"예수금 : {account.get_total_cash_balance():,}원 평가금 : {account.get_total_evaluation_amount():,}원 손익 : {account.get_evaluation_profit_loss_sum():,}원",
            separator,
            "| " + header_str + " |",
            separator
        ]
        
        for stock in stocks:
            stock_str = "| {stock_code: <8} | {stock_name: <14} | {holding_quantity: <6}주 | {purchase_amount: >10,}원 | {current_price: >10,}원 | {evaluation_profit_loss_rate: >9.2f}% | {evaluation_profit_loss_amount: >10,}원 |".format(
                stock_code=stock.get_stock_code(),
                stock_name=stock.get_stock_name(),
                holding_quantity=stock.get_holding_quantity(),
                purchase_amount=stock.get_purchase_amount(),
                current_price=stock.get_current_price(),
                evaluation_profit_loss_rate=stock.get_evaluation_profit_loss_rate(),
                evaluation_profit_loss_amount=stock.get_evaluation_profit_loss_amount()
            )
            log_messages.append(stock_str)
        
        log_messages.append(separator)

        for message in log_messages:
            log_manager.logger.info(message)

if __name__ == "__main__":

    from account_info import DataParser

    data = {
        'ctx_area_fk100': ' ',
        'ctx_area_nk100': ' ',
        'output1': [
            {
                'pdno': '005930',
                'prdt_name': '삼성전자',
                'trad_dvsn_name': '현금',
                'bfdy_buy_qty': '0',
                'bfdy_sll_qty': '0',
                'thdt_buyqty': '0',
                'thdt_sll_qty': '0',
                'hldg_qty': '2',
                'ord_psbl_qty': '2',
                'pchs_avg_pric': '80750.0000',
                'pchs_amt': '161500',
                'prpr': '87100',
                'evlu_amt': '174200',
                'evlu_pfls_amt': '12700',
                'evlu_pfls_rt': '7.86',
                'evlu_erng_rt': '7.86377709',
                'loan_dt': '',
                'loan_amt': '0',
                'stln_slng_chgs': '0',
                'expd_dt': '',
                'fltt_rt': '2.96000000',
                'bfdy_cprs_icdc': '2500',
                'item_mgna_rt_name': '20%',
                'grta_rt_name': '',
                'sbst_pric': '0',
                'stck_loan_unpr': '0.0000'
            }
        ],
        'output2': [
            {
                'dnca_tot_amt': '9838480',
                'nxdy_excc_amt': '9838480',
                'prvs_rcdl_excc_amt': '9838480',
                'cma_evlu_amt': '0',
                'bfdy_buy_amt': '0',
                'thdt_buy_amt': '0',
                'nxdy_auto_rdpt_amt': '0',
                'bfdy_sll_amt': '0',
                'thdt_sll_amt': '0',
                'd2_auto_rdpt_amt': '0',
                'bfdy_tlex_amt': '0',
                'thdt_tlex_amt': '0',
                'tot_loan_amt': '0',
                'scts_evlu_amt': '174200',
                'tot_evlu_amt': '10012680',
                'nass_amt': '10012680',
                'fncg_gld_auto_rdpt_yn': '',
                'pchs_amt_smtl_amt': '161500',
                'evlu_amt_smtl_amt': '174200',
                'evlu_pfls_smtl_amt': '12700',
                'tot_stln_slng_chgs': '0',
                'bfdy_tot_asst_evlu_amt': '10007680',
                'asst_icdc_amt': '5000',
                'asst_icdc_erng_rt': '0.04996163'
            }
        ],
        'rt_cd': '0',
        'msg_cd': '20310000',
        'msg1': '모의투자 조회가 완료되었습니다.'
    }

    DataParser.parse_account_data(data)

    stock_info_list = DataParser.get_stock_info_list()
    account_info = DataParser.get_account_info()

    formatter = AccountFormatter()
    formatter.format(stock_info_list, account_info)