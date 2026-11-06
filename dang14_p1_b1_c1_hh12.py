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


def bt_dang14_p1_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo phần nội dung tích vô hướng thay đổi theo câu
                ch = ['\\overrightarrow{AB} \\cdot \\overrightarrow{CD}',
                      '\\overrightarrow{AC} \\cdot \\overrightarrow{DB}',
                      '\\overrightarrow{AB} \\cdot \\overrightarrow{BC}',
                      '\\overrightarrow{AB} \\cdot \\overrightarrow{AC}']

                kq = ['%s'%(f'$0$'),
                      '%s'%(f'$0$'),
                      '%s'%(f'$-\\frac{{a^2}}{{2}}$'),
                      '%s'%(f'$\\frac{{a^2}}{{2}}$')
                      ]

                lg = ['%s'%(f'Ta có: $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{CD}} = \\overrightarrow{{AB}} \\cdot (\\overrightarrow{{AD}} - \\overrightarrow{{AC}})$.\\\\ $= \\overrightarrow{{AB}} \\cdot \\overrightarrow{{AD}} - \\overrightarrow{{AB}} \\cdot \\overrightarrow{{AC}}$.\\\\ Vì $ABCD$ là tứ diện đều nên $AB=AC=AD=a$ và góc giữa các cạnh là $60^\\circ$.\\\\ $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{AD}} = a \\cdot a \\cdot \\cos(60^\\circ) = \\frac{{a^2}}{{2}}$.\\\\ $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{AC}} = a \\cdot a \\cdot \\cos(60^\\circ) = \\frac{{a^2}}{{2}}$.\\\\ Vậy $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{CD}} = \\frac{{a^2}}{{2}} - \\frac{{a^2}}{{2}} = 0$.'),
                      '%s'%(f'Ta có: $\\overrightarrow{{AC}} \\cdot \\overrightarrow{{DB}} = (\\overrightarrow{{AB}} + \\overrightarrow{{BC}}) \\cdot \\overrightarrow{{DB}}$.\\\\ $= \\overrightarrow{{AB}} \\cdot \\overrightarrow{{DB}} + \\overrightarrow{{BC}} \\cdot \\overrightarrow{{DB}}$.\\\\ $= \\overrightarrow{{AB}} \\cdot (\\overrightarrow{{DA}} + \\overrightarrow{{AB}}) + \\overrightarrow{{BC}} \\cdot (\\overrightarrow{{DA}} + \\overrightarrow{{AB}})$.\\\\ $= \\overrightarrow{{AB}} \\cdot \\overrightarrow{{DA}} + \\overrightarrow{{AB}}^2 + \\overrightarrow{{BC}} \\cdot \\overrightarrow{{DA}} + \\overrightarrow{{BC}} \\cdot \\overrightarrow{{AB}}$.\\\\ $= -a \\cdot a \\cos(60^\\circ) + a^2 + 0 + a \\cdot a \\cos(60^\\circ) = -\\frac{{a^2}}{{2}} + a^2 + \\frac{{a^2}}{{2}} = a^2$.\\\\ Cách khác: Ta có: $\\overrightarrow{{AC}} \\cdot \\overrightarrow{{DB}} = \\overrightarrow{{AC}} \\cdot (\\overrightarrow{{AB}} - \\overrightarrow{{AD}}) = \\overrightarrow{{AC}}\\overrightarrow{{AB}} - \\overrightarrow{{AC}}\\overrightarrow{{AD}} = \\frac{{a^2}}{{2}} - \\frac{{a^2}}{{2}} = 0$.'),
                      '%s'%(f'Ta có $\\overrightarrow{{AB}}$ và $\\overrightarrow{{BC}}$ là hai cạnh của tam giác đều $ABC$. Góc giữa hai vectơ này là $\\widehat{{ABC}} = 60^\\circ$, nhưng vectơ $\\overrightarrow{{AB}}$ và $\\overrightarrow{{BC}}$ có cùng gốc là điểm $B$. Do đó $\\widehat{{B_{{chung}}}}=120^\\circ$. \\\\ Vậy $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{BC}} = AB \\cdot BC \\cdot \\cos(120^\\circ) = a \\cdot a \\cdot \\left(-\\frac{{1}}{{2}}\\right) = -\\frac{{a^2}}{{2}}$.'),
                      '%s'%(f'Ta có: $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{AC}} = AB \\cdot AC \\cdot \\cos(\\widehat{{BAC}})$.\\\\ Vì tam giác $ABC$ là tam giác đều nên $\\widehat{{BAC}}=60^\\circ$.\\\\ Vậy $\\overrightarrow{{AB}} \\cdot \\overrightarrow{{AC}} = a \\cdot a \\cdot \\cos(60^\\circ) = a^2 \\cdot \\frac{{1}}{{2}} = \\frac{{a^2}}{{2}}$.')
                ]

                k = random.randint(0,3)
                da = kq[k]
                loigiai = lg[k]
                noidung_vochuong = ch[k]

                # Các đáp án trắc nghiệm sai (nhiễu)
                s = ['%s'%(f'$a^2$'),
                     '%s'%(f'$0$'),
                     '%s'%(f'$-\\frac{{a^2}}{{2}}$'),
                     '%s'%(f'$\\frac{{a^2}}{{2}}$'),
                     '%s'%(f'$a^2 \\sqrt{{2}}$'),
                     '%s'%(f'$\\frac{{3}}{{4}} a^2$')]

                # Lọc bỏ đáp án đúng ra khỏi danh sách nhiễu
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi=f"""Trong không gian, cho tứ diện đều $ABCD$ có các cạnh bằng $a$. Tích vô hướng ${noidung_vochuong}$ bằng"""

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

