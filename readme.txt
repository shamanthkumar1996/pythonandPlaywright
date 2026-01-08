pytest is the testing engine -- pip install pytest
playwright is for automation -- pip install pytest-playwright

to see the logs use below
c:\PlayWright_automation\automate_AmazonSite.py -s

pytest c:\PlayWright_automation\playwright_apitest.py -s


to run group of test 

pytest -m smoke

to run all test 

pytest

to run with dynamic global input

pytest c:\PlayWright_automation\playwright_apitest.py --browser_name firefox -s

To run by testname with a pattren

pytest -k web_site

How to run in parllel 
 Install plugin 
  pip install pytest-xdist
  pytest -n 3

  Report 
  
  pip install pytest-html

  pytest - n 3 --html=report.html

To enable logging and screenshot

pytest -n 3 --tracing on --html=report.html

After running, find results at:
- HTML Report: c:\PlayWright_automation\report.html
- Trace Files: c:\PlayWright_automation\test-results\
- View trace: playwright show-trace c:\PlayWright_automation\test-results\trace.zip


