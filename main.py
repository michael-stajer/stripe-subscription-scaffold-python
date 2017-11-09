#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import stripe

stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])


class SubscribeHandler(webapp2.RequestHandler):
    def post(self):
        form_stripeToken = self.request.get('stripeToken')
        form_keys = self.request.params
        # 1. check for valid stripeToken

        # 2. upsert stripe_customer_id with stripeToken
        # - if we are downgrading to free plan, no stripeToken

        # 3. subscribe stripe_customer_id to plan

        # 4. display confirmation

        customer = stripe.Customer.create(
            email="jenny.rosen@example.com",
            source=form_stripeToken,
        )

        variables = {
            'st': form_stripeToken,
            'keys': form_keys,
            'stripe_customer': customer,
            'stripe_customer_id': customer.id
        }

        template = 'templates/subscribe.html'
        template = JINJA_ENVIRONMENT.get_template(template)
        self.response.write(template.render(variables))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        variables = {}
        template = "templates/main.html"
        template = JINJA_ENVIRONMENT.get_template(template)
        self.response.write(template.render(variables))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/subscribe', SubscribeHandler)
], debug=True)
