#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
from models import User, Blog, Comment


def test():
    yield from orm.create_pool(asyncio.get_event_loop(), user='calvin', password='calvin', db='blogs')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


for x in test():
    pass