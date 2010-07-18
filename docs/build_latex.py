#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010 Rosen Diankov (rosen.diankov@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser(description='Preprocesses and build the latex genereted doxygen scripts',
                          usage='%prog [options] latex_directory')

    (options, args) = parser.parse_args()
    
    # preprocess the index
    refman_file = os.path.join(args[0],'refman.tex')
    doctext = open(refman_file,'r').read()
    lines = doctext.splitlines()
#     filedocindex = [i for i,s in enumerate(lines) if s.find('\\section{File Documentation}') >= 0][0]
#     if filedocindex >= 0:
#         lines.pop(filedocindex)
#         while filedocindex < len(lines):
#             if lines[filedocindex].find('\\input{') < 0:
#                 break
#             lines.pop(filedocindex)
    doctext = '\n'.join(lines)
    doctext = re.sub('\\\\section\{','\\clearemptydoublepage\n\\section{',doctext)
    open(refman_file,'w').write(doctext)

    os.chdir(args[0])
    # yes, 3 times
    os.system('pdflatex refman.tex')
    os.system('pdflatex refman.tex')
    os.system('pdflatex refman.tex')
