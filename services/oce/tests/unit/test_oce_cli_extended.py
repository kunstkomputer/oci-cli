# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestOce(unittest.TestCase):
    def setUp(self):
        pass

    def test_oce_instances_list(self):
        result = util.invoke_command(['oce', 'oce-instance', 'list', '--compartment-id', 'x', '--all-pages'])
        assert 'Error: no such option: --all-pages' in result.output
        result = util.invoke_command(['oce', 'oce-instance', 'list', '--compartment-id', 'x', '--all'])
        assert 'Error: no such option: --all' in result.output

    def test_work_request_list(self):
        result = util.invoke_command(['oce', 'work-request', 'list', '--compartment-id', 'x', '--all-pages'])
        assert 'Error: no such option: --all-pages' in result.output
        result = util.invoke_command(['oce', 'work-request', 'list', '--compartment-id', 'x', '--all'])
        assert 'Error: no such option: --all' in result.output

    def test_work_request_error_list(self):
        result = util.invoke_command(['oce', 'work-request-error', 'list', '--work-request-id', 'x', '--all-pages'])
        assert 'Error: no such option: --all-pages' in result.output
        result = util.invoke_command(['oce', 'work-request-error', 'list', '--work-request-id', 'x', '--all'])
        assert 'Error: no such option: --all' in result.output

    def test_work_request_log_entry_list(self):
        result = util.invoke_command(['oce', 'work-request-log-entry', 'list', '--work-request-id', 'x', '--all-pages'])
        assert 'Error: no such option: --all-pages' in result.output
        result = util.invoke_command(['oce', 'work-request-log-entry', 'list', '--work-request-id', 'x', '--all'])
        assert 'Error: no such option: --all' in result.output
