from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order



def make_contract(symbol, sec_type, exch, prim_exch, curr):
    Contract.m_symbol = symbol
    Contract.m_secType = sec_type
    Contract.m_exchange = exch
    Contract.m_currency = curr
    Contract.m_primaryExch = prim_exch
    return Contract
    
def make_order(action, quantity, price = None):
    if price is not None:
        order = Order()
        order.m_orderType = 'LMY'
        order.m_totalQuantity = quantity
        order.m_action = action
        order.m_lmtPrice = price
        
    else:
        order = Order()
        order.m_orderType = 'MKT'
        order.m_totalQuantity = quantity
        order.m_action = action
       
       
    return order
    
def main():
    conn = Connection.create(port=7497, clientId=999)
    conn.connect()
    
    oid = 1
    
    cont = make_contract('SPY', 'STK', 'SMART', 'SMART', 'USD')
    offer = make_order('BUY', 1, 200)
    conn.placeOrder(oid, cont, offer)
    conn.disconnect()
    
main() 
    
