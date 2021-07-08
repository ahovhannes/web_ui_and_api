#
# Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
#
# Step functions
#

import os
import sys
import json
from enum import Enum
from behave import given, when, then
from TestFunctions.FunctionApi.Function_Api import bddApi

errorFromNewLine = "\n"
space8 = '        '

class ParameterValues(Enum):
    novalue = "novalue"
    allvalues = "allvalues"


# ----------------- github_public_users.feature -----------------

@given(u'I have endpoint with the host={host}')
def step_impl(context, host):
    context.host = host

@when(u'I add the userId={userId}')
def step_impl(context, userId):
    headers = {'Content-Type': 'application/json'}
    host = context.host +'/'+ str(userId)
    print('host='+str(host))
    #
    context.bddApi = bddApi()
    result = context.bddApi.do_api_call('get', host, headers)
    assert result.status_code == 200, "***** ERROR: Response code is: "+str(result.status_code)+", but must be 200"
    #
    context.result = result.json()
    print('response='+str(context.result))

@then(u'I will get appropriate values: name={name}, id={id}, company={company}, location={location}, public_repos={public_repos}, public_gists={public_gists}, followers={followers}, following={following}')
def step_impl(context, name, id, company, location, public_repos, public_gists, followers, following):
    print('...Expected values are:')
    print('name='+name+', id='+id+', company='+company)
    print('location='+location+', public_repos='+public_repos+', public_gists='+public_gists)
    print('followers='+followers+', following='+following)
    #
    # Checking if expected results are same with received values
    assert str(context.result["id"]) == str(id), "***** ERROR: Expected value for 'id' is: "+str(id)+", but actual result is: "+str(context.result["id"])
    assert str(context.result["name"]) == str(name), "***** ERROR: Expected value for 'name' is: "+str(name)+", but actual result is: "+str(context.result["name"])
    assert str(context.result["company"]) == str(company), "***** ERROR: Expected value for 'company' is: "+str(company)+", but actual result is: "+str(context.result["company"])
    assert str(context.result["location"]) == str(location), "***** ERROR: Expected value for 'location' is: "+str(location)+", but actual result is: "+str(context.result["location"])
    assert str(context.result["public_repos"]) == str(public_repos), "***** ERROR: Expected value for 'public_repos' is: "+str(public_repos)+", but actual result is: "+str(context.result["public_repos"])
    assert str(context.result["public_gists"]) == str(public_gists), "***** ERROR: Expected value for 'public_gists' is: "+str(public_gists)+", but actual result is: "+str(context.result["public_gists"])
    assert str(context.result["followers"]) == str(followers), "***** ERROR: Expected value for 'followers' is: "+str(followers)+", but actual result is: "+str(context.result["followers"])
    assert str(context.result["following"]) == str(following), "***** ERROR: Expected value for 'following' is: "+str(following)+", but actual result is: "+str(context.result["following"])
    print('***** SUCCES: Test passed')

