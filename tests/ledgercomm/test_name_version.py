def test_get_app_and_version(cmd, hid):
    if hid:
        # for now it doesn't work with Speculos
        app_name, version = cmd.get_app_and_version()

        assert app_name == "Supra"
        assert version == "0.0.1"
