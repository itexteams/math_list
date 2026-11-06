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


def bt_dang48_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ số liệu hợp lý để góc tam giác nguyên và đẹp (tính theo độ)
                configs = [
                    {
                        'AB': 'R', 'AC': 'R\\sqrt{3}', 'obtuse_v': 'B', 'acute_v': 'C',
                        'sin_C': '\\frac{1}{2}', 'C_val': 30,
                        'sin_B': '\\frac{\\sqrt{3}}{2}', 'B_acute': 60, 'B_obtuse': 120,
                        'A_val': 30
                    },
                    {
                        'AB': 'R', 'AC': 'R\\sqrt{2}', 'obtuse_v': 'B', 'acute_v': 'C',
                        'sin_C': '\\frac{1}{2}', 'C_val': 30,
                        'sin_B': '\\frac{\\sqrt{2}}{2}', 'B_acute': 45, 'B_obtuse': 135,
                        'A_val': 15
                    },
                    {
                        'AB': 'R\\sqrt{3}', 'AC': 'R', 'obtuse_v': 'C', 'acute_v': 'B',
                        'sin_B': '\\frac{1}{2}', 'B_val': 30,
                        'sin_C': '\\frac{\\sqrt{3}}{2}', 'C_acute': 60, 'C_obtuse': 120,
                        'A_val': 30
                    },
                    {
                        'AB': 'R\\sqrt{2}', 'AC': 'R', 'obtuse_v': 'C', 'acute_v': 'B',
                        'sin_B': '\\frac{1}{2}', 'B_val': 30,
                        'sin_C': '\\frac{\\sqrt{2}}{2}', 'C_acute': 45, 'C_obtuse': 135,
                        'A_val': 15
                    }
                ]

                conf = random.choice(configs)

                # Đáp án đúng
                da = '$%s^\\circ$' % (conf['A_val'])

                # Tạo danh sách các phương án sai ngẫu nhiên không trùng với đáp án đúng
                all_choices = [15, 30, 45, 60, 75, 90, 105, 120]
                all_choices.remove(conf['A_val'])
                random.shuffle(all_choices)

                s = [
                    '$%s^\\circ$' % (all_choices[0]),
                    '$%s^\\circ$' % (all_choices[1]),
                    '$%s^\\circ$' % (all_choices[2])
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ nội tiếp đường tròn bán kính $R$, $AB = %s$, $AC = %s$. Số đo góc $A$ biết $%s$ là góc tù bằng'''
                                 % (conf['AB'], conf['AC'], conf['obtuse_v']))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                if conf['obtuse_v'] == 'B':
                    loigiai = ('''Áp dụng định lý sin trong tam giác $ABC$, ta có: \\\\
                                  $\\frac{AB}{\\sin C} = \\frac{AC}{\\sin B} = 2R$. \\\\
                                  Suy ra $\\sin C = \\frac{AB}{2R} = \\frac{%s}{2R} = %s \\Rightarrow C = %s^\\circ$ (do tam giác có $B$ tù nên $C$ là góc nhọn). \\\\
                                  Và $\\sin B = \\frac{AC}{2R} = \\frac{%s}{2R} = %s \\Rightarrow B = %s^\\circ$ hoặc $B = %s^\\circ$. \\\\
                                  Vì $B$ là góc tù nên ta nhận giá trị $B = %s^\\circ$. \\\\
                                  Tổng ba góc trong tam giác $ABC$ bằng $180^\\circ$, suy ra: \\\\
                                  $A = 180^\\circ - (B + C) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.'''
                               % (conf['AB'], conf['sin_C'], conf['C_val'],
                                  conf['AC'], conf['sin_B'], conf['B_acute'], conf['B_obtuse'],
                                  conf['B_obtuse'],
                                  conf['B_obtuse'], conf['C_val'], conf['A_val']))
                else:
                    loigiai = ('''Áp dụng định lý sin trong tam giác $ABC$, ta có: \\\\
                                  $\\frac{AB}{\\sin C} = \\frac{AC}{\\sin B} = 2R$. \\\\
                                  Suy ra $\\sin B = \\frac{AC}{2R} = \\frac{%s}{2R} = %s \\Rightarrow B = %s^\\circ$ (do tam giác có $C$ tù nên $B$ là góc nhọn). \\\\
                                  Và $\\sin C = \\frac{AB}{2R} = \\frac{%s}{2R} = %s \\Rightarrow C = %s^\\circ$ hoặc $C = %s^\\circ$. \\\\
                                  Vì $C$ là góc tù nên ta nhận giá trị $C = %s^\\circ$. \\\\
                                  Tổng ba góc trong tam giác $ABC$ bằng $180^\\circ$, suy ra: \\\\
                                  $A = 180^\\circ - (B + C) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.'''
                               % (conf['AC'], conf['sin_B'], conf['B_val'],
                                  conf['AB'], conf['sin_C'], conf['C_acute'], conf['C_obtuse'],
                                  conf['C_obtuse'],
                                  conf['B_val'], conf['C_obtuse'], conf['A_val']))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

