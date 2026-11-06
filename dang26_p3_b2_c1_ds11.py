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


def bt_dang26_p3_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bài toán cố định hoặc tính toán giá trị theo mẫu trong ảnh image_39ef42.png
                # Tổng A = tan(9°) + cot(9°) + tan(15°) + cot(15°) - tan(27°) - cot(27°) = 8

                # Giá trị đúng của bài toán gốc
                kq_dung = 8

                # Tạo danh sách đáp án nhiễu không trùng với đáp án đúng
                s_choices = [4, -4, -8, 6, -6, 12, -12, 10, -10]
                if kq_dung in s_choices:
                    s_choices.remove(kq_dung)

                random.shuffle(s_choices)

                # Lấy ra 3 phương án sai từ danh sách đã trộn
                das1 = s_choices[0]
                das2 = s_choices[1]
                das3 = s_choices[2]

                # Định dạng chuỗi các phương án theo yêu cầu (không dấu chấm ở cuối)
                da = '$%s$' % (latex(kq_dung))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2))
                da_s3 = '$%s$' % (latex(das3))

                # Câu hỏi
                noidungcauhoi = ('''Giá trị biểu thức $A = \\tan 9^\\circ + \\cot 9^\\circ + \\tan 15^\\circ + \\cot 15^\\circ - \\tan 27^\\circ - \\cot 27^\\circ$ bằng bao nhiêu?''')

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, đầy đủ không viết tắt theo ảnh mẫu
                loigiai = ('''$A = \\tan 9^\\circ + \\cot 9^\\circ + \\tan 15^\\circ + \\cot 15^\\circ - \\tan 27^\\circ - \\cot 27^\\circ$ \\\\
            $A = \\tan 9^\\circ + \\cot 9^\\circ - \\tan 27^\\circ - \\cot 27^\\circ + \\tan 15^\\circ + \\cot 15^\\circ$ \\\\
            $A = \\tan 9^\\circ + \\tan 81^\\circ - \\tan 27^\\circ - \\tan 63^\\circ + \\tan 15^\\circ + \\cot 15^\\circ$. \\\\
            Ta có: \\\\
            $\\tan 9^\\circ - \\tan 27^\\circ + \\tan 81^\\circ - \\tan 63^\\circ = \\frac{-\\sin 18^\\circ}{\\cos 9^\\circ \\cdot \\cos 27^\\circ} + \\frac{\\sin 18^\\circ}{\\cos 81^\\circ \\cdot \\cos 63^\\circ}$ \\\\
            $= \\sin 18^\\circ \\left( \\frac{\\cos 9^\\circ \\cdot \\cos 27^\\circ - \\cos 81^\\circ \\cdot \\cos 63^\\circ}{\\cos 81^\\circ \\cdot \\cos 63^\\circ \\cdot \\cos 9^\\circ \\cdot \\cos 27^\\circ} \\right) = \\frac{\\sin 18^\\circ (\\cos 9^\\circ \\cdot \\cos 27^\\circ - \\sin 9^\\circ \\cdot \\sin 27^\\circ)}{\\cos 81^\\circ \\cdot \\cos 63^\\circ \\cdot \\cos 9^\\circ \\cdot \\cos 27^\\circ}$ \\\\
            $= \\frac{4 \\sin 18^\\circ \\cdot \\cos 36^\\circ}{(\\cos 72^\\circ + \\cos 90^\\circ)(\\cos 36^\\circ + \\cos 90^\\circ)} = \\frac{4 \\sin 18^\\circ}{\\cos 72^\\circ} = 4$. \\\\
            $\\tan 15^\\circ + \\cot 15^\\circ = \\frac{\\sin^2 15^\\circ + \\cos^2 15^\\circ}{\\sin 15^\\circ \\cdot \\cos 15^\\circ} = \\frac{2}{\\sin 30^\\circ} = 4$. \\\\
            Vậy $A = %s$.''' % (latex(kq_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # Xuất câu trắc nghiệm định dạng ex_choice
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content



