from pyq import q, K

q.set(':alpha', q('!', ["Name", "Ask", "Bid", "Last", "Vol", "Time"], [K.symbol([]), K.float([]), K.float([]), K.float([]), K.float([]), K.gtime([])]).flip)
