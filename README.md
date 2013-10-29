jsonzilla
============

    zilla = JsonZilla("http://mybugzilla.example.com/jsonrpc.cgi", "login@example.com", "secure")
    print zilla.version()
    print zilla.bugs([123, 456])
    print zilla.bug(128)

Debug Mode:
-----------

You can enable `DEBUG` by setting environment variable `JSONZILLA_DEBUG` to `True`.

Build instructions:
-------------------

    python -c "import setuptools; execfile('setup.py')" bdist_egg

