#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests

rdca = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """get the web cache data"""
    rdca.set(f"cached:{url}", count)
    pg_response = requests.get(url)
    rdca.incr(f"count:{url}")
    rdca.setex(f"cached:{url}", 10, rdca.get(f"cached:{url}"))
    return pg_response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
