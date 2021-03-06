#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tweego` package."""

import pytest
import json
from tweego import scrape_twitter


def test_scrape():
    """Connection to Twitter is established"""
    json_filename = scrape_twitter.get_tweets()
    j = open(json_filename).read()
    tweet = json.loads(j)[0]
    assert tweet["username"] != ""
