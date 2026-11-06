import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p1_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                hinhve=('''\\begin{center} \n'''
                        '''\\scalebox{0.6}{ \n'''
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'''
            '''\\clip(-1.249540353972289,-0.6248497881033352) rectangle (5.597837916904829,5.686288015777371);\n'''
            '''\\draw (0.,5.)-- (4.,5.);\n'''
            '''\\draw (0.,5.)-- (2.,4.);\n'''
            '''\\draw (2.,4.)-- (4.,5.);\n'''
            '''\\draw (4.,5.)-- (4.,1.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (4.,1.)-- (0.,1.);\n'''
            '''\\draw (0.,1.)-- (2.,0.);\n'''
            '''\\draw (2.,0.)-- (4.,1.);\n'''
            '''\\draw (2.,0.)-- (2.,4.);\n'''
            '''\\draw (0.,5.)-- (0.,1.);\n'''
            '''\\draw (2.,4.)-- (4.,1.);\n'''
            '''\\draw (2.,0.)-- (4.,5.);\n'''
            '''\\draw (1.,4.5)-- (1.,0.5);\n'''
            '''\\draw (3.,2.5)-- (4.,3.);\n'''
            '''\\draw (-0.36955599787563126,5.535040704573258) node[anchor=north west] {$A$};\n'''
            '''\\draw (1.8991536701860643,4.655056348476601) node[anchor=north west] {$B$};\n'''
            '''\\draw (4,5.45) node[anchor=north west] {$C$};\n'''
            '''\\draw (-0.65,1.3276155019861207) node[anchor=north west] {$A'$};\n'''
            '''\\draw (1.624158558905859,0) node[anchor=north west] {$B'$};\n'''
            '''\\draw (0.5241781137850366,0.4) node[anchor=north west] {$M'$};\n'''
            '''\\draw (4,1.2726164797300796) node[anchor=north west] {$C'$};\n'''
            '''\\draw (2.4628936483104855,2.75) node[anchor=north west] {$O$};\n'''
            '''\\draw (4.016616027043647,3.4863271255357304) node[anchor=north west] {$I$};\n'''
            '''\\draw (0.9091712695773244,5.067549015396909) node[anchor=north west] {$M$};\n'''
            '''\\end{tikzpicture}}\n'''
            '''\\end{center}\n''')
                #NHập đáp án đúng vào đây
                du = ['''$AA'//BB'$''',
                    '''$AA'//CC'$'''
                    '''$BB'//CC'$'''
                    '''$B$ là hình chiếu của $B'$ trên mặt phẳng $(ABC)$ qua phép chiếu song song theo phương $CC'$''',
                    '''$C$ là hình chiếu của $C'$ trên mặt phẳng $(ABC)$ qua phép chiếu song song theo phương $AA'$''',
                    '''$A$ là hình chiếu của $A'$ trên mặt phẳng $(ABC)$ qua phép chiếu song song theo phương $BB'$''',
                    '''Hình chiếu của $M$ trên mặt phẳng $(A'B'C')$ qua phép chiếu song song theo phương $BB'$ là điểm $M'\\in A'B'$''',
                    '''Ảnh của $O$ qua phép chiếu song song theo phương $BC$ trên mặt phẳng $(ACC'A')$ là trung điểm $CC'$''',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('''Vì $A'$ là hình chiếu song song của $A$ trên mặt phẳng $(A'B'C')$ theo phương $BB'$ nên $AA'//BB'$.'''
                    ),
                    ('''Vì $A'$ là hình chiếu song song của $A$ trên mặt phẳng $(A'B'C')$ theo phương $CC'$ nên $AA'//CC'$.'''
                            ),
                    ('''Vì $B'$ là hình chiếu song song của $B$ trên mặt phẳng $(A'B'C')$ theo phương $CC'$ nên $BB'//CC'$.'''
                            ),
                        ('''Vì $BB'//CC'$ và $B$ thuộc $(ABC)$ nên $B$ là hình chiếu song song của $B'$ trên mặt phẳng $(ABC)$ theo phương $CC'$.'''
                            ),
                    ('''Vì $CC'//AA'$ và $C$ thuộc $(ABC)$ nên $C$ là hình chiếu song song của $C'$ trên mặt phẳng $(ABC)$ theo phương $AA'$.'''
                            ),
                        ('''Vì $AA'//BB'$ và $A$ thuộc $(ABC)$ nên $A$ là hình chiếu song song của $A'$ trên mặt phẳng $(ABC)$ theo phương $BB'$.'''
                            ),
                    ('''Trong mặt phẳng $(ABB'A')$, kẻ đường thẳng $MM'//BB'$ với $M' \\in A'B'$. Khi đó $M'$ là hình chiếu song song của điểm $M$ trên mặt phẳng $(A'B'C')$ theo phương $BB'$.'''
                            ),
                        ('''Gọi $I$ là trung điểm $CC'$. Vì $OI$ là đường trung bình của tam giác $C'BC$ nên $OI//BC$ mà $I \\in (ACC'A')$ nên $I$ là ảnh của $O$ trên mặt phẳng $(ACC'A')$ qua phép chiếu song song theo phương $BC$.'''
                                ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['''$AB'//BA'$''',
                    '''$BC'//CB'$''',
                    '''$B'$ là hình chiếu của $M$ trên mặt phẳng $(A'B'C')$ qua phép chiếu song song theo phương $CC'$''',
                    '''Hình chiếu của $M$ trên mặt phẳng $(A'B'C')$ qua phép chiếu song song theo phương $AA'$ là điểm $M'\\in B'C'$''',
                    '''Hình chiếu của $M$ trên mặt phẳng $(A'B'C')$ qua phép chiếu song song theo phương $BB'$ là điểm $M'\\in A'C'$''',
                    '''Ảnh của $O$ qua phép chiếu song song theo phương $AA'$ trên mặt phẳng $(A'B'C')$ là trung điểm $A'C'$''',
                    '''Ảnh của $O$ qua phép chiếu song song theo phương $BB'$ trên mặt phẳng $(A'B'C')$ là trung điểm $B'C'$''',
                    '''Ảnh của $O$ qua phép chiếu song song theo phương $BC$ trên mặt phẳng $(ACC'A')$ là trung điểm $BB'$''',
                    '''Ảnh của $O$ qua phép chiếu song song theo phương $B'C'$ trên mặt phẳng $(ACC'A')$ là trung điểm $AA'$''',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình lăng trụ $ABC.A'B'C'$. $M$ là một điểm trên đoạn $BC$, $O$ là tâm hình bình hành $BCC'B'$. Khẳng định nào sau đây đúng? \n'''
            )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

