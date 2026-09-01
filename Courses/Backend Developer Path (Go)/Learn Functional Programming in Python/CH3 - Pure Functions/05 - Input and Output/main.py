def convert_case(text: str, target_format: str) -> str:
    if not (text and target_format):
        raise ValueError("no text or target format provided")

    match target_format:
        case "uppercase": return text.upper()
        case "lowercase": return text.lower()
        case "titlecase": return text.title()
        case _: raise ValueError("unsupported format: " + target_format)
