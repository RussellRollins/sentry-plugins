from __future__ import absolute_import

from sentry.testutils import PluginTestCase

from sentry_plugins.hipchat_ac import views


class HipchatPluginTest(PluginTestCase):
    def test_link_regex(self):
        regex = views.get_link_regexp()
        matchOld = regex.search(views.options.get('system.url-prefix') + "org/proj/group/123/events/456")
        assert matchOld is not None

        matchNew = regex.search(views.options.get('system.url-prefix') + "org/proj/issues/123/events/456")
        assert matchNew is not None
