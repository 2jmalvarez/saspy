#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import logging
from saspy.sasproccommons import SASProcCommons


class SASqc:
    """
    This class is for SAS/STAT procedures to be called as python3 objects and use SAS as the computational engine
    This class and all the useful work in this package require a licensed version of SAS.
    To add a new procedure do the following:
    1. Create a new method for the procedure
    2. Create the set of required statements. If there are no required statements then create an empty set {}
    3. Create the legal set of statements. This can often be obtained from the documentation of the procedure.
        'procopts' should always be included in the legal set to allow flexibility in calling the procedure.
    4. Create the doc string with the following parts at a minimum:
        A. Procedure Name
        B. Required set
        C. Legal set
        D. Link to the procedure documentation
    5. Add the return call for the method using an existing procedure as an example
    6. Verify that all the statements in the required and legal sets are listed in _makeProcCallMacro method
        of sasproccommons.py
    7. Write at least one test to exercise the procedures and include it in the appropriate testing file
    """
    def __init__(self, session, *args, **kwargs):
        """Submit an initial set of macros to prepare the SAS system"""
        self.sasproduct = "qc"
        # create logging
        # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.WARN)
        self.sas = session
        logging.debug("Initialization of SAS Macro: " + self.sas.saslog())
    
    def cusum(self, **kwargs):
        """
        Python method to call the CUSUM procedure
        required_set = {}
        legal_set = {'by','xchart'}
        Documentation link:
        http://support.sas.com/documentation/cdl/en/qcug/68161/HTML/default/viewer.htm#qcug_cusum_sect001.htm
        """
        required_set = {}
        legal_set = {'by', 'xchart', 'procopts'}
        logger.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "CUSUM", required_set, legal_set, **kwargs)

    def macontrol(self, **kwargs):
        """
        Python method to call the MACONTROL procedure

        Documentation link:
        http://support.sas.com/documentation/cdl/en/qcug/68161/HTML/default/viewer.htm#qcug_macontrol_toc.htm
        """
        required_set = {}
        legal_set = {'procopts'}
        logger.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "MACONTROL", required_set, legal_set, **kwargs)

    def capability(self, **kwargs):
        """
        Python method to call the CUSUM procedure
        required_set = {}
        legal_set = {'cdfplot', 'comphist', 'histogram', 'inset', 'intervals', 'output', 'ppplot', 'probplot',
                     'qqplot', 'freq', 'weight', 'id', 'by', 'spec'}
        Documentation link:
        http://support.sas.com/documentation/cdl/en/qcug/68161/HTML/default/viewer.htm#qcug_capability_sect001.htm
        """
        required_set = {}
        legal_set = {'cdfplot', 'comphist', 'histogram', 'inset', 'intervals', 'output', 'ppplot', 'probplot',
                     'qqplot', 'freq', 'weight', 'id', 'by', 'spec', 'out', 'procopts'}
        logger.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "CAPABILITY", required_set, legal_set, **kwargs)

    def shewhart(self, **kwargs):
        """
        Python method to call the SHEWHART procedure\n
        Documentation link:
        http://support.sas.com/documentation/cdl/en/qcug/68161/HTML/default/viewer.htm#qcug_shewhart_toc.htm
        """
        required_set = {}
        legal_set = {'procopts'}
        logger.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "SHEWHART", required_set, legal_set, **kwargs)
