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


def bt_dang5_p4_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the constants A and B for the cost function C(x) = A + B*x
                # A: Fixed Cost (in million VND) - must be > 100
                A = random.choice([150, 250, 300, 450, 500])
                # B: Marginal Cost (in million VND/unit) - the limit value (answer)
                B = random.choice([40, 60, 70, 80, 90])

                # The Total Cost Function C(x)
                Cx = A + B*x

                # The Average Cost Function f(x) = C(x) / x
                fx = Cx/x

                # The limit as x approaches infinity
                limit_fx = limit(fx, x, oo) # This is the correct answer: B

                # The final answer
                kq = latex(limit_fx) # B
                kq_value = limit_fx # B

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (B)
                      ]
                da = random.choice(du)

                # Distractors
                s = ['$%s$'%(latex(kq_value + 10)), # B + 10
                     '$%s$'%(latex(kq_value - 10)) if kq_value > 10 else '$%s$'%(latex(kq_value + 20)), # B - 10 (hoặc B + 20 nếu B quá nhỏ)
                     '$%s$'%(latex(A)), # Distractor: Fixed Cost (A)
                     '$%s$'%(latex(A/10)), # Distractor: A/10
                     '$%s$'%(latex(kq_value/2)), # Distractor: B/2
                     '$%s$'%(latex(A + kq_value)), # Distractor: A + B
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Chi phí sản xuất $x$ sản phẩm của một cơ sở sản xuất là $C(x)=%s+%s x$ triệu đồng. Khi cơ sở sản xuất càng nhiều sản phẩm tính chi phí sản xuất trung bình của mỗi sản phẩm.'''
                                  %(latex(A), latex(B)
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
                loigiai=('''Chi phí sản xuất trung bình của mỗi sản phẩm khi sản xuất $x$ sản phẩm là \\\\
                         $$f(x) = \\frac{C(x)}{x} = \\frac{%s+%s x}{x} = %s + \\frac{%s}{x}.$$
                         Ta có giới hạn: $$\\lim_{x \\to \\infty} f(x) = \\lim_{x \\to \\infty} \\left(%s + \\frac{%s}{x}\\right) = %s + 0 = %s.$$
                         Vậy khi sản xuất càng nhiều sản phẩm, chi phí sản xuất trung bình của mỗi sản phẩm càng gần $%s$ triệu đồng.'''
                         # Đảm bảo đủ đối số: 4 + 4 = 8
                         %(latex(A), latex(B), # 1, 2
                           latex(B), latex(A), # 3, 4
                           latex(B), latex(A), # 5, 6
                           latex(B), latex(kq_value), # 7, 8
                           latex(kq_value) # 9 - Thêm 1 đối số cho câu kết luận. Tổng cộng 9 đối số
                         ))
                         # Đếm lại: 5 %s ở dòng 1 + 3 %s ở dòng 2 + 1 %s ở dòng 3 = 9 %s. Tổng cộng 9 đối số. OK.


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       

