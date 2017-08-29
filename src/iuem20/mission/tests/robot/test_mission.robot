# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s iuem20.mission -t test_mission.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src iuem20.mission.testing.IUEM20_MISSION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_mission.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a mission
  Given a logged-in site administrator
    and an add mission form
   When I type 'My mission' into the title field
    and I submit the form
   Then a mission with the title 'My mission' has been created

Scenario: As a site administrator I can view a mission
  Given a logged-in site administrator
    and a mission 'My mission'
   When I go to the mission view
   Then I can see the mission title 'My mission'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add mission form
  Go To  ${PLONE_URL}/++add++mission

a mission 'My mission'
  Create content  type=mission  id=my-mission  title=My mission


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the mission view
  Go To  ${PLONE_URL}/my-mission
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a mission with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the mission title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
