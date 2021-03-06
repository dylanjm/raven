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

def evaluate(self):
  """
    Method required by RAVEN to run this as an ControlFunction in LogicalModel.
    @ In, self, object, object to store members on
    @ Out, model, str, the name of external model that
      will be executed by hybrid model
  """
  model = None
  if self.x > 0 and self.y > 1:
    model = 'sum'
  elif self.x > 0 and self.y <= 1:
    model = 'multiply'
  else:
    model = 'minus'

  return model
