class DataParser:
    class StockInfo:
        def __init__(self, data):
            self.stock_code = data['pdno']
            self.stock_name = data['prdt_name']
            self.trade_type = data['trad_dvsn_name']
            self.holding_quantity = int(data['hldg_qty'])
            self.orderable_quantity = int(data['ord_psbl_qty'])
            self.purchase_avg_price = float(data['pchs_avg_pric'])
            self.purchase_amount = int(data['pchs_amt'])
            self.current_price = int(data['prpr'])
            self.evaluation_amount = int(data['evlu_amt'])
            self.evaluation_profit_loss_amount = int(data['evlu_pfls_amt'])
            self.evaluation_profit_loss_rate = float(data['evlu_pfls_rt'])
            self.fluctuation_rate = float(data['fltt_rt'])

        def get_stock_code(self):
            return self.stock_code

        def set_stock_code(self, value):
            self.stock_code = value

        def get_stock_name(self):
            return self.stock_name

        def set_stock_name(self, value):
            self.stock_name = value

        def get_trade_type(self):
            return self.trade_type

        def set_trade_type(self, value):
            self.trade_type = value

        def get_holding_quantity(self):
            return self.holding_quantity

        def set_holding_quantity(self, value):
            self.holding_quantity = value

        def get_orderable_quantity(self):
            return self.orderable_quantity

        def set_orderable_quantity(self, value):
            self.orderable_quantity = value

        def get_purchase_avg_price(self):
            return self.purchase_avg_price

        def set_purchase_avg_price(self, value):
            self.purchase_avg_price = value

        def get_purchase_amount(self):
            return self.purchase_amount

        def set_purchase_amount(self, value):
            self.purchase_amount = value

        def get_current_price(self):
            return self.current_price

        def set_current_price(self, value):
            self.current_price = value

        def get_evaluation_amount(self):
            return self.evaluation_amount

        def set_evaluation_amount(self, value):
            self.evaluation_amount = value

        def get_evaluation_profit_loss_amount(self):
            return self.evaluation_profit_loss_amount

        def set_evaluation_profit_loss_amount(self, value):
            self.evaluation_profit_loss_amount = value

        def get_evaluation_profit_loss_rate(self):
            return self.evaluation_profit_loss_rate

        def set_evaluation_profit_loss_rate(self, value):
            self.evaluation_profit_loss_rate = value

        def get_fluctuation_rate(self):
            return self.fluctuation_rate

        def set_fluctuation_rate(self, value):
            self.fluctuation_rate = value

    class AccountInfo:
        def __init__(self, data):
            self.total_cash_balance = int(data['dnca_tot_amt'])
            self.next_day_withdrawal_amount = int(data['nxdy_excc_amt'])
            self.previous_day_withdrawal_amount = int(data['prvs_rcdl_excc_amt'])
            self.securities_evaluation_amount = int(data['scts_evlu_amt'])
            self.total_evaluation_amount = int(data['tot_evlu_amt'])
            self.net_assets = int(data['nass_amt'])
            self.purchase_amount_sum = int(data['pchs_amt_smtl_amt'])
            self.evaluation_amount_sum = int(data['evlu_amt_smtl_amt'])
            self.evaluation_profit_loss_sum = int(data['evlu_pfls_smtl_amt'])
            self.total_assets_evaluation_previous_day = int(data['bfdy_tot_asst_evlu_amt'])
            self.assets_fluctuation_amount = int(data['asst_icdc_amt'])
            self.assets_fluctuation_rate = float(data['asst_icdc_erng_rt'])

        def get_total_cash_balance(self):
            return self.total_cash_balance

        def set_total_cash_balance(self, value):
            self.total_cash_balance = value

        def get_next_day_withdrawal_amount(self):
            return self.next_day_withdrawal_amount

        def set_next_day_withdrawal_amount(self, value):
            self.next_day_withdrawal_amount = value

        def get_previous_day_withdrawal_amount(self):
            return self.previous_day_withdrawal_amount

        def set_previous_day_withdrawal_amount(self, value):
            self.previous_day_withdrawal_amount = value

        def get_securities_evaluation_amount(self):
            return self.securities_evaluation_amount

        def set_securities_evaluation_amount(self, value):
            self.securities_evaluation_amount = value

        def get_total_evaluation_amount(self):
            return self.total_evaluation_amount

        def set_total_evaluation_amount(self, value):
            self.total_evaluation_amount = value

        def get_net_assets(self):
            return self.net_assets

        def set_net_assets(self, value):
            self.net_assets = value

        def get_purchase_amount_sum(self):
            return self.purchase_amount_sum

        def set_purchase_amount_sum(self, value):
            self.purchase_amount_sum = value

        def get_evaluation_amount_sum(self):
            return self.evaluation_amount_sum

        def set_evaluation_amount_sum(self, value):
            self.evaluation_amount_sum = value

        def get_evaluation_profit_loss_sum(self):
            return self.evaluation_profit_loss_sum

        def set_evaluation_profit_loss_sum(self, value):
            self.evaluation_profit_loss_sum = value

        def get_total_assets_evaluation_previous_day(self):
            return self.total_assets_evaluation_previous_day

        def set_total_assets_evaluation_previous_day(self, value):
            self.total_assets_evaluation_previous_day = value

        def get_assets_fluctuation_amount(self):
            return self.assets_fluctuation_amount

        def set_assets_fluctuation_amount(self, value):
            self.assets_fluctuation_amount = value

        def get_assets_fluctuation_rate(self):
            return self.assets_fluctuation_rate

        def set_assets_fluctuation_rate(self, value):
            self.assets_fluctuation_rate = value

    @classmethod
    def parse_account_data(cls, data):
        cls.stock_info_list = [cls.StockInfo(stock) for stock in data['output1']]
        cls.account_info = cls.AccountInfo(data['output2'][0])

    @classmethod
    def get_stock_info_list(cls):
        return cls.stock_info_list

    @classmethod
    def get_account_info(cls):
        return cls.account_info
