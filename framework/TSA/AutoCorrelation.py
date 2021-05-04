# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
  Auto Correlation Transformation for Characterization of Time-Series Data.
"""
import numpy as np

from utils import InputData, InputTypes, xmlUtils

class AutoCorrelation( TimeSeriesCharacterizer):

  """
    Perform AutoCorrelation Transformation on time-dependent data.
  """

  @classmethod
  def getInputSpecification(cls):
    """
      Method to get a reference to a class that specifies the input data for class cls.
      @ Out, specs, InputData.ParameterInput, class to use for specifying input of cls.
    """
    specs = super(AutoCorrelation, cls).getInputSpecification()
    specs.name = 'AutoCorrelation'

    specs.description = """AutoCorrelation TimeSeriesAnalysis algorithm that characterizes the correlation of a signal. 
                           It is essentially the similarity between observations as a function of the time lag between them."""

    specs.addSub(InputData.parameterInputFactory(
      'nlags',
      contentType=InputTypes.IntegerType,
      descr=""" Number of lags to return autocorrelation for. """
    ))
    specs.addSub(InputData.parameterInputFactory(

      'confidence',
      contentType=InputTypes.FloatType,
      descr=""" If a number is given, the confidence intervals for the given level are returned. For instance if confidence=.05, 

      95 % confidence intervals are returned where the standard deviation is computed according to Bartlett”s formula. """
    ))
    return specs


  def __init__(self, *args, **kwargs):
    """
      A constructor that will appropriately intialize a time-series analysis object
      @ In, args, list, an arbitrary list of positional values
      @ In, kwargs, dict, an arbitrary dictionary of keywords and values
      @ Out, None
    """
    # general infrastructure

    super().__init__( *args, **kwargs)



  def handleInput(self, spec):
    """
      Reads user inputs into this object.
      @ In, spec, InputData.InputParams, input specifications
      @ Out, settings, dict, initialization settings for this algorithm
    """
    settings = super().handleInput(spec)
    settings['nlags'] = spec.findFirst('nlags').value

    settings['confidence'] = spec.findFirst('confidence').value

    return settings


  def characterize(self, signal, pivot, targets, settings):
    """
      This function utilizes the Discrete Wavelet Transform to
      characterize a time-dependent series of data.

      @ In, signal, np.ndarray, time series with dims [time, target]
      @ In, pivot, np.1darray, time-like parameter values
      @ In, targets, list(str), names of targets in same order as signal
      @ In, settings, dict, additional settings specific to this algorithm
      @ Out, params, dict, characteristic parameters
    """

    try:
      import statsmodels.tsa.stattools as sm
    except ModuleNotFoundError:
      print("This RAVEN TSA Module requires the statsmodels.tsa.stattools library to be installed in the current python environment")
      raise ModuleNotFoundError


    ## The pivot input parameter isn't used explicity in the
    ## transformation as it assumed/required that each element in the
    ## time-dependent series is independent, uniquely indexed and
    ## sorted in time.
    nlags = settings['nlags']

    alpha = settings['confidence']

    params = {target: {'results': {}} for target in targets}

    for i, target in enumerate(targets):
      results = params[target]['results']

      results['acf'], results['confint'] = sm.acf(signal[:, i], nlags=nlags, alpha=alpha)


    return params



  def writeXML(self, writeTo, params):
    """
      Allows the engine to put whatever it wants into an XML to print to file.
      @ In, writeTo, xmlUtils.StaticXmlElement, entity to write to
      @ In, params, dict, trained parameters as from self.characterize
      @ Out, None
    """


