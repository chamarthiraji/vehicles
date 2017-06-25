#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vehicles.application import generate_application

app = generate_application()
app_prod = generate_application('vehicles.config.prod')
