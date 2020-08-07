    
import datetime
import fileinput
import logging
import os
import socket
import ssl
import time

def ssl_valid_time_remaining(hostname: str) -> datetime.timedelta:
    """Get the number of days left in a cert's lifetime."""
    expires = ssl_expiry_datetime(hostname)
    logger.debug(
        'SSL cert for {} expires at {}'.format(
            hostname, expires.isoformat()
        )
    )
    return expires - datetime.datetime.utcnow()


def test_host(hostname: str, buffer_days: int=30) -> str:
    """Return test message for hostname cert expiration."""
    try:
        will_expire_in = ssl_valid_time_remaining(hostname)
    except ssl.CertificateError as e:
        return f'{hostname} cert error {e}'
    except ssl.SSLError as e:
        return f'{hostname} cert error {e}'
    except socket.timeout as e:
        return f'{hostname} could not connect'
    else:
        if will_expire_in < datetime.timedelta(days=0):
            return f'{hostname} cert will expired'
        elif will_expire_in < datetime.timedelta(days=buffer_days):
            return f'{hostname} cert will expire in {will_expire_in}'
        else:
            return f'{hostname} cert is fine'