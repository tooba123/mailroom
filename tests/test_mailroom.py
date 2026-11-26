import mailroom


def test_main_prints_greeting(capsys):
    mailroom.main()
    captured = capsys.readouterr()
    assert "mailroom" in captured.out
