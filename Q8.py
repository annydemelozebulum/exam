def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

# testing
print(is_valid_url("http://www.example.com"))  # output: True
print(is_valid_url("ftp://example.com"))       # output: False
