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
#************************************************************************
#* Simple analytic test ExternalModule                                  *
#* The mean and variance for this problem can be computed analytically. *
#************************************************************************
#
import numpy as np
import time

def evaluate(inp):
  return np.prod(list(1.+n for n in inp))

def run(self,Input):
  self.ans = self.x1**2*self.x2 + self.x1**2 + self.x1*self.x2 + self.x1 + self.x2 + 1.
  self.ans2 = self.x1*self.x2 + self.x1 + self.x2 + 1.
  time.sleep(0.01) #for testing collection before completion
