pyzilla-json
============

    zilla = JsonZilla("http://mybugzilla.example.com/jsonrpc.cgi", "login@example.com", "secure")
    print zilla.version()
    print zilla.bugs([123, 456])
    print zilla.bug(128)

You can enable DEBUG by setting environment variable `JSONZILLA_DEBUG` to `True`

