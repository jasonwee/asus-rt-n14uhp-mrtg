

    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs,
                                                    timeout)

    if not (readable or writable or exceptional):
        print('  timed out, do some other work here',
              file=sys.stderr)
        continue


