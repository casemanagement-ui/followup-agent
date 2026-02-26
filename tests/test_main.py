from main import (
    generate_1week_message,
    generate_24hr_message,
    generate_3week_message,
)


def test_generate_24hr_message_non_empty():
    message = generate_24hr_message("Alex", "Harbor Therapy", "https://example.com/book")
    assert isinstance(message, str)
    assert message.strip()


def test_generate_1week_message_non_empty():
    message = generate_1week_message("Alex", "Harbor Therapy", "https://example.com/book")
    assert isinstance(message, str)
    assert message.strip()


def test_generate_3week_message_non_empty():
    message = generate_3week_message("Alex", "Harbor Therapy", "https://example.com/book")
    assert isinstance(message, str)
    assert message.strip()
