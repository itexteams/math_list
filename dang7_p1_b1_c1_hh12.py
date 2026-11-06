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


def bt_dang7_p1_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)

            if dang=='7':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(Rational(a**2,2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(Rational(a**2+1,2))),
                    '$%s$'%(latex(Rational(a**2+2,2))),
                    '$%s$'%(latex(Rational(a**2+3,2))),
                    '$%s$'%(latex(Rational(a**2-1,2))),
                    '$%s$'%(latex(Rational(a**2-2,2))),
                    '$%s$'%(latex(Rational(a**2-3,2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$, gọi $O$ là tâm của đáy. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{SO}$ bằng \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{SO}\\right)=45^\\circ$ và $SO= \\dfrac{%s \\sqrt{2}}{2}$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{SO} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{SO} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{SO}) =%s \\cdot \\dfrac{%s \\sqrt{2}}{2} \\cdot \\cos 45^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(a),latex(Rational(a**2,2))
                        ))

            if dang=='6':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(Rational(a**2*3,4))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(Rational(1+a**2*3,4))),
                    '$%s$'%(latex(Rational(2+a**2*3,4))),
                    '$%s$'%(latex(Rational(3+a**2*3,4))),
                    '$%s$'%(latex(Rational(-1+a**2*3,4))),
                    '$%s$'%(latex(Rational(-2+a**2*3,4))),
                    '$%s$'%(latex(Rational(-3+a**2*3,4))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$, gọi $M$ là trung điểm của $AB$. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{SM}$ bằng  \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{SM}\\right)=30^\\circ$ và $SM= \\dfrac{%s \\sqrt{3}}{2}$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{SM} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{SM} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{SM}) =%s \\cdot \\dfrac{%s \\sqrt{3}}{2} \\cdot \\cos 30^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(a),latex(Rational(a**2*3,4))
                        ))

            if dang=='5':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(latex(a**2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(latex(a**2+1))),
                    '$%s$'%(latex(latex(a**2+2))),
                    '$%s$'%(latex(latex(a**2+3))),
                    '$%s$'%(latex(latex(a**2-1))),
                    '$%s$'%(latex(latex(a**2-2))),
                    '$%s$'%(latex(latex(a**2-3))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{AC}$ bằng  \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{AB}, \\overrightarrow{AC}\\right)=45^\\circ$ và $AC=%s \\sqrt{2}$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} =\\left| \\overrightarrow{AB} \\right| \\cdot \\left| \\overrightarrow{AC} \\right| \\cdot \\cos (\\overrightarrow{AB}, \\overrightarrow{AC}) =%s \\cdot %s \\sqrt{2} \\cdot \\cos 45^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(a),latex(a**2)
                        ))

            if dang=='4':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(Rational(a**2,2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(Rational(a**2+1,2))),
                    '$%s$'%(latex(Rational(a**2+2,2))),
                    '$%s$'%(latex(Rational(a**2+3,2))),
                    '$%s$'%(latex(Rational(a**2-1,2))),
                    '$%s$'%(latex(Rational(a**2-2,2))),
                    '$%s$'%(latex(Rational(a**2-3,2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{CD}$ bằng  \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{CD}\\right)=60^\\circ$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{CD} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{CD} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{CD}) =%s \\cdot %s \\cdot \\cos 60^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(Rational(a**2,2))
                        ))

            if dang=='3':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(-Rational(a**2,2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(-Rational(a**2+1,2))),
                    '$%s$'%(latex(-Rational(a**2+2,2))),
                    '$%s$'%(latex(-Rational(a**2+3,2))),
                    '$%s$'%(latex(-Rational(a**2-1,2))),
                    '$%s$'%(latex(Rational(a**2-2,2))),
                    '$%s$'%(latex(Rational(a**2-3,2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{BC}$ bằng  \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{BC}\\right)=60^\\circ$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{BC} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{BC} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{BC}) =%s \\cdot %s \\cdot \\cos 120^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(-Rational(a**2,2))
                        ))
            if dang=='2':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(0*a**2)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(0*a**2+1)),
                    '$%s$'%(latex(0*a**2+2)),
                    '$%s$'%(latex(0*a**2+3)),
                    '$%s$'%(latex(0*a**2-1)),
                    '$%s$'%(latex(0*a**2-2)),
                    '$%s$'%(latex(0*a**2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{SC}$ bằng \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{SC}\\right)=90^\\circ$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{SC} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{SC} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{SC}) =%s \\cdot %s \\cdot \\cos 90^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(0*a**2)
                        ))
            if dang=='1':
                # Khai báo biến
                a=randint(1,20)
                du = ['$%s$'%(latex(Rational(a**2,2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(Rational(a**2+1,2))),
                    '$%s$'%(latex(Rational(a**2+2,2))),
                    '$%s$'%(latex(Rational(a**2+3,2))),
                    '$%s$'%(latex(Rational(a**2-1,2))),
                    '$%s$'%(latex(Rational(a**2-2,2))),
                    '$%s$'%(latex(Rational(a**2-3,2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Tích vô hướng $\\overrightarrow{SA} \\cdot \\overrightarrow{SB}$ bằng \n'
                                %(latex(a))
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
                loigiai=('Ta có $\\left(\\overrightarrow{SA}, \\overrightarrow{SB}\\right)=60^\\circ$.\\\\ \n'
                        '\\hspace*{1cm} $\\overrightarrow{SA} \\cdot \\overrightarrow{SB} =\\left| \\overrightarrow{SA} \\right| \\cdot \\left| \\overrightarrow{SB} \\right| \\cdot \\cos (\\overrightarrow{SA}, \\overrightarrow{SB}) =%s \\cdot %s \\cdot \\cos 60^\\circ=%s$. \\\\ \n'
                        %(latex(a),latex(a),latex(Rational(a**2,2))
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n ').replace('\\frac', '\\dfrac')
            return content

