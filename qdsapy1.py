def reorderLogFiles(logs: list[str]) -> list[str]:
    def get_sort_key(log: str):
        # Split into at most 2 parts: [identifier, content]
        ident, content = log.split(" ", 1)
        
        # Check if the content is letter-based or digit-based
        if content[0].isalpha():
            # Key priority: 
            # 1. Type 0 (Letter-logs come before Type 1 Digit-logs)
            # 2. Content lexicographically
            # 3. Identifier lexicographically
            return (0, content, ident)
        else:
            # Type 1 for Digit-logs. 
            # Python's sort is stable, so original order is kept for matching keys.
            return (1,)

    return sorted(logs, key=get_sort_key)