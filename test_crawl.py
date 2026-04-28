#!/usr/bin/env python3
"""Tests for crawler module."""

from pathlib import Path

import yaml

from trendradar.crawler.fetcher import DataFetcher


def test_config_file_is_readable() -> None:
    """Config file should be parseable and contain platform sources."""
    config_path = Path(__file__).resolve().parent / "config" / "config.yaml"
    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    assert isinstance(config, dict)
    assert "platforms" in config
    assert isinstance(config["platforms"].get("sources"), list)
    assert len(config["platforms"]["sources"]) > 0


def test_data_fetcher_default_api_url() -> None:
    """DataFetcher should keep a valid default API URL."""
    fetcher = DataFetcher()
    assert fetcher.api_url == DataFetcher.DEFAULT_API_URL
    assert fetcher.api_url.startswith("https://")
