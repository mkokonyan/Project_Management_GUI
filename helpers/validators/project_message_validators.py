def validate_message_content(value) -> None:
    if not value:
        raise ValueError("You can't send empty message")


