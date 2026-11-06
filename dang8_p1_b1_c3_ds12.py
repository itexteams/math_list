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


def bt_dang8_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,9)
                du = ['$%sx+%s\\cos x +\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%sx+%s\\cos x +\\text{C}$'%(latex(-a),latex(a)),
                    '$%sx+%s\\sin x +\\text{C}$'%(latex(a),latex(a)),
                    '$%sx+\\cos x +\\text{C}$'%(latex(a)),
                    '$%sx+%s\\cos x +\\text{C}$'%(latex(-a),latex(-a)),
                    '$%sx-\\cos x +\\text{C}$'%(latex(a))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\left(\\sin \\dfrac{x}{2}-\\cos \\dfrac{x}{2}\\right)^2 \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\left(\\sin \\dfrac{x}{2}-\\cos \\dfrac{x}{2}\\right)^2 \\text{d}x}&=&%s\\displaystyle \\int{\\left(\\sin^2 \\dfrac{x}{2}-2\\sin \\dfrac{x}{2}\\cos \\dfrac{x}{2}+\\cos^2 \\dfrac{x}{2}\\right) \\text{d}x} \\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(1-\\sin x\\right) \\text{d}x}\\\\ \n'
                        '&=&%sx+%s\\cos x +\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,9)
                du = ['$%sx-%s\\cos x +\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%sx+%s\\cos x +\\text{C}$'%(latex(a),latex(a)),
                    '$%sx+%s\\sin x +\\text{C}$'%(latex(a),latex(a)),
                    '$%sx+%s\\cos x +\\text{C}$'%(latex(-a),latex(a)),
                    '$%sx+%s\\cos x +\\text{C}$'%(latex(-a),latex(-a)),
                    '$%sx-\\cos x +\\text{C}$'%(latex(a))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\left(\\sin \\dfrac{x}{2}+\\cos \\dfrac{x}{2}\\right)^2 \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\left(\\sin \\dfrac{x}{2}+\\cos \\dfrac{x}{2}\\right)^2 \\text{d}x}&=&%s\\displaystyle \\int{\\left(\\sin^2 \\dfrac{x}{2}+2\\sin \\dfrac{x}{2}\\cos \\dfrac{x}{2}+\\cos^2 \\dfrac{x}{2}\\right) \\text{d}x} \\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(1+\\sin x\\right) \\text{d}x}\\\\ \n'
                        '&=&%sx-%s\\cos x +\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,15)
                du = ['$%s\\sin x +\\text{C}$'%(latex(2*a))
                    ]
                da= random.choice(du)
                s = ['$%s\\sin x +\\text{C}$'%(latex(a)),
                    '$%s\\sin x +\\text{C}$'%(latex(-a)),
                    '$%s\\sin x +\\text{C}$'%(latex(-2*a)),
                    '$%s\\cos x +\\text{C}$'%(latex(2*a)),
                    '$%s\\cos x +\\text{C}$'%(latex(-a)),


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cos^4\\dfrac{x}{2} \\text{d}x}-\\displaystyle \\int{%s\\sin^4\\dfrac{x}{2} \\text{d}x}$ bằng'
                                %(latex(a),latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\cos^4\\dfrac{x}{2} \\text{d}x}-\\displaystyle \\int{%s\\sin^4\\dfrac{x}{2} \\text{d}x}&=&%s\\displaystyle \\int{\\cos^4\\dfrac{x}{2}-\\sin^4\\dfrac{x}{2} \\text{d}x} \\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(\\cos^2\\dfrac{x}{2}-\\sin^2\\dfrac{x}{2}\\right)\\left(\\cos^2\\dfrac{x}{2}+\\sin^2\\dfrac{x}{2}\\right) \\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(\\cos^2\\dfrac{x}{2}-\\sin^2\\dfrac{x}{2}\\right)\\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{2\\cos x \\text{d}x}\\\\ \n'
                        '&=&%s\\sin x +\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(a),latex(a),latex(a),latex(a),
                        latex(a),latex(a*2))

                        )
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,9)
                du = ['$x+\\text{C}$'
                    ]
                da= random.choice(du)
                s = ['$\\sin %sx+\\text{C}$'%(latex(2*a)),
                    '$\\cos %sx+\\text{C}$'%(latex(2*a)),
                    '$%sx+\\text{C}$'%(latex(a)),
                    '$-%sx+\\text{C}$'%(latex(a)),
                    '$-%sx^2+\\text{C}$'%(latex(a)),
                    '$\\tan %sx+\\text{C}$'%(latex(a)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\sin^2%sx \\text{d}x}+\\displaystyle \\int{\\cos^2%sx \\text{d}x}$ bằng'
                                %(latex(a),latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\sin^2 %sx \\text{d}x}+\\displaystyle \\int{\\cos^2 %sx \\text{d}x}=\\displaystyle \\int{\\sin^2 %sx+\\cos^2 %sx \\text{d}x}=\\displaystyle \\int{1\\text{d}x}=x+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,20)
                du = ['$%s\\ln \\abs{\\sin x}+\\text{C}$'%(latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\ln \\abs{\\sin x}+\\text{C}$'%(latex(-a)),
                    '$%s\\ln \\abs{\\cos x}+\\text{C}$'%(latex(-a)),
                    '$%s\\ln \\abs{\\cos x}+\\text{C}$'%(latex(a)),
                    '$\\dfrac{%s}{\\sin^2x}+\\text{C}$'%(latex(-a)),
                    '$\\dfrac{%s}{\\sin^2x}+\\text{C}$'%(latex(a)),
                    '$%s\\tan x+\\text{C}$'%(latex(-a)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cot x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\cot x \\text{d}x}=%s\\displaystyle \\int{\\dfrac{\\cos x}{\\sin x} \\text{d}x}=%s\\displaystyle \\int{\\dfrac{(\\sin x)\'}{\\sin x} \\text{d}x}=%s\\ln \\abs{\\sin x}+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,20)
                du = ['$%s\\ln \\abs{\\cos x}+\\text{C}$'%(latex(-a))
                    ]
                da= random.choice(du)
                s = ['$%s\\ln \\abs{\\cos x}+\\text{C}$'%(latex(a)),
                    '$%s\\ln \\abs{\\sin x}+\\text{C}$'%(latex(-a)),
                    '$%s\\ln \\abs{\\sin x}+\\text{C}$'%(latex(a)),
                    '$\\dfrac{%s}{\\cos^2x}+\\text{C}$'%(latex(a)),
                    '$%s\\cot x+\\text{C}$'%(latex(-a)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\tan x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\tan x \\text{d}x}=%s\\displaystyle \\int{\\dfrac{\\sin x}{\\cos x} \\text{d}x}=%s\\displaystyle \\int{\\dfrac{(\\cos x)\'}{\\cos x} \\text{d}x}=%s\\ln \\abs{\\cos x}+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(-a),latex(-a))

                        )
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                a=randint(-20,-2)
                du = ['$%s\\cot x-%sx+\\text{C}$'%(latex(-a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(-a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\cot^3 x+\\text{C}$'%(latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{(%s)\\cdot\\cot^2 x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{(%s)\\cdot\\cot^2x \\text{d}x}=%s\\displaystyle \\int{\\left(\\dfrac{1}{\\sin^2x}-1\\right) \\text{d}x}=%s\\cot x-%sx+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(-a),latex(a))

                        )
            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,20)
                du = ['$%s\\cot x-%sx+\\text{C}$'%(latex(-a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(-a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\cot^3 x+\\text{C}$'%(latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cot^2 x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\cot^2x \\text{d}x}=%s\\displaystyle \\int{\\left(\\dfrac{1}{\\sin^2x}-1\\right) \\text{d}x}=%s\\cot x-%sx+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(-a),latex(a))

                        )
            if dang=='9':
                # Khai báo biến
                x=symbols('x')
                a=randint(-20,-2)
                du = ['$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\tan x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\tan x+%sx+\\text{C}$'%(latex(-a),latex(-a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\tan^3 x+\\text{C}$'%(latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{(%s)\\cdot\\tan^2 x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{(%s)\\cdot\\tan^2x \\text{d}x}=%s\\displaystyle \\int{\\left(\\dfrac{1}{\\cos^2x}-1\\right) \\text{d}x}=%s\\tan x-%sx+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='10':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,20)
                du = ['$%s\\tan x-%sx+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\tan x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\tan x+%sx+\\text{C}$'%(latex(-a),latex(-a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(a),latex(a)),
                    '$%s\\cot x+%sx+\\text{C}$'%(latex(-a),latex(a)),
                    '$%s\\tan^3 x+\\text{C}$'%(latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\tan^2 x \\text{d}x}$ bằng'
                                %(latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\tan^2x \\text{d}x}=%s\\displaystyle \\int{\\left(\\dfrac{1}{\\cos^2x}-1\\right) \\text{d}x}=%s\\tan x-%sx+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='11':
                # Khai báo biến
                x=symbols('x')
                a=randint(-15,15)
                b=randint(-20,20)

                while a==0 or b==0:
                    x=symbols('x')
                    a=randint(-15,15)
                    b=randint(-20,20)

                du = ['$%s\\cos x+%s\\sin x+\\text{C}$'%(latex(-a),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%s\\cos x+%s\\sin x+\\text{C}$'%(latex(a),latex(-b)),
                    '$%s\\cos x+%s\\sin x+\\text{C}$'%(latex(-a),latex(-b)),
                    '$%s\\sin x+%s\\cos x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}=%s\\cos x+%s\\sin x+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(b),
                        latex(-a),latex(b))

                        )
            if dang=='12':
                # Khai báo biến
                x=symbols('x')
                a=randint(-15,15)
                b=randint(1,20)

                while a==0 or b==0:
                    x=symbols('x')
                    a=randint(-15,15)
                    b=randint(1,20)

                du = ['$%s\\cos x-%s\\tan x+\\text{C}$'%(latex(-a),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\cos x-%s\\tan x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\cos x+%s\\cot x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s\\sin x-\\dfrac{%s}{\\cos^2x}\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\sin x-\\dfrac{%s}{\\cos^2x}\\right) \\text{d}x}=%s\\cos x-%s\\tan x+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(b),
                        latex(-a),latex(b))

                        )
            if dang=='13':
                # Khai báo biến
                x=symbols('x')
                a=randint(-15,15)
                b=randint(1,20)

                while a==0 or b==0:
                    x=symbols('x')
                    a=randint(-15,15)
                    b=randint(1,20)

                du = ['$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\cos x-%s\\tan x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\cos x+%s\\cot x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(-a),latex(b)),
                    '$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(-a),latex(-b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s\\sin x+\\dfrac{%s}{\\cos^2x}\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\sin x+\\dfrac{%s}{\\cos^2x}\\right) \\text{d}x}=%s\\cos x+%s\\tan x+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(b),
                        latex(-a),latex(b))

                        )
            if dang=='14':
                # Khai báo biến
                x=symbols('x')
                a=randint(-30,-1)
                b=2*a

                while a==0:
                    x=symbols('x')
                    a=randint(-30,-1)
                    b=2*a

                du = ['$%sx+%s\\sin x+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%sx-%s\\sin x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{(%s)\\cdot\\cos^2 \\dfrac{x}{2} \\text{d}x}$ bằng'
                                %(latex(b)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{(%s)\\cdot\\cos^2 \\dfrac{x}{2} \\text{d}x}&=&\\displaystyle \\int{(%s)\\cdot \\left(\\dfrac{1+\\cos x}{2}\\right) \\text{d}x} \\\\ \n'
                        '&=&\\displaystyle \\int{(%s)\\cdot \\left(1+\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&\\displaystyle \\int{\\left(%s+%s\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&%sx+%s\\sin x+\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(b),latex(b),
                        latex(a),latex(a),latex(a),latex(a),latex(a))

                        )
            if dang=='15':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,30)
                b=2*a

                while a==0:
                    x=symbols('x')
                    a=randint(1,30)
                    b=2*a

                du = ['$%sx+%s\\sin x+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%sx-%s\\sin x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cos^2 \\dfrac{x}{2} \\text{d}x}$ bằng'
                                %(latex(b)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\cos^2 \\dfrac{x}{2} \\text{d}x}&=&\\displaystyle \\int{%s\\cdot \\left(\\dfrac{1+\\cos x}{2}\\right) \\text{d}x} \\\\ \n'
                        '&=&\\displaystyle \\int{%s\\cdot \\left(1+\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&\\displaystyle \\int{\\left(%s+%s\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&%sx+%s\\sin x+\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(b),latex(b),
                        latex(a),latex(a),latex(a),latex(a),latex(a))

                        )
            if dang=='16':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,15)
                du = ['$%s\\sin x +\\text{C}$'%(latex(a))
                    ]
                da= random.choice(du)
                s = ['$%s\\sin x +\\text{C}$'%(latex(3*a)),
                    '$%s\\sin x +\\text{C}$'%(latex(-a)),
                    '$%s\\sin x +\\text{C}$'%(latex(-2*a)),
                    '$%s\\cos x +\\text{C}$'%(latex(2*a)),
                    '$%s\\cos x +\\text{C}$'%(latex(-a)),


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cos^4\\dfrac{x}{2} \\text{d}x}-\\displaystyle \\int{%s\\sin^4\\dfrac{x}{2} \\text{d}x}$ bằng'
                                %(latex(a),latex(a)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\cos^4\\dfrac{x}{2} \\text{d}x}-\\displaystyle \\int{%s\\sin^4\\dfrac{x}{2} \\text{d}x}&=&%s\\displaystyle \\int{\\cos^4\\dfrac{x}{2}-\\sin^4\\dfrac{x}{2} \\text{d}x} \\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(\\cos^2\\dfrac{x}{2}-\\sin^2\\dfrac{x}{2}\\right)\\left(\\cos^2\\dfrac{x}{2}+\\sin^2\\dfrac{x}{2}\\right) \\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{\\left(\\cos^2\\dfrac{x}{2}-\\sin^2\\dfrac{x}{2}\\right)\\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{\\cos x \\text{d}x}\\\\ \n'
                        '&=&%s\\sin x +\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(a),latex(a),latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='17':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,30)
                b=2*a

                while a==0:
                    x=symbols('x')
                    a=randint(1,30)
                    b=2*a

                du = ['$%sx-%s\\sin x+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$%sx+%s\\sin x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(a),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(a)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\cos x+\\text{C}$'%(latex(b),latex(b)),
                    '$%sx-%s\\sin x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\sin^2 \\dfrac{x}{2} \\text{d}x}$ bằng'
                                %(latex(b)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\displaystyle \\int{%s\\sin^2 \\dfrac{x}{2} \\text{d}x}&=&\\displaystyle \\int{%s\\cdot \\left(\\dfrac{1-\\cos x}{2}\\right) \\text{d}x} \\\\ \n'
                        '&=&\\displaystyle \\int{%s\\cdot \\left(1-\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&\\displaystyle \\int{\\left(%s-%s\\cos x\\right) \\text{d}x}\\\\ \n'
                        '&=&%sx-%s\\sin x+\\text{C}.\n'
                        '\\end{eqnarray*}'
                        %(latex(b),latex(b),
                        latex(a),latex(a),latex(a),latex(a),latex(a))

                        )
            if dang=='18':
                # Khai báo biến
                x=symbols('x')
                a=randint(-15,15)
                b=randint(1,20)

                while a==0 or b==0:
                    x=symbols('x')
                    a=randint(-15,15)
                    b=randint(1,20)

                du = ['$%s\\sin x+%s\\cot x+\\text{C}$'%(latex(a),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%s\\cos x+%s\\cot x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\sin x-%s\\cot x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\sin x+%s\\cot x+\\text{C}$'%(latex(2*a),latex(b)),
                    '$%s\\sin x-%s\\cot x+\\text{C}$'%(latex(a),latex(2*b)),
                    '$%s\\cos x+%s\\tan x+\\text{C}$'%(latex(a),latex(b)),
                    '$%s\\sin x+%s\\tan x+\\text{C}$'%(latex(a),latex(b))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s\\cos x-\\dfrac{%s}{\\sin^2x}\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\cos x-\\dfrac{%s}{\\sin^2x}\\right) \\text{d}x}=%s\\sin x+%s\\cot x+\\text{C}$. \\\\ \n'
                        %(latex(a),latex(b),
                        latex(a),latex(b))

                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('$1\\cos', '$\\cos').replace('$-1\\cos', '$-\\cos').replace('$1\\sin', '$\\sin').replace('$-1\\sin', '$-\\sin').replace('+1\\cot', '+\\cot').replace('-1\\cot', '-\\cot').replace('+1\\tan', '+\\tan').replace('-1\\tan', '-\\tan').replace('\\int{1cdot','\\int{').replace('\\int{-1cdot','\\int{-').replace('+1\\cos','+\\cos').replace('-1\\cos','-\\cos').replace('+1\\sin','+\\sin').replace('-1\\sin','-\\sin')
            return content

