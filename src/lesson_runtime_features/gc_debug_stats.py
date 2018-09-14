import gc

gc.set_debug(gc.DEBUG_STATS)

gc.collect()
print('Exiting')
