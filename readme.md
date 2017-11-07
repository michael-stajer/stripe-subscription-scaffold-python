# stripe-subscription-scaffold-python

## What is it?

A scaffold python application to implement stripe subscriptions into your
webapp. Written in python 2.7 with webapp2 framework.

## Requirements/Includes

* python 2.7 (but should be 3+ compatible)
* stripe python library (I have included the current verision in /lib)
* google app engine (but should be easily portable to flask, django)
* webapp2
* bootstrap

## Installing

## Questions

## Why?

Why is everyone paying monthly fees and a percent of revenues to companies likely chargebee, recurly, chargify? Those projects are just abstracting the underlying payment processors API. They still require developers to implement their API which is only marginally easier than implementing the stripe api. Further, if you implement one of those subscription management companies, you are signing up for a lifetime of fees.

## Get Invovled

Are you building subscription management for your web app? Consider contributing to this project. Not a python programmer, great - let's port this to other languages. Also, I want to port to django, flask, etc.