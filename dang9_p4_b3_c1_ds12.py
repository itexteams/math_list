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


def bt_dang9_p4_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the constants A and B for the concentration function f(t) = (A*t) / (B + t)
                # A: The concentration of the incoming brine (The correct answer)
                A = random.choice([25, 30, 40, 50])
                # B: The ratio of initial volume to flow rate (V_0 / R) - Must be a multiple of 10 or 25 for clean numbers
                B = random.choice([100, 150, 250, 300]) 

                # The Concentration Function f(t)
                ft = (A * x) / (B + x) # Use x as the variable for sympy limit calculation

                # The limit as x approaches infinity (The correct answer: A)
                limit_ft = limit(ft, x, oo)

                # The final answer
                kq_value = limit_ft
                kq = latex(kq_value) # A

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (A)
                      ]
                da = random.choice(du)

                # Distractors
                s = ['$%s$'%(latex(kq_value + 5)), # A + 5
                     '$%s$'%(latex(kq_value - 5)) if kq_value > 5 else '$%s$'%(latex(kq_value + 10)), # A - 5 (or A + 10 if A is small)
                     '$%s$'%(latex(B)), # Distractor: B
                     '$%s$'%(latex(A*B/1000)), # Distractor: A*B/1000
                     '$%s$'%(latex(A/2)), # Distractor: A/2
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một bể chứa nước tinh khiết. Người ta bơm vào bể đó nước muối có nồng độ %s gam muối cho mỗi lít nước. Nồng độ muối trong bể được tính bởi công thức $$f(t)=\\frac{%s t}{%s + t}$$ (t là thời gian nước chảy vào bể (phút)). Tìm nồng độ muối lớn nhất mà bể có thể đạt được (đơn vị: gam/lít).'''
                                  %(latex(A), latex(A), latex(B)
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
                loigiai=('''Nồng độ muối lớn nhất mà bể có thể đạt được là tiệm cận ngang của đồ thị hàm số, tức là giới hạn của $f(t)$ khi thời gian $t \\to +\\infty$.\\\\
                         $$\\lim_{t \\to +\\infty} f(t) = \\lim_{t \\to +\\infty} \\frac{%s t}{%s + t} = \\lim_{t \\to +\\infty} \\frac{%s}{1 + \\frac{%s}{t}} = \\frac{%s}{1 + 0} = %s.$$
                         Vậy nồng độ muối lớn nhất của bể là $%s$ gam/lít.'''
                         # Đảm bảo đủ đối số: 2 + 5 + 1 = 8 đối số
                         %(latex(A), latex(B), # 1, 2
                           latex(A), latex(B), # 3, 4
                           latex(A), latex(kq_value), # 5, 6
                           latex(kq_value) # 7
                         )) 
                         # Lưu ý: Hàm số có thể được viết lại dưới dạng: f(t) = A - (A*B)/(B+t). 
                         # Lời giải trên ngắn gọn và trực tiếp hơn cho dạng toán này.


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       

