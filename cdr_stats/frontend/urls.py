#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import patterns


urlpatterns = patterns('frontend.views',
    (r'^login/$', 'login_view'),
    (r'^logout/$', 'logout_view'),
    (r'^pleaselog/$', 'pleaselog'),
    # Password reset
    (r'^password_reset/$', 'cust_password_reset'),
    (r'^password_reset/done/$', 'cust_password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'cust_password_reset_confirm'),
    (r'^reset/done/$', 'cust_password_reset_complete'),
)
