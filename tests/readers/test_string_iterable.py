"""Test String Iterable Reader."""

from gpt_index.readers.string_iterable import StringIterableReader


def test_load() -> None:
    """Test loading data into StringIterableReader."""
    reader = StringIterableReader()
    documents = reader.load_data(texts=["I went to the store", "I bought an apple"])
    assert len(documents) == 2
def test_failed_request(mocked_responses: responses.RequestsMock) -> None:
    """Test that a failed request raises an error."""
    path = "chains/path/chain.json"
    loader = Mock()

    mocked_responses.get(urljoin(URL_BASE.format(ref=DEFAULT_REF), path), status=500)

    with pytest.raises(ValueError, match=re.compile("Could not find file at .*")):
        try_load_from_hub(f"lc://{path}", loader, "chains", {"json"})
    loader.assert_not_called()
